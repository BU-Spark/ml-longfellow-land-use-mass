import { useState } from "react";
import { useDropzone } from "react-dropzone";
import Loader from "../Loader";
import JSZip from "jszip";

const DragDropArea = ({ onFileUpload, isLoading }) => {
  const [isDragActive, setIsDragActive] = useState(false);

  const extractTiffsFromZip = async (zipFile) => {
    try {
      const zip = await JSZip.loadAsync(zipFile);
      const tiffFiles = [];

      await Promise.all(
        Object.keys(zip.files).map(async (filename) => {
          if (
            filename.startsWith("__MACOSX/") ||
            filename.startsWith("._") ||
            filename.toLowerCase().endsWith("/")
          ) {
            return;
          }

          if (
            filename.toLowerCase().endsWith(".tiff") ||
            filename.toLowerCase().endsWith(".tif")
          ) {
            const cleanFilename = filename.substring(
              filename.lastIndexOf("/") + 1
            );

            const fileData = await zip.files[filename].async("blob");
            const tiffFile = new File([fileData], cleanFilename, {
              type: "image/tiff",
            });
            tiffFiles.push(tiffFile);
          }
        })
      );

      return tiffFiles;
    } catch (error) {
      console.error("Error extracting TIFFs from ZIP:", error);
      return [];
    }
  };

  const onDrop = async (acceptedFiles) => {
    setIsDragActive(false);

    const tiffFiles = [];
    for (const file of acceptedFiles) {
      if (file.type === "application/zip") {
        const extractedTiffs = await extractTiffsFromZip(file);
        tiffFiles.push(...extractedTiffs);
      } else if (file.type === "image/tiff") {
        tiffFiles.push(file);
      } else {
        console.error("Unsupported file type");
      }
    }

    if (tiffFiles.length > 0) {
      onFileUpload(tiffFiles);
    }
  };

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    multiple: true,
    onDragEnter: () => setIsDragActive(true),
    onDragLeave: () => setIsDragActive(false),
    accept: {
      "image/tiff": [".tiff", ".tif"],
      "application/zip": [".zip"],
    },
  });

  return (
    <div>
      <div
        {...getRootProps()}
        className={`DragDropArea ${isDragActive ? "active" : ""}`}
      >
        {isLoading && <Loader />}
        {!isLoading && (
          <div>
            <input {...getInputProps()} />
            <span className="material-symbols-outlined">upload_file</span>
            <h3>
              Drag and drop TIFF files or a ZIP file containing TIFFs here, or
              click to browse files
            </h3>
          </div>
        )}
      </div>
    </div>
  );
};

export default DragDropArea;

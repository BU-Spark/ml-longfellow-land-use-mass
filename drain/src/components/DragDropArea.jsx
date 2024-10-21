import { useState } from 'react';
import { useDropzone } from 'react-dropzone';

const DragDropArea = ({ onFileUpload }) => {
    const [isDragActive, setIsDragActive] = useState(false);

    const onDrop = (acceptedFiles) => {
        setIsDragActive(false);

        const tiffFiles = acceptedFiles.filter(file => {
            if (file.type === 'image/tiff') {
                return true;
            } else {
                console.error('Unsupported file type');
                return false;
            }
        });

        if (tiffFiles.length > 0) {
            onFileUpload(tiffFiles); 
        }
    };

    const { getRootProps, getInputProps } = useDropzone({
        onDrop,
        multiple: true,
        onDragEnter: () => setIsDragActive(true),
        onDragLeave: () => setIsDragActive(false),
        accept: 'image/tiff'  
    });

    return (
        <div {...getRootProps()} className={`DragDropArea ${isDragActive ? 'active' : ''}`}>
            <input {...getInputProps()} />
            <span className="material-symbols-outlined">upload_file</span>
            <h3>Drag and drop TIFF files here, or click to browse files</h3>
        </div>
    );
};

export default DragDropArea;

import { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

const DragDropArea = () => {
    const [isDragActive, setIsDragActive] = useState(false);

    const onDrop = async (acceptedFiles) => {
        setIsDragActive(false);
        const formData = new FormData();

        // Append each file to the form data
        acceptedFiles.forEach(file => {
            if(file.type === 'image/tiff') {
                formData.append('file', file);
            } else {
                console.error('Unsupported file type');
                return;
            }
        });

        try {
            const response = await axios.post('http://127.0.0.1:5000/api/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                },
                responseType: 'blob' // Important for handling binary data, especially for file download
            });
            console.log('File uploaded successfully', response.data);
            downloadFile(response.data, 'output.csv');
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

    const downloadFile = (data, filename) => {
        const url = window.URL.createObjectURL(new Blob([data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', filename);
        document.body.appendChild(link);
        link.click();
        link.remove();
    };

    const { getRootProps, getInputProps } = useDropzone({
        onDrop,
        multiple: true,  // Allow multiple files
        onDragEnter: () => setIsDragActive(true),
        onDragLeave: () => setIsDragActive(false)
    });

    return (
        <div {...getRootProps()} className={`DragDropArea ${isDragActive ? 'active' : ''}`}>
            <input {...getInputProps()} />
            <span className="material-symbols-outlined">upload_file</span>
            <h3>Drag and drop TIF files here, or click to browse files</h3>
        </div>
    );
};

export default DragDropArea;


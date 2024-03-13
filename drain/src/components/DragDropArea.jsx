import React from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

const DragDropArea = () => {
    const onDrop = async (acceptedFiles) => {
        const formData = new FormData();
        formData.append('file', acceptedFiles[0]);

        try {
            const response = await axios.post('/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log('File uploaded successfully', response.data);
        } catch (error){
            console.error('Error uploading file:', error);
        }
    };

    const {getRootProps, getInputProps} = useDropzone({onDrop});

    return (
        <div {...getRootProps()} className="DragDropArea">
            <input {...getInputProps()} />
            <span className="material-symbols-outlined">upload_file</span>
            <h3>Drag and drop a TIF files here, or click to browse files</h3>
        </div>
    );
};

export default DragDropArea;

import { useState } from 'react';
import DragDropArea from './components/DragDropArea';
import './App.css'
import Banner from './components/Banner';
import Loader from './Loader';
import Papa from 'papaparse';

const App = () => {
    const [isLoading, setIsLoading] = useState(false);
    const handleFileUpload = async (files) => {
        setIsLoading(true);

        const formData = new FormData();
        files.forEach(file => {
            formData.append('file', file);
        });

        try {
            const response = await fetch('http://localhost:5000/api/upload', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const blob = await response.blob();
            const text = await blob.text();

            Papa.parse(text, {
                complete: (results) => {
                    console.log("Parsed CSV Data:", results.data);

                },
                header: true,
            });
        } catch (error) {
            console.error('Error during fetch:', error);
        }finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="App">
            {isLoading && <Loader />}
            <Banner/>
            <header className="App-header">
                <h1>DRAIN: Deed Restriction Artificial Intelligence Notification System</h1>
                <h3>OCR File Upload</h3>
                <p>Convert your files to text using OCR</p>
                <DragDropArea onFileUpload={handleFileUpload}/>
            </header>
        </div>
    );
}

export default App;



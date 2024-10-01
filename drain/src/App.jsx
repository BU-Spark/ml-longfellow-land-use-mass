import { useState } from 'react';
import DragDropArea from './components/DragDropArea';
import './App.css';
import Banner from './components/Banner';
import Loader from './Loader';

const App = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [ocrEngine, setOcrEngine] = useState('google');

    const handleFileUpload = async (files) => {
        setIsLoading(true);

        const formData = new FormData();
        files.forEach(file => {
            formData.append('file', file);
        });

        formData.append('ocr_engine', ocrEngine);

        try {
            const response = await fetch('http://127.0.0.1:5000/api/upload', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            console.log('Response from server:', data);
        } catch (error) {
            console.error('Error during fetch:', error);
        } finally {
            setIsLoading(false);
        }
    };

    const handleOcrChange = (event) => {
        setOcrEngine(event.target.value);
    };

    return (
        <div className="App">
            {isLoading && <Loader />}
            <Banner />
            <header className="App-header">
                <h1>DRAIN: Deed Restriction Artificial Intelligence Notification System</h1>
                <h3>OCR File Upload</h3>
                <p>Convert your files to text using OCR</p>

                <DragDropArea onFileUpload={handleFileUpload} />
                <div className="ocr-select-container">
                    <label htmlFor="ocr-select">Select OCR Engine: </label>
                    <select id="ocr-select" value={ocrEngine} onChange={handleOcrChange} className="ocr-select">
                        <option value="google">Google OCR</option>
                        <option value="azure">Azure OCR</option>
                    </select>
                </div>
            </header>
        </div>
    );
}

export default App;

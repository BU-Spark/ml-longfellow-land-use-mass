import React, { useState } from 'react';
import DragDropArea from './components/DragDropArea';
import './App.css'
import Banner from './components/Banner';
import Loader from './Loader';

const App = () => {
    const [isLoading, setIsLoading] = useState(false);
    const handleFileUpload = async () => {
        setIsLoading(true);

        setIsLoading(false);
    }

    return (
        <div className="App">
            {isLoading && <Loader />}
            <Banner/>
            <header className="App-header">
                <h1>DRAIN: OCR File Upload</h1>
                <h3>Deed Restriction Artificial Intelligence Notification System</h3>
                <p>Convert your files to text using OCR</p>
            </header>
            <main>
                <DragDropArea />
            </main>
        </div>
    );
}

export default App;
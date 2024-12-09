import { useState } from "react";
import DragDropArea from "./components/DragDropArea";
import "./App.css";
import Banner from "./components/Banner";

const BACKEND_URL = "https://spark-ds549-f24-racist-deeds.hf.space"

const bigotryTerms = new Set([
  "irishman", "greek", "portugese", "mulatto", "quadroon", "chinaman", "jap", "hebrew", 
  "pole", "french canadian", "canadien", "quebecois", "arab", "turk", "frenchman", "german", 
  "spaniard", "slav", "russian", "persian", "korean", "negro", "colored", "polander", "polish", 
  "italian", "african", "hindu", "japanese", "chinese", "catholic", "jew", "jewish", "white", 
  "aryan", "caucasian", "race", "semetic", "shall not be re-sold", "shall not be resold", 
  "shall not be sold"
].map(word => word.toLowerCase())); 

const highlightText = (text, shouldHighlight) => {
  console.log('Should highlight:', shouldHighlight);  
  if (!shouldHighlight) {
    return text;
  }
  const words = text.split(/(\s+)/);
  return words.map((word, index) => (
    bigotryTerms.has(word.toLowerCase()) ?
    <span key={index} style={{ backgroundColor: 'yellow' }}>{word}</span> :
    word
  ));
};

const TiffResult = ({
  fileName,
  spellcheckedText,
  analysisResult,
  extractedInfo,
}) => (
  <div className="results-container">
    <h3>{fileName}</h3>
    <div className="result-box">
      <h4>Spellchecked Text:</h4>
      <p>{highlightText(spellcheckedText, analysisResult)}</p>
    </div>
    <div className="result-box">
      <h4>Analysis Result:</h4>
      <p>
        {analysisResult ? (
          <span className="racist-label">Racist Content Detected</span>
        ) : (
          <span className="non-racist-label">No Racist Content</span>
        )}
      </p>
    </div>
    <div className="result-box">
      <h4>Extracted Information:</h4>
      {extractedInfo.names.length > 0 && (
        <div>
          <h5>Names:</h5>
          <ul>
            {extractedInfo.names.map((name, index) => (
              <li key={index}>{name}</li>
            ))}
          </ul>
        </div>
      )}
      {extractedInfo.locations.length > 0 && (
        <div>
          <h5>Locations:</h5>
          <ul>
            {extractedInfo.locations.map((location, index) => (
              <li key={index}>{location}</li>
            ))}
          </ul>
        </div>
      )}
      <div>
        <h5>Book Numbers:</h5>
        <p>
          {extractedInfo.book_numbers && extractedInfo.book_numbers.length > 0
            ? extractedInfo.book_numbers.join(", ")
            : "None"}
        </p>
      </div>
      <div>
        <h5>Page Numbers:</h5>
        <p>
          {extractedInfo.page_numbers && extractedInfo.page_numbers.length > 0
            ? extractedInfo.page_numbers.join(", ")
            : "None"}
        </p>
      </div>
    </div>
  </div>
);

const App = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [ocrEngine, setOcrEngine] = useState("google");
  const [analysisMethod, setAnalysisMethod] = useState("logistic_regression");
  const [results, setResults] = useState([]);
  const [selectedResult, setSelectedResult] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");

  const handleFileUpload = async (files) => {
    setResults([]);
    setIsLoading(true);

    try {
      const newResults = [];
      for (const file of files) {
        const formData = new FormData();
        formData.append("file", file);
        formData.append("ocr_engine", ocrEngine);
        formData.append("analysis_method", analysisMethod);

        // Reads from HuggingFace backend
        const response = await fetch(
          `${BACKEND_URL}/api/upload`,
          {
            method: "POST",
            body: formData,
          }
        );

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        newResults.push({
          fileName: file.name,
          spellcheckedText: data.spellchecked_text || "No text available",
          analysisResult: data.result || false,
          extractedInfo: data.extracted_info || { names: [], locations: [] },
        });
      }
      setResults(newResults);
      setSelectedResult("all");
    } catch (error) {
      console.error("Error during fetch:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDownloadExcel = async () => {
    const response = await fetch(
      `${BACKEND_URL}/api/download_excel`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(results),
      }
    );

    if (response.ok) {
      const blob = await response.blob();
      const downloadUrl = window.URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = downloadUrl;
      link.download = "analysis_results.xlsx";
      document.body.appendChild(link);
      link.click();
      link.remove();
    } else {
      console.error("Failed to download file:", await response.text());
    }
  };

  const handleOcrChange = (event) => {
    setOcrEngine(event.target.value);
  };

  const handleAnalysisChange = (event) => {
    setAnalysisMethod(event.target.value);
  };

  const handleSearchConfirm = () => {
    if (!searchTerm.trim()) {
      setSelectedResult("all");
    } else {
      const foundResult = results.find((result) =>
        result.fileName.toLowerCase().includes(searchTerm.toLowerCase())
      );
      if (foundResult) {
        setSelectedResult(foundResult);
      } else {
        alert("File not found!");
      }
    }
  };

  const handleDropdownChange = (event) => {
    const value = event.target.value;
    if (value === "all") {
      setSelectedResult("all");
    } else {
      const selectedFile = results.find((result) => result.fileName === value);
      setSelectedResult(selectedFile);
    }
  };

  return (
    <div className="App">
      <Banner />
      <header className="App-header">
        <h1>
          DRAIN: Deed Restriction Artificial Intelligence Notification System
        </h1>
        <h3>OCR File Upload</h3>
        <p>Convert your files to text using OCR</p>

        <DragDropArea onFileUpload={handleFileUpload} isLoading={isLoading} />

        <div className="selector-container">
          <div className="select-box">
            <label htmlFor="ocr-select">Select OCR Engine: </label>
            <select
              id="ocr-select"
              value={ocrEngine}
              onChange={handleOcrChange}
              className="select-input"
            >
              <option value="google">Google OCR</option>
            </select>
          </div>

          <div className="select-box">
            <label htmlFor="analysis-select">Select Analysis Method: </label>
            <select
              id="analysis-select"
              value={analysisMethod}
              onChange={handleAnalysisChange}
              className="select-input"
            >
              <option value="chatgpt">ChatGPT</option>
              <option value="logistic_regression">Logistic Regression</option>
            </select>
          </div>
        </div>

        {results.length > 0 && (
          <div className="search-container">
            <input
              type="text"
              placeholder="Search file names..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="search-input"
            />
            <button onClick={handleSearchConfirm} className="go-button">
              Go
            </button>
          </div>
        )}

        {results.length > 0 && (
          <div className="file-dropdown-container">
            <div className="select-box">
              <select
                id="file-select"
                onChange={handleDropdownChange}
                className="select-input"
              >
                <option value="all">View All</option>
                {results.map((result) => (
                  <option key={result.fileName} value={result.fileName}>
                    {result.fileName}
                  </option>
                ))}
              </select>
            </div>
            <button onClick={handleDownloadExcel} className="download-button">
              Download Results as Excel
            </button>
          </div>
        )}

        {selectedResult === "all"
          ? results.map((result) => (
              <TiffResult
                key={result.fileName}
                fileName={result.fileName}
                spellcheckedText={result.spellcheckedText}
                analysisResult={result.analysisResult}
                extractedInfo={result.extractedInfo}
              />
            ))
          : selectedResult && (
              <TiffResult
                fileName={selectedResult.fileName}
                spellcheckedText={selectedResult.spellcheckedText}
                analysisResult={selectedResult.analysisResult}
                extractedInfo={selectedResult.extractedInfo}
              />
            )}
      </header>
    </div>
  );
};

export default App;

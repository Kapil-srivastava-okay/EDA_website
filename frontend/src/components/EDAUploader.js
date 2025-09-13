import React, { useState } from "react";
import axios from "axios";

function EDAUploader() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://127.0.0.1:5000/upload-csv/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResults(response.data.eda_results);
    } catch (error) {
      console.error("Upload failed:", error);
    }
  };

  return (
    <div>
      <h2>Upload CSV for EDA</h2>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      {results && (
        <div>
          <h3>Quick Info</h3>
          <pre>{results.info}</pre>

          <h3>Missing Values</h3>
          <pre>{JSON.stringify(results.missing_values, null, 2)}</pre>

          <h3>Descriptive Stats</h3>
          <pre>{JSON.stringify(results.descriptive_stats, null, 2)}</pre>

          <h3>Correlation Matrix</h3>
          <img
            src={`data:image/png;base64,${results.correlation_matrix}`}
            alt="Correlation Heatmap"
            style={{ maxWidth: "100%" }}
          />
        </div>
      )}
    </div>
  );
}

export default EDAUploader;

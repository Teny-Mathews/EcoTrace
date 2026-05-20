import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [category, setCategory] = useState('MIXED');
  const [loading, setLoading] = useState(false);
  const [previewData, setPreviewData] = useState(null);
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError('');
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) {
      setError('Please select an image first.');
      return;
    }

    setLoading(true);
    setError('');
    setPreviewData(null);

    // Prepare multi-part form data payload
    const formData = new FormData();
    formData.append('image', file);
    formData.append('category', category);

    try {
      // Direct request to our local Django backend
      const response = await axios.post('http://localhost:8000/api/logistics/analyze/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setPreviewData(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to connect to backend engine.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '50px auto', padding: '20px', fontFamily: 'sans-serif' }}>
      <h2 style={{ color: '#2e7d32' }}>EcoTrace: Smart Pickup Request</h2>
      <p style={{ color: '#555' }}>Upload an image of your sorted waste items to instantly evaluate environmental metrics.</p>
      
      <form onSubmit={handleUpload} style={{ background: '#f5f5f5', padding: '20px', borderRadius: '8px' }}>
        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', fontWeight: 'bold', marginBottom: '5px' }}>Waste Material Type:</label>
          <select value={category} onChange={(e) => setCategory(e.target.value)} style={{ width: '100%', padding: '8px', borderRadius: '4px' }}>
            <option value="MIXED">Mixed Recyclables</option>
            <option value="PLASTIC">Plastic Waste</option>
            <option value="ORGANIC">Organic / Food Waste</option>
            <option value="E_WASTE">Electronic Waste</option>
            <option value="PAPER">Paper & Cardboard</option>
            <option value="GLASS">Glass & Bottles</option>
          </select>
        </div>

        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', fontWeight: 'bold', marginBottom: '5px' }}>Select Image:</label>
          <input type="file" accept="image/*" onChange={handleFileChange} style={{ width: '100%' }} />
        </div>

        <button type="submit" disabled={loading} style={{ background: '#2e7d32', color: '#fff', border: 'none', padding: '10px 15px', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}>
          {loading ? 'Analyzing Waste Patterns...' : 'Submit to AI Engine'}
        </button>
      </form>

      {error && <p style={{ color: '#d32f2f', fontWeight: 'bold', marginTop: '15px' }}>{error}</p>}

      {/* The UI Hydration State (Sustainability Preview Card) */}
      {previewData && (
        <div style={{ marginTop: '25px', padding: '20px', border: '2px solid #2e7d32', borderRadius: '8px', background: '#e8f5e9' }}>
          <h3 style={{ color: '#1b5e20', marginTop: 0 }}>📊 Sustainability Preview</h3>
          <p><strong>Identified Category:</strong> {previewData.analyzed_category}</p>
          <p><strong>Estimated Volume:</strong> {previewData.estimated_volume_m3} m³</p>
          <p style={{ fontSize: '1.2rem', color: '#2e7d32' }}>
            <strong>Projected Carbon Offsets:</strong> {previewData.carbon_offset_kg} kg CO₂e
          </p>
          <p style={{ fontStyle: 'italic', fontSize: '0.9rem', color: '#666', marginBottom: 0 }}>
            {previewData.message}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';

const Login = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    try {
      // Send credentials to our Django Login API
      const response = await axios.post(
        'http://localhost:8000/api/users/login/',
        formData,
        { withCredentials: true } 
      );

      if (response.status === 200) {
        setSuccess('Login successful! Welcome back.');
        
        // 🧠 UPDATED: Extract ALL role flags from the backend response
        const { is_admin, is_driver, is_superuser } = response.data.user;

        setTimeout(() => {
          // 🧠 UPDATED: Permanent Dynamic Routing for all 3 privilege tiers
          if (is_admin || is_superuser) {
            navigate('/admin-dashboard'); // Send admins/superusers to the control room
          } else if (is_driver) {
            navigate('/driver-dashboard'); // Send drivers to their logistics screen
          } else {
            navigate('/dashboard'); // Send regular citizens to their home screen
          }
        }, 1500);
      }
    } catch (err) {
      if (err.response && err.response.data) {
        // Extract the error message Django sends (e.g., "Incorrect username or password")
        const errorMessages = Object.values(err.response.data).flat();
        setError(errorMessages.join(' '));
      } else {
        setError('Something went wrong. Please check your backend connection.');
      }
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '50px auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px', backgroundColor: '#fff' }}>
      <h2 style={{ textAlign: 'center' }}>Log In</h2>

      {error && <div style={{ color: '#dc3545', background: '#f8d7da', padding: '10px', borderRadius: '4px', marginBottom: '10px' }}>{error}</div>}
      {success && <div style={{ color: '#155724', background: '#d4edda', padding: '10px', borderRadius: '4px', marginBottom: '10px' }}>{success}</div>}

      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '10px' }}>
          <label style={{ display: 'block', fontWeight: 'bold' }}>Username:</label>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>

        <div style={{ marginBottom: '20px' }}>
          <label style={{ display: 'block', fontWeight: 'bold' }}>Password:</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            style={{ width: '100%', padding: '8px', marginTop: '5px' }}
          />
        </div>

        <button type="submit" style={{ width: '100%', padding: '10px', background: '#007bff', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}>
          Log In
        </button>
      </form>
      
      <p style={{ textAlign: 'center', marginTop: '15px', fontSize: '14px' }}>
        Don't have an account? <Link to="/register">Register here</Link>
      </p>
    </div>
  );
};

export default Login;
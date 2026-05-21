import React from 'react';
import { Link } from 'react-router-dom';

const Landing = () => {
  return (
    <div style={{ textAlign: 'center', padding: '100px 20px', fontFamily: 'sans-serif' }}>
      <h1 style={{ color: '#28a745', fontSize: '3.5rem', marginBottom: '10px' }}>
        🌍 EcoTrace
      </h1>
      <h3 style={{ color: '#333', fontSize: '1.5rem', marginBottom: '20px' }}>
        Sustainable Logistics & Carbon Tracking
      </h3>
      <p style={{ fontSize: '1.1rem', color: '#666', maxWidth: '600px', margin: '0 auto 40px', lineHeight: '1.6' }}>
        Join the movement towards a greener future. Track your carbon footprint, optimize eco-friendly logistics, and manage your environmental impact all in one place.
      </p>
      
      <div style={{ display: 'flex', justifyContent: 'center', gap: '20px' }}>
        <Link 
          to="/register" 
          style={{ padding: '12px 30px', background: '#28a745', color: '#fff', textDecoration: 'none', borderRadius: '5px', fontWeight: 'bold', fontSize: '1.1rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}
        >
          Join EcoTrace
        </Link>
        <Link 
          to="/login" 
          style={{ padding: '12px 30px', background: '#007bff', color: '#fff', textDecoration: 'none', borderRadius: '5px', fontWeight: 'bold', fontSize: '1.1rem', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}
        >
          Log In
        </Link>
      </div>
    </div>
  );
};

export default Landing; 

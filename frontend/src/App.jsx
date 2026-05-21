import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Landing from './pages/Landing'; // 👈 1. Import your new Landing page
import Register from './pages/Register';
import Login from './pages/Login';

// 1. Citizen Destination Screen
const DashboardPlaceholder = () => (
  <div style={{ padding: '50px', textAlign: 'center', fontFamily: 'sans-serif' }}>
    <h2 style={{ color: '#28a745' }}>🌱 Welcome to the Citizen Dashboard! 🌱</h2>
    <p>You have logged in successfully. Here you can track your carbon footprint and eco-logs.</p>
  </div>
);

// 2. Admin/Superuser Control Room Destination Screen
const AdminDashboardPlaceholder = () => (
  <div style={{ padding: '50px', textAlign: 'center', fontFamily: 'sans-serif' }}>
    <h1 style={{ color: '#007bff' }}>🛠️ EcoTrace Admin Control Center 🛠️</h1>
    <p style={{ fontWeight: 'bold' }}>Privileged Access Level Verified.</p>
    <p>From here you can manage global logistics, approve platform requests, and view system audits.</p>
  </div>
);

// Add a quick placeholder for the Driver view inside App.jsx
const DriverDashboardPlaceholder = () => (
  <div style={{ padding: '50px', textAlign: 'center', fontFamily: 'sans-serif' }}>
    <h2 style={{ color: '#ffc107' }}>🚛 Welcome to the Driver Logistics Dashboard! 🚛</h2>
    <p>Route assignments, pick-up schedules, and optimization metrics will load here.</p>
  </div>
);

// Inside your App() function Routes wrapper, make sure this route is listed:
<Route path="/driver-dashboard" element={<DriverDashboardPlaceholder />} />

function App() {
  return (
    <Router>
      <Routes>
        {/* 2. Replace the Navigate redirect with the Landing component */}
        <Route path="/" element={<Landing />} />
        
        {/* Identity & Authentication Routing */}
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />

        {/* Multi-tier Role Target Screens */}
        <Route path="/dashboard" element={<DashboardPlaceholder />} />
        <Route path="/admin-dashboard" element={<AdminDashboardPlaceholder />} />
        <Route path="/driver-dashboard" element={<DriverDashboardPlaceholder />} />
      </Routes>
    </Router>
  );
}

export default App;
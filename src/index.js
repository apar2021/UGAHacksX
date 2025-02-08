import React from 'react';
import ReactDOM from 'react-dom/client'; // Updated import
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Create a root and render the app
const root = ReactDOM.createRoot(document.getElementById('root')); // Create root
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Optional: Web Vitals reporting
reportWebVitals();

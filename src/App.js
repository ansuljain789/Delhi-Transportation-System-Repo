import React from 'react';
import './App.css';
import './Responsive.css';
import Sidebar from './components/sidebar';
import Dashboard from './components/dashboard';

const App = () => {
  return (
    <div className="container">
      <Sidebar />
      <Dashboard />
    </div>
  );
};

export default App;

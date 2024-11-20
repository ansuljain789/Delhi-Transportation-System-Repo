import React, { useState } from 'react';

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(false); // State to toggle sidebar

  const toggleSidebar = () => {
    setIsOpen(!isOpen);
  };

  return (
    <>
      {/* Hamburger Icon */}
      <button className="hamburger" onClick={toggleSidebar}>
        <span className="line"></span>
        <span className="line"></span>
        <span className="line"></span>
      </button>

      {/* Sidebar */}
      <aside className={`sidebar ${isOpen ? 'open' : ''}`}>
    
        <ul className="menu">
          <a href="#!"><li>Dashboard</li></a>
          <a href="#!"><li>Link Duty Scheduling</li></a>
          <a href="#!"><li>Unlink Duty Scheduling</li></a>
          <a href="#!"><li>Route Management</li></a>
          <a href="#!"><li>Fuel Efficiency</li></a>
          <a href="#!"><li>Emergency Response</li></a>
          <a href="#!"><li>Reports</li></a>
        </ul>

      </aside>
    </>
  );
};

export default Sidebar;

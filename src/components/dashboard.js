import React from 'react';

const data = [
  { busNumber: '101', route: 'Route A', crewId: '5678', crewName: 'Hemant Khora', status: 'Active', maintenance: 'Scheduled', fuelEfficiency: '8.5 MPG' },
  { busNumber: '102', route: 'Route B', crewId: '5689', crewName: 'Ansul Jain', status: 'Inactive', maintenance: 'Completed', fuelEfficiency: '9.1 MPG' },
  { busNumber: '103', route: 'Route C', crewId: '5690', crewName: 'Subhajit Sahu', status: 'Active', maintenance: 'Pending', fuelEfficiency: '7.8 MPG' },
  { busNumber: '104', route: 'Route D', crewId: '5691', crewName: 'Akshat Jain', status: 'Inactive', maintenance: 'Completed', fuelEfficiency: '8.3 MPG' },
];

const Dashboard = () => {
  return (
    <main className="main-content">
      <h1>DTC BUS MANAGEMENT DASHBOARD</h1>
      <table className="data-table">
        <thead>
          <tr>
            <th>Bus Number</th>
            <th>Route</th>
            <th>Crew ID</th>
            <th>Crew Name</th>
            <th>Status</th>
            <th>Maintenance</th>
            <th>Fuel Efficiency</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.busNumber}</td>
              <td>{item.route}</td>
              <td>{item.crewId}</td>
              <td>{item.crewName}</td>
              <td>{item.status}</td>
              <td>{item.maintenance}</td>
              <td>{item.fuelEfficiency}</td>
              <td><button className="action-btn">Details</button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
};

export default Dashboard;

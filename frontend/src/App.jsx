import { useEffect, useState } from 'react';
import api from './api/axios';

function App() {
  const [doctors, setDoctors] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    // Try to fetch the doctors list we created earlier
    api.get('doctors/')
      .then(response => {
        console.log("Data fetched:", response.data);
        setDoctors(response.data);
      })
      .catch(err => {
        console.error("Error:", err);
        setError('Failed to connect to Backend');
      });
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>System Status Check</h1>
      {error && <h3 style={{ color: 'red' }}>{error}</h3>}
      
      {!error && (
        <div>
          <h3 style={{ color: 'green' }}>Backend Connection: SUCCESS</h3>
          <p>Doctors found: {doctors.length}</p>
        </div>
      )}
    </div>
  );
}

export default App;
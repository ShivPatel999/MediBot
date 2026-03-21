import React from 'react';
import ChatWindow from './components/ChatWindow';

function App() {
  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #1a365d 0%, #2b6cb0 100%)',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '20px'
    }}>
      <h1 style={{ color: 'white', marginBottom: '24px', fontFamily: 'sans-serif', fontSize: '28px', letterSpacing: '1px' }}>
        🩺 Medibot
      </h1>
      <p style={{ color: 'rgba(255,255,255,0.75)', marginBottom: '24px', marginTop: '-16px', fontSize: '14px' }}>
        OTC Medication & Symptom Guidance Assistant
      </p>
      <ChatWindow />
    </div>
  );
}

export default App;
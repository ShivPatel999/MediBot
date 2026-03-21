import React from 'react';
import ChatWindow from './components/ChatWindow';

function App() {
  return (
    <div style={{ backgroundColor: '#f4f7f6', minHeight: '100vh', padding: '20px' }}>
      <h1 style={{ textAlign: 'center', color: '#2c3e50', fontFamily: 'sans-serif' }}>Medibot Triage Assistant</h1>
      <ChatWindow />
    </div>
  );
}

export default App;
import React, { useState } from 'react';
import { chatWithMedibot } from '../services/api';

export default function ChatWindow() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;
    
    const userMsg = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    try {
      const data = await chatWithMedibot(userMsg.content);
      setMessages(prev => [...prev, { role: 'bot', data: data }]);
    } catch (error) {
      setMessages(prev => [...prev, { role: 'bot', data: { is_emergency: true, emergency_message: "Error connecting to server." } }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', backgroundColor: 'white', borderRadius: '8px', padding: '20px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', fontFamily: 'sans-serif' }}>
      <div style={{ height: '400px', overflowY: 'auto', marginBottom: '20px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {messages.map((msg, idx) => (
          <div key={idx} style={{ padding: '10px', borderRadius: '8px', alignSelf: msg.role === 'user' ? 'flex-end' : 'flex-start', backgroundColor: msg.role === 'user' ? '#3498db' : '#ecf0f1', color: msg.role === 'user' ? 'white' : 'black', maxWidth: '80%' }}>
            {msg.role === 'user' && <p style={{margin: 0}}>{msg.content}</p>}
            {msg.role === 'bot' && msg.data.is_emergency && <strong style={{color: 'red'}}>{msg.data.emergency_message}</strong>}
            {msg.role === 'bot' && !msg.data.is_emergency && msg.data.analysis && (
              <div>
                <h4 style={{margin: '0 0 5px 0'}}>🔍 Analysis</h4>
                <p style={{margin: '0', fontSize: '14px'}}>Symptom: {msg.data.analysis.symptom} | Severity: {msg.data.analysis.severity}</p>
                <hr style={{margin: '10px 0'}} />
                <h4 style={{margin: '0 0 5px 0'}}>📋 Triage</h4>
                <p style={{margin: '0', fontSize: '14px'}}>Urgency: {msg.data.triage.urgency_level}</p>
                <p style={{margin: '0', fontSize: '14px', color: 'red'}}>⚠️ See doctor if: {msg.data.triage.when_to_see_doctor}</p>
              </div>
            )}
          </div>
        ))}
        {loading && <div style={{color: 'gray'}}>Medibot is analyzing...</div>}
      </div>
      <div style={{ display: 'flex', gap: '10px' }}>
        <input type="text" value={input} onChange={(e) => setInput(e.target.value)} onKeyPress={(e) => e.key === 'Enter' && handleSend()} placeholder="Describe symptoms..." style={{ flex: 1, padding: '10px', borderRadius: '4px', border: '1px solid #ccc' }} />
        <button onClick={handleSend} style={{ padding: '10px 20px', backgroundColor: '#2c3e50', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>Send</button>
      </div>
    </div>
  );
}
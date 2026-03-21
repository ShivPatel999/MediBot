import React, { useState, useRef, useEffect } from 'react';

const ChatWindow = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([
    {
      role: 'bot',
      is_medical: false,
      chat_message: "👋 Hi! I'm Medibot, your medical information assistant. Tell me what symptoms you're experiencing and I'll suggest OTC options and general guidance. Note: I am an AI, not a doctor."
    }
  ]);
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userMessage = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setLoading(true);
    const currentInput = input;
    setInput('');

    try {
      const response = await fetch('http://localhost:8000/api/chat/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: currentInput }),
      });

      if (!response.ok) throw new Error(`Server error: ${response.status}`);
      const data = await response.json();
      setMessages(prev => [...prev, { role: 'bot', ...data }]);
    } catch (error) {
      setMessages(prev => [...prev, {
        role: 'bot',
        is_medical: false,
        chat_message: "⚠️ Error connecting to the server. Please make sure the backend is running."
      }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      width: '100%', maxWidth: '640px', background: 'white',
      borderRadius: '16px', boxShadow: '0 8px 30px rgba(0,0,0,0.12)',
      overflow: 'hidden', fontFamily: "'Segoe UI', sans-serif"
    }}>
      {/* Header */}
      <div style={{ background: '#1a365d', padding: '18px 20px', color: 'white' }}>
        <h2 style={{ margin: 0, fontSize: '18px' }}>🩺 Medibot</h2>
        <p style={{ margin: '4px 0 0', fontSize: '12px', opacity: 0.75 }}>OTC Medication & Symptom Guidance</p>
      </div>

      {/* Messages */}
      <div style={{ height: '480px', overflowY: 'auto', padding: '20px', display: 'flex', flexDirection: 'column', gap: '16px', background: '#f7fafc' }}>
        {messages.map((msg, i) => (
          <div key={i} style={{ alignSelf: msg.role === 'user' ? 'flex-end' : 'flex-start', maxWidth: '88%' }}>
            {msg.role === 'user' ? (
              <div style={{
                background: '#2b6cb0', color: 'white', padding: '10px 16px',
                borderRadius: '18px 18px 4px 18px', fontSize: '14px', lineHeight: '1.5'
              }}>
                {msg.content}
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {/* Chat bubble */}
                <div style={{
                  background: 'white', color: '#2d3748', padding: '12px 16px',
                  borderRadius: '4px 18px 18px 18px', fontSize: '14px', lineHeight: '1.6',
                  boxShadow: '0 1px 3px rgba(0,0,0,0.08)'
                }}>
                  {msg.chat_message}
                </div>

                {/* Medical card */}
                {msg.is_medical && (
                  <div style={{
                    background: 'white', border: '1px solid #e2e8f0',
                    borderRadius: '12px', overflow: 'hidden',
                    boxShadow: '0 1px 3px rgba(0,0,0,0.08)'
                  }}>
                    {/* Analysis row */}
                    <div style={{ background: '#ebf8ff', padding: '12px 16px', borderBottom: '1px solid #bee3f8' }}>
                      <div style={{ fontSize: '12px', fontWeight: 700, color: '#2b6cb0', marginBottom: '4px' }}>🔍 ANALYSIS</div>
                      <div style={{ fontSize: '13px', color: '#2d3748' }}>
                        <strong>Symptom:</strong> {msg.symptom || 'Detected'} &nbsp;|&nbsp;
                        <strong>Severity:</strong> {msg.severity || 'Not specified'}
                      </div>
                    </div>

                    {/* Triage row */}
                    {msg.urgency && (
                      <div style={{ background: '#fffaf0', padding: '10px 16px', borderBottom: '1px solid #feebc8' }}>
                        <div style={{ fontSize: '12px', fontWeight: 700, color: '#c05621', marginBottom: '2px' }}>📋 TRIAGE</div>
                        <div style={{ fontSize: '13px', color: '#2d3748' }}>Urgency: <strong>{msg.urgency}</strong></div>
                      </div>
                    )}

                    {/* Medications */}
                    {msg.medications?.length > 0 && (
                      <div style={{ padding: '12px 16px', borderBottom: msg.warning_signs ? '1px solid #e2e8f0' : 'none' }}>
                        <div style={{ fontSize: '12px', fontWeight: 700, color: '#276749', marginBottom: '8px' }}>💊 OTC OPTIONS</div>
                        {msg.medications.map((med, idx) => (
                          <div key={idx} style={{
                            background: '#f0fff4', border: '1px solid #c6f6d5',
                            borderRadius: '8px', padding: '10px 12px', marginBottom: '8px'
                          }}>
                            <div style={{ fontSize: '13px', fontWeight: 700, color: '#22543d' }}>{med.name}</div>
                            <div style={{ fontSize: '12px', color: '#2d3748', marginTop: '3px' }}>
                              <strong>Used for:</strong> {med.purpose}
                            </div>
                            <div style={{ fontSize: '12px', color: '#4a5568', marginTop: '2px' }}>
                              <strong>How to use:</strong> {med.how_to_use}
                            </div>
                          </div>
                        ))}
                      </div>
                    )}

                    {/* Warning */}
                    {msg.warning_signs && (
                      <div style={{ background: '#fff5f5', padding: '10px 16px' }}>
                        <div style={{ fontSize: '12px', color: '#c53030' }}>
                          ⚠️ <strong>When to see a doctor:</strong> {msg.warning_signs}
                        </div>
                      </div>
                    )}
                  </div>
                )}
              </div>
            )}
          </div>
        ))}

        {loading && (
          <div style={{ alignSelf: 'flex-start' }}>
            <div style={{
              background: 'white', color: '#718096', padding: '10px 16px',
              borderRadius: '4px 18px 18px 18px', fontSize: '13px',
              boxShadow: '0 1px 3px rgba(0,0,0,0.08)'
            }}>
              Medibot is thinking...
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div style={{ padding: '16px 20px', borderTop: '1px solid #e2e8f0', background: 'white', display: 'flex', gap: '10px' }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Describe your symptoms... (e.g. 'I have a headache')"
          disabled={loading}
          style={{
            flex: 1, padding: '10px 16px', borderRadius: '24px',
            border: '1px solid #cbd5e0', outline: 'none', fontSize: '14px',
            background: loading ? '#f7fafc' : 'white'
          }}
        />
        <button
          onClick={sendMessage}
          disabled={loading}
          style={{
            padding: '10px 20px', background: loading ? '#a0aec0' : '#1a365d',
            color: 'white', border: 'none', borderRadius: '24px',
            cursor: loading ? 'not-allowed' : 'pointer', fontWeight: 600, fontSize: '14px'
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatWindow;
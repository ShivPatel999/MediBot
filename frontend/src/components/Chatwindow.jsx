import React, { useState, useRef, useEffect } from 'react';

const ChatWindow = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([
    {
      role: 'bot',
      is_medical: false,
      chat_message: "👋 Hi! I'm Medibot, your medical information assistant. I remember our conversation, so feel free to ask follow-up questions! Tell me what symptoms you're experiencing and I'll suggest OTC options and general guidance. Note: I am an AI, not a doctor."
    }
  ]);
  // Separate state to track conversation history sent to backend
  const [conversationHistory, setConversationHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, loading]);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userText = input;
    const userMessage = { role: 'user', content: userText };

    // Add user message to display
    setMessages(prev => [...prev, { role: 'user', content: userText }]);
    setLoading(true);
    setInput('');

    try {
      const response = await fetch('http://localhost:8000/api/chat/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: userText,
          history: conversationHistory  // Send full history to backend
        }),
      });

      if (!response.ok) throw new Error(`Server error: ${response.status}`);
      const data = await response.json();

      // Add bot response to display
      setMessages(prev => [...prev, { role: 'bot', ...data }]);

      // Update conversation history for next request
      // Store user message + bot's text response for context
      setConversationHistory(prev => [
        ...prev,
        { role: 'user', content: userText },
        { role: 'assistant', content: data.chat_message }
      ]);

    } catch (error) {
      setMessages(prev => [...prev, {
        role: 'bot',
        is_medical: false,
        chat_message: "Error connecting to the server. Please make sure the backend is running."
      }]);
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    setMessages([{
      role: 'bot',
      is_medical: false,
      chat_message: "👋 Chat cleared! I'm ready to help. Tell me what symptoms you're experiencing. Note: I am an AI, not a doctor."
    }]);
    setConversationHistory([]);
  };

  return (
    <div style={{
      width: '100%', maxWidth: '640px', background: 'white',
      borderRadius: '16px', boxShadow: '0 8px 30px rgba(0,0,0,0.12)',
      overflow: 'hidden', fontFamily: "'Segoe UI', sans-serif"
    }}>
      {/* Header */}
      <div style={{ background: '#1a365d', padding: '16px 20px', color: 'white', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h2 style={{ margin: 0, fontSize: '18px' }}>🩺 Medibot</h2>
          <p style={{ margin: '4px 0 0', fontSize: '12px', opacity: 0.75 }}>OTC Medication & Symptom Guidance</p>
        </div>
        <button
          onClick={clearChat}
          style={{ background: 'rgba(255,255,255,0.15)', border: '1px solid rgba(255,255,255,0.3)', color: 'white', padding: '6px 12px', borderRadius: '8px', cursor: 'pointer', fontSize: '12px' }}
        >
          Clear Chat
        </button>
      </div>

      {/* Messages */}
      <div style={{ height: '500px', overflowY: 'auto', padding: '20px', display: 'flex', flexDirection: 'column', gap: '16px', background: '#f7fafc' }}>
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
                {msg.is_medical && (msg.symptom || msg.urgency || (msg.medications && msg.medications.length > 0)) && (
                  <div style={{
                    background: 'white', border: '1px solid #e2e8f0',
                    borderRadius: '12px', overflow: 'hidden',
                    boxShadow: '0 1px 3px rgba(0,0,0,0.08)'
                  }}>
                    {/* Analysis */}
                    {msg.symptom && (
                      <div style={{ background: '#ebf8ff', padding: '10px 16px', borderBottom: '1px solid #bee3f8' }}>
                        <div style={{ fontSize: '11px', fontWeight: 700, color: '#2b6cb0', marginBottom: '3px' }}>🔍 ANALYSIS</div>
                        <div style={{ fontSize: '13px', color: '#2d3748' }}>
                          <strong>Symptom:</strong> {msg.symptom}
                          {msg.severity && <> &nbsp;|&nbsp; <strong>Severity:</strong> {msg.severity}</>}
                        </div>
                      </div>
                    )}

                    {/* Triage */}
                    {msg.urgency && (
                      <div style={{ background: '#fffaf0', padding: '10px 16px', borderBottom: '1px solid #feebc8' }}>
                        <div style={{ fontSize: '11px', fontWeight: 700, color: '#c05621', marginBottom: '3px' }}>📋 TRIAGE</div>
                        <div style={{ fontSize: '13px', color: '#2d3748' }}>Urgency: <strong>{msg.urgency}</strong></div>
                      </div>
                    )}

                    {/* Medications */}
                    {msg.medications && msg.medications.length > 0 && (
                      <div style={{ padding: '12px 16px', borderBottom: msg.warning_signs ? '1px solid #e2e8f0' : 'none' }}>
                        <div style={{ fontSize: '11px', fontWeight: 700, color: '#276749', marginBottom: '8px' }}>💊 OTC OPTIONS</div>
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
          placeholder="Ask a follow-up or describe symptoms..."
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
            padding: '10px 20px',
            background: loading ? '#a0aec0' : '#1a365d',
            color: 'white', border: 'none', borderRadius: '24px',
            cursor: loading ? 'not-allowed' : 'pointer',
            fontWeight: 600, fontSize: '14px'
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatWindow;
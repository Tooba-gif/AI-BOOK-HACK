import React, { useState, useRef, useEffect } from 'react';
import { useAuth } from '../hooks/useAuth';

const ChatBot = ({ chapterId = null }) => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const { user, isAuthenticated } = useAuth();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || !isAuthenticated) return;

    // Add user message to the chat
    const userMessage = { type: 'user', content: inputValue, timestamp: new Date() };
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Call the backend API to get the AI response
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${user.token}`,
        },
        body: JSON.stringify({
          question: inputValue,
          chapter_id: chapterId
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      // Add AI response to the chat
      const aiMessage = {
        type: 'ai',
        content: data.answer,
        sources: data.sources,
        timestamp: new Date()
      };
      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error getting chat response:', error);
      const errorMessage = {
        type: 'ai',
        content: 'Sorry, I encountered an error. Please try again.',
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const renderSources = (sources) => {
    if (!sources || sources.length === 0) return null;

    return (
      <div className="chat-sources">
        <h4>Sources:</h4>
        <ul>
          {sources.map((source, index) => (
            <li key={index}>
              <a href={`/chapters/${source.chapter_id}`}>{source.section_title}</a>
            </li>
          ))}
        </ul>
      </div>
    );
  };

  return (
    <div className="chatbot-container">
      <div className="chat-messages">
        {messages.length === 0 ? (
          <div className="chat-welcome">
            <p>Hello! I'm your AI assistant for the Physical AI & Humanoid Robotics textbook. Ask me any questions about the content.</p>
          </div>
        ) : (
          messages.map((message, index) => (
            <div key={index} className={`chat-message ${message.type}`}>
              <div className="message-content">
                {message.type === 'ai' && (
                  <div className="ai-indicator">AI Assistant</div>
                )}
                <div className="message-text">{message.content}</div>
                {message.sources && renderSources(message.sources)}
              </div>
            </div>
          ))
        )}
        {isLoading && (
          <div className="chat-message ai">
            <div className="message-content">
              <div className="ai-indicator">AI Assistant</div>
              <div className="message-text typing-indicator">Thinking...</div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className="chat-input-form">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Ask a question about the textbook..."
          disabled={!isAuthenticated || isLoading}
        />
        <button type="submit" disabled={!isAuthenticated || isLoading || !inputValue.trim()}>
          Send
        </button>
      </form>

      {!isAuthenticated && (
        <div className="chat-auth-notice">
          Please log in to ask questions to the AI assistant.
        </div>
      )}
    </div>
  );
};

export default ChatBot;
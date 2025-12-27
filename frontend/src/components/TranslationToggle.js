import React, { useState } from 'react';
import { useAuth } from '../hooks/useAuth';
import chapterService from '../services/chapterService';

const TranslationToggle = ({ chapterId, onContentChange }) => {
  const [currentLanguage, setCurrentLanguage] = useState('en'); // Default to English
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const { user, isAuthenticated } = useAuth();

  const toggleLanguage = async () => {
    if (loading) return; // Prevent multiple simultaneous requests

    setLoading(true);
    setError(null);

    try {
      if (currentLanguage === 'en') {
        // Switch to Urdu
        if (!chapterId) {
          throw new Error('Chapter ID is required for translation');
        }

        // Call the backend API to get Urdu translation
        const data = await chapterService.getChapterInUrduById(chapterId, user.token);
        onContentChange(data.content);
        setCurrentLanguage('ur');
      } else {
        // Switch back to English
        // Fetch the original English content
        if (!chapterId) {
          throw new Error('Chapter ID is required for translation');
        }

        const data = await chapterService.getChapterById(chapterId, user.token);
        onContentChange(data.content);
        setCurrentLanguage('en');
      }
    } catch (err) {
      setError(err.message);
      console.error('Error toggling language:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="translation-toggle">
      <button
        onClick={toggleLanguage}
        disabled={loading}
        className={`language-toggle-btn ${currentLanguage}`}
      >
        {loading ? 'Loading...' : currentLanguage === 'en' ? 'اردو میں تبدیل کریں' : 'Switch to English'}
      </button>

      {error && (
        <div className="translation-error">
          Error: {error}
        </div>
      )}
    </div>
  );
};

export default TranslationToggle;
import React, { useState, useEffect } from 'react';
import { useAuth } from '../hooks/useAuth';
import ChatBot from './ChatBot';
import InteractiveElements from './InteractiveElements';
import TranslationToggle from './TranslationToggle';

const ChapterPage = ({ chapterData }) => {
  const { user, isAuthenticated } = useAuth();
  const [chapter, setChapter] = useState(chapterData || null);
  const [progress, setProgress] = useState({ progress_percentage: 0, completed: false });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [displayedContent, setDisplayedContent] = useState('');

  useEffect(() => {
    if (chapterData) {
      setChapter(chapterData);
      setDisplayedContent(chapterData.chapter.content); // Set the initial content to display
    }
  }, [chapterData]);

  useEffect(() => {
    const fetchProgress = async () => {
      if (isAuthenticated && user && chapter?.chapter?.id) {
        try {
          const response = await fetch(`/api/progress`, {
            headers: {
              'Authorization': `Bearer ${user.token}`,
            },
          });
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          const data = await response.json();

          // Find progress for current chapter
          const chapterProgress = data.progress.find(p => p.chapter_id === chapter.chapter.id);
          if (chapterProgress) {
            setProgress({
              progress_percentage: chapterProgress.progress_percentage,
              completed: chapterProgress.completed
            });
          }
        } catch (err) {
          console.error('Error fetching progress:', err);
        }
      }
    };

    fetchProgress();
  }, [isAuthenticated, user, chapter?.chapter?.id]);

  // Update displayed content when chapter changes
  useEffect(() => {
    if (chapter && chapter.chapter) {
      setDisplayedContent(chapter.chapter.content);
    }
  }, [chapter]);

  const handleContentChange = (newContent) => {
    setDisplayedContent(newContent);
  };

  if (!chapter) return <div>Chapter not found</div>;

  const handleProgressUpdate = async (newProgress) => {
    if (isAuthenticated && user && chapter?.chapter?.id) {
      try {
        const response = await fetch(`/api/progress/${chapter.chapter.id}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${user.token}`,
          },
          body: JSON.stringify({ progress_percentage: newProgress }),
        });

        if (response.ok) {
          const data = await response.json();
          setProgress({
            progress_percentage: data.progress_percentage,
            completed: data.completed
          });
        }
      } catch (err) {
        console.error('Error updating progress:', err);
      }
    }
  };

  // Function to track reading progress
  const trackReadingProgress = () => {
    const scrollPercentage = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
    const newProgress = Math.min(100, Math.max(progress.progress_percentage, Math.round(scrollPercentage)));

    if (newProgress > progress.progress_percentage) {
      handleProgressUpdate(newProgress);
    }
  };

  useEffect(() => {
    window.addEventListener('scroll', trackReadingProgress);
    return () => {
      window.removeEventListener('scroll', trackReadingProgress);
    };
  }, [progress.progress_percentage]);

  return (
    <div className="chapter-page">
      <header className="chapter-header">
        <h1>{chapter.chapter.title}</h1>
        <div className="progress-bar">
          <div
            className="progress-fill"
            style={{ width: `${progress.progress_percentage}%` }}
          ></div>
          <span className="progress-text">{progress.progress_percentage}% complete</span>
        </div>
        <TranslationToggle
          chapterId={chapter.chapter.id}
          onContentChange={handleContentChange}
        />
      </header>

      <main className="chapter-content">
        <div
          className="markdown-content"
          dangerouslySetInnerHTML={{ __html: displayedContent }}
        />

        <InteractiveElements elements={chapter.chapter.interactive_elements} />
      </main>

      <section className="chapter-chatbot">
        <h3>Ask the AI Assistant</h3>
        <ChatBot chapterId={chapter.chapter.id} />
      </section>

      <footer className="chapter-footer">
        <button
          className="btn btn-primary"
          onClick={() => handleProgressUpdate(progress.progress_percentage + 10)}
        >
          Mark 10% More
        </button>
        <button
          className="btn btn-secondary"
          onClick={() => handleProgressUpdate(100)}
        >
          Mark Complete
        </button>
      </footer>
    </div>
  );
};

export default ChapterPage;
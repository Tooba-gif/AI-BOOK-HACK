import React, { useState, useEffect } from 'react';
import Layout from '@theme/Layout';
import { useParams } from 'react-router-dom';
import ChapterPage from '../components/ChapterPage';

// This page is for individual chapter viewing
// It will fetch the chapter content from the backend API
const ChapterPageWrapper = () => {
  const [chapter, setChapter] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  // Using URL parameters instead of React Router for Docusaurus
  const pathParts = typeof window !== 'undefined' ? window.location.pathname.split('/') : [];
  const slug = pathParts[pathParts.length - 1] || 'introduction-to-physical-ai';

  useEffect(() => {
    const fetchChapter = async () => {
      try {
        const response = await fetch(`/api/chapters/${slug}`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setChapter(data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    if (typeof window !== 'undefined') {
      fetchChapter();
    }
  }, [slug]);

  if (loading) {
    return (
      <Layout title="Loading Chapter..." description="Loading textbook content...">
        <div className="container margin-vert--xl">
          <div className="row">
            <div className="col col--8 col--offset-2">
              <h1>Loading...</h1>
            </div>
          </div>
        </div>
      </Layout>
    );
  }

  if (error) {
    return (
      <Layout title="Error" description="Error loading textbook content">
        <div className="container margin-vert--xl">
          <div className="row">
            <div className="col col--8 col--offset-2">
              <h1>Error loading chapter</h1>
              <p>{error}</p>
            </div>
          </div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout title={chapter?.chapter?.title || "Chapter"} description="AI-powered interactive textbook">
      <div className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset-2">
            {chapter && <ChapterPage chapterData={chapter} />}
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default ChapterPageWrapper;
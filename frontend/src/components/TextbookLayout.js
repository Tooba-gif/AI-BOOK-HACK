import React from 'react';
import { Outlet } from 'react-router-dom';

const TextbookLayout = () => {
  return (
    <div className="textbook-layout">
      <header className="textbook-header">
        <h1>AI Native Textbook</h1>
        <nav className="textbook-nav">
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/chapters">Chapters</a></li>
            <li><a href="/dashboard">Dashboard</a></li>
          </ul>
        </nav>
      </header>

      <main className="textbook-main">
        <Outlet />
      </main>

      <footer className="textbook-footer">
        <p>AI Native Textbook for Physical AI & Humanoid Robotics</p>
      </footer>
    </div>
  );
};

export default TextbookLayout;
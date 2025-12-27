import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Interactive Learning',
    description: (
      <>
        Engage with interactive elements throughout the textbook to enhance your learning experience in Physical AI & Humanoid Robotics.
      </>
    ),
  },
  {
    title: 'AI-Powered Assistance',
    description: (
      <>
        Get instant answers to your questions with our AI-powered chatbot that understands the textbook content.
      </>
    ),
  },
  {
    title: 'Personalized Content',
    description: (
      <>
        Content adapts to your background and learning preferences for an optimized educational experience.
      </>
    ),
  },
];

function Feature({title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
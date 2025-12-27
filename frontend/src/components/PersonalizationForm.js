import React, { useState, useEffect } from 'react';
import { useAuth } from '../hooks/useAuth';
import userService from '../services/userService';

const PersonalizationForm = () => {
  const { user, isAuthenticated } = useAuth();
  const [background, setBackground] = useState({
    experience_level: 'intermediate',
    field_of_interest: 'general',
    learning_style: 'balanced'
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (isAuthenticated && user) {
      fetchUserProfile();
    }
  }, [isAuthenticated, user]);

  const fetchUserProfile = async () => {
    try {
      setLoading(true);
      const profile = await userService.getUserProfile(user.token);
      if (profile.background) {
        setBackground(profile.background);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setBackground(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const updatedProfile = await userService.updateUserProfile(
        background, 
        null, // preferences can be null if we're only updating background
        user.token
      );
      
      alert('Personalization preferences updated successfully!');
    } catch (err) {
      setError(err.message);
      alert(`Error updating preferences: ${err.message}`);
    }
  };

  if (loading) return <div>Loading personalization settings...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="personalization-form">
      <h3>Personalize Your Learning Experience</h3>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="experience_level">Experience Level:</label>
          <select
            id="experience_level"
            name="experience_level"
            value={background.experience_level}
            onChange={handleChange}
          >
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="field_of_interest">Field of Interest:</label>
          <select
            id="field_of_interest"
            name="field_of_interest"
            value={background.field_of_interest}
            onChange={handleChange}
          >
            <option value="general">General</option>
            <option value="robotics">Robotics</option>
            <option value="ai">Artificial Intelligence</option>
            <option value="machine_learning">Machine Learning</option>
            <option value="computer_vision">Computer Vision</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="learning_style">Learning Style:</label>
          <select
            id="learning_style"
            name="learning_style"
            value={background.learning_style}
            onChange={handleChange}
          >
            <option value="balanced">Balanced</option>
            <option value="visual">Visual</option>
            <option value="textual">Textual</option>
            <option value="practical">Practical</option>
          </select>
        </div>

        <button type="submit" className="btn btn-primary">
          Update Preferences
        </button>
      </form>
    </div>
  );
};

export default PersonalizationForm;
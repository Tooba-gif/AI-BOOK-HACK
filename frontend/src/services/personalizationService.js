// API service for personalization operations
class PersonalizationService {
  constructor(baseURL = '/api') {
    this.baseURL = baseURL;
  }

  async getPersonalizedChapter(chapterId, token) {
    try {
      const response = await fetch(`${this.baseURL}/personalization/${chapterId}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error fetching personalized chapter:', error);
      throw error;
    }
  }

  async updatePersonalizationPreferences(preferences, token) {
    try {
      const response = await fetch(`${this.baseURL}/user/profile`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ preferences }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error updating personalization preferences:', error);
      throw error;
    }
  }
}

export default new PersonalizationService();
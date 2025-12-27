// API service for translation operations
class TranslationService {
  constructor(baseURL = '/api') {
    this.baseURL = baseURL;
  }

  async getUrduTranslation(chapterId, token) {
    try {
      const response = await fetch(`${this.baseURL}/translation/${chapterId}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        if (response.status === 422) {
          throw new Error('Urdu translation not available for this chapter');
        }
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error fetching Urdu translation:', error);
      throw error;
    }
  }

  async addUrduTranslation(chapterId, content, token) {
    try {
      const response = await fetch(`${this.baseURL}/translation/${chapterId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ content }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error adding Urdu translation:', error);
      throw error;
    }
  }
}

export default new TranslationService();
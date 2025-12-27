// API service for chapter-related operations
class ChapterService {
  constructor(baseURL = '/api') {
    this.baseURL = baseURL;
  }

  async getAllChapters() {
    try {
      const response = await fetch(`${this.baseURL}/chapters`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error fetching chapters:', error);
      throw error;
    }
  }

  async getChapterBySlug(slug) {
    try {
      const response = await fetch(`${this.baseURL}/chapters/${slug}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error(`Error fetching chapter ${slug}:`, error);
      throw error;
    }
  }

  async getChapterById(id, token) {
    try {
      const response = await fetch(`${this.baseURL}/chapters/${id}`, {
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
      console.error(`Error fetching chapter ${id}:`, error);
      throw error;
    }
  }

  async getChapterInUrdu(slug) {
    try {
      const response = await fetch(`${this.baseURL}/chapters/${slug}/urdu`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        if (response.status === 422) {
          throw new Error('Urdu translation not available');
        }
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error(`Error fetching Urdu chapter ${slug}:`, error);
      throw error;
    }
  }

  async getChapterInUrduById(id, token) {
    try {
      const response = await fetch(`${this.baseURL}/chapters/${id}/urdu`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        if (response.status === 422) {
          throw new Error('Urdu translation not available');
        }
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error(`Error fetching Urdu chapter ${id}:`, error);
      throw error;
    }
  }

  async getUserProgress(token) {
    try {
      const response = await fetch(`${this.baseURL}/progress`, {
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
      console.error('Error fetching user progress:', error);
      throw error;
    }
  }

  async updateUserProgress(chapterId, progressPercentage, token) {
    try {
      const response = await fetch(`${this.baseURL}/progress/${chapterId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ progress_percentage: progressPercentage }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error updating user progress:', error);
      throw error;
    }
  }
}

export default new ChapterService();
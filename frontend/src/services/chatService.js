// API service for chat-related operations
class ChatService {
  constructor(baseURL = '/api') {
    this.baseURL = baseURL;
  }

  async askQuestion(question, chapterId = null, token) {
    try {
      const response = await fetch(`${this.baseURL}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({
          question,
          chapter_id: chapterId
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error('Error asking question:', error);
      throw error;
    }
  }
}

export default new ChatService();
// frontend/src/services/authService.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/auth';

const authService = {
  login: async (username, password) => {
    try {
      const response = await axios.post(`${API_URL}/login`, { username, password });
      return response.data; // Return the response data for further processing
    } catch (error) {
      throw new Error(error.response.data.msg || 'Login failed. Please try again.');
    }
  },

  logout: () => {
    localStorage.removeItem('token'); // Remove the token
  },

  register: async (userData) => {
    try {
      const response = await axios.post(`${API_URL}/create_user_account`, userData);
      return response.data; // Return the response data for further processing
    } catch (error) {
      throw new Error(error.response.data.message || 'Registration failed. Please try again.');
    }
  },

  // You can add more API methods here in the future
};

export default authService;
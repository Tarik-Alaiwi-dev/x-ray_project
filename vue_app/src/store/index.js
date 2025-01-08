import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
  },
  mutations: {
    initializeStore(state) {
      const token = localStorage.getItem('token');
      if (token) {
        state.token = token;
        state.isAuthenticated = true;
      } else {
        state.token = '';
        state.isAuthenticated = false;
      }
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
      localStorage.setItem('token', token);  // Store token persistently
    },
    removeToken(state) {
      state.token = '';
      state.isAuthenticated = false;
      localStorage.removeItem('token');  // Remove token from localStorage
    }
  },
  actions: {
    logout({ commit }) {
      commit('removeToken');
    }
  }
});

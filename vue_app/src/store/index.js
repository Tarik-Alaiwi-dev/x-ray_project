import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoading: false,
  },
  getters: {
  },
  mutations: {
    setIsLoading(state, status) {
      state.isLoading = status
    }
  },
  actions: {
  },
  modules: {
  }
})

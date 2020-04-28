import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const keyword = 'Bearer'
const login_url = process.env.VUE_APP_AUTH_BASEURL + process.env.VUE_APP_VERSION + '/users/login'
const register_url = process.env.VUE_APP_USER_BASEURL + process.env.VUE_APP_VERSION + '/users'

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user: {}
  },
  mutations: {
    request(state) {
      state.status = 'loading'
    },

    login(state, payload) {
      state.status = 'success'
      state.token = payload.token
      state.user = payload.user
    },

    error(state) {
      state.status = 'error'
    },

    logout(state) {
      state.status = ''
      state.token = ''
      state.user = {}
    }
  },
  actions: {
    login({ commit }, user_data) {
      return new Promise(
        (resolve, reject) => {
          commit('request')

          axios({ url: login_url, data: user_data, method: 'POST' })
            .then(response => {
              const token = response.data.token
              const user = {
                uuid: response.data.uuid,
                username: response.data.username
              }

              commit('login', { token: token, user: user })
              localStorage.setItem('token', token)
              axios.defaults.headers.common['Authorization'] = keyword + ' ' + token

              resolve(response)
            })
            .catch(error => {
              commit('error')
              localStorage.removeItem('token')
              reject(error)
            })
        }
      )
    },

    register({ commit }, user_data) {
      return new Promise(
        (resolve, reject) => {
          commit('request')

          axios({ url: register_url, data: user_data, method: 'POST' })
            .then(response => {
              const token = response.data.token
              const user = response.data.user

              commit('login', { token: token, user: user })
              localStorage.setItem('token', token)
              axios.defaults.headers.common['Authorization'] = token

              resolve(response)
            })
            .catch(error => {
              commit('error')
              localStorage.removeItem('token')
              reject(error)
            })
        }
      )
    },

    logout({ commit }) {
      return new Promise(
        (resolve /*, reject*/) => {
          commit('logout')
          localStorage.removeItem('token')
          delete axios.defaults.headers.common['Authorization']
          resolve()
        }
      )
    }
  },

  getters: {
    isLoggedIn: state => !!state.token,
    status: state => state.status,
    uuid: state => state.user.uuid,
    username: state => state.user.username
  },

  modules: {
  }
})

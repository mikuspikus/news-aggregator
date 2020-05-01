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
    user: {
      username: localStorage.getItem('username') || '',
      uuid: localStorage.getItem('uuid') || ''
    }
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
    login({ commit }, login_data) {
      return new Promise(
        (resolve, reject) => {
          commit('request')

          axios({ url: login_url, data: login_data.user, method: 'POST' })
            .then(response => {
              const token = response.data.token
              const user = {
                uuid: response.data.uuid,
                username: response.data.username
              }

              commit('login', { token: token, user: user })
              localStorage.setItem('token', token)
              localStorage.setItem('username', user.username)
              localStorage.setItem('uuid', user.uuid)

              const vue = login_data.vue

              vue.$http.auth.defaults.headers.common['Authorization'] = keyword + ' ' + token;
              vue.$http.user.defaults.headers.common['Authorization'] = keyword + ' ' + token;
              vue.$http.comment.defaults.headers.common['Authorization'] = keyword + ' ' + token;
              vue.$http.rssparser.defaults.headers.common['Authorization'] = keyword + ' ' + token;
              vue.$http.news.defaults.headers.common['Authorization'] = keyword + ' ' + token;
              // axios.defaults.headers.common['Authorization'] = keyword + ' ' + token

              resolve(response)
            })
            .catch(error => {
              commit('error')
              localStorage.removeItem('token')
              localStorage.removeItem('username')
              localStorage.removeItem('uuid')
              reject(error)
            })
        }
      )
    },

    register({ commit }, register_data) {
      return new Promise(
        (resolve, reject) => {
          commit('request')

          axios({ url: register_url, data: register_data.user, method: 'POST' })
            .then(response => {
              const token = response.data.token
              const user = response.data.user

              commit('login', { token: token, user: user })
              localStorage.setItem('token', token)
              localStorage.setItem('username', user.username)
              localStorage.setItem('uuid', user.uuid)

              const vue = register_data.vue

              vue.$http.auth.defaults.headers.common['Authorization'] = keyword + ' ' + token;
              vue.$http.user.defaults.headers.common['Authorization'] = keyword + ' ' + token;
              vue.$http.comment.defaults.headers.common['Authorization'] = keyword + ' ' + token;
              vue.$http.rssparser.defaults.headers.common['Authorization'] = keyword + ' ' + token;
              vue.$http.news.defaults.headers.common['Authorization'] = keyword + ' ' + token;
              // axios.defaults.headers.common['Authorization'] = keyword + ' ' + token

              resolve(response)
            })
            .catch(error => {
              commit('error')
              localStorage.removeItem('token')
              localStorage.removeItem('username')
              localStorage.removeItem('uuid')
              reject(error)
            })
        }
      )
    },

    logout({ commit }, logout_data) {
      return new Promise(
        (resolve /*, reject*/) => {
          commit('logout')
          localStorage.removeItem('token')
          localStorage.removeItem('username')
          localStorage.removeItem('uuid')

          const vue = logout_data.vue

          delete vue.$http.auth.defaults.headers.common['Authorization'];
          delete vue.$http.user.defaults.headers.common['Authorization'];
          delete vue.$http.comment.defaults.headers.common['Authorization'];
          delete vue.$http.rssparser.defaults.headers.common['Authorization'];
          delete vue.$http.news.defaults.headers.common['Authorization'];
          // delete axios.defaults.headers.common['Authorization']
          resolve()
        }
      )
    }
  },

  getters: {
    isLoggedIn: state => !!state.token,
    status: state => state.status,
    uuid: state => state.user.uuid,
    username: state => state.user.username,
    token: state => state.token,
  },

  modules: {
  }
})

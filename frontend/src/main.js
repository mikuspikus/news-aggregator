import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import axios from 'axios'

const auth = axios.create({ baseURL: process.env.VUE_APP_AUTH_BASEURL + process.env.VUE_APP_VERSION + '/' });
const user = axios.create({ baseURL: process.env.VUE_APP_USER_BASEURL + process.env.VUE_APP_VERSION + '/' });
const comment = axios.create({ baseURL: process.env.VUE_APP_COMMENT_BASEURL + process.env.VUE_APP_VERSION + '/' });
const rssparser = axios.create({ baseURL: process.env.VUE_APP_RSSPARSER_BASEURL + process.env.VUE_APP_VERSION + '/' });
const news = axios.create({ baseURL: process.env.VUE_APP_NEWS_BASEURL + process.env.VUE_APP_VERSION + '/' });

const keyword = 'Bearer'
const token = localStorage.getItem('token')

if (token) {
  axios.defaults.headers.common['Authorization'] = keyword + ' ' + token;
  auth.defaults.headers.common['Authorization'] = keyword + ' ' + token;
  user.defaults.headers.common['Authorization'] = keyword + ' ' + token;
  comment.defaults.headers.common['Authorization'] = keyword + ' ' + token;
  rssparser.defaults.headers.common['Authorization'] = keyword + ' ' + token;
  news.defaults.headers.common['Authorization'] = keyword + ' ' + token;
}

Vue.prototype.$http = {}
Vue.prototype.$http.auth = auth
Vue.prototype.$http.user = user
Vue.prototype.$http.comment = comment
Vue.prototype.$http.rssparser = rssparser
Vue.prototype.$http.news = news

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

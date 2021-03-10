import Vue from 'vue'
import VueRouter from 'vue-router'

import Index from '../views/Index.vue'
import LoginView from '../views/Login.vue'
import RegisterView from '../views/Register.vue'
import UserView from '../views/User.vue'
import NewsSingleView from '../views/News.vue'
import NotFoundView from '../views/NotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Index
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/users/:uuid',
    name: 'User',
    component: UserView
  },
  {
    path: '/news/:uuid',
    name: 'NewsSingle',
    component: NewsSingleView,
    // meta: {

    // }

  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/404',
    name: 'NotFound',
    component: NotFoundView,
    props: true
  },
]

const router = new VueRouter({
  mode: 'history',
  routes: routes
})

// router.beforeEach((to, matched, next) => {
//   if (to.matched.some(record => record.meta.requiresAuthorization)) {
//     if (store.getters.isLoggedIn) {
//       next()
//       return
//     }
//     next('/login')
//   } else {
//     next()
//   }
// })

export default router

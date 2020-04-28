<template>
  <div id="app">
    <navbar :islogged="isLoggedIn"/>
    <feeds v-if="isLoggedIn"/>

    <router-view/>
  </div>
</template>

<script>
import Navbar from '../src/components/utility/Navbar.vue'
import Feeds from '../src/components/rssfeed/Feeds.vue'

export default {
  components: {Navbar, Feeds},

  computed: {
    isLoggedIn () {
      return this.$store.getters.isLoggedIn;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

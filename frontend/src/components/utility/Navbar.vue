<template>
  <div id="navbar">
    <b-navbar toggleable="lg" type="dark" variant="dark">

      <b-navbar-brand href="#">News for Hackers</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">Home</b-nav-item>
          <b-nav-item v-b-toggle="sidebar_name">Feeds</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item href="#">Sign In</b-nav-item>
          <b-nav-item href="#">Sign Up</b-nav-item>
          <b-nav-item href="#">Sign Out</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
    data () {
      return {
        sidebar_name: 'sidebar-feeds'
      }
    }
}
</script>
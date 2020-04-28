<template>
  <div id="navbar">
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand :to="{ name: 'Home' }">News for Hackers</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="{ name: 'Home'}">Home</b-nav-item>
          <b-nav-item v-if="islogged" v-b-toggle="FeedsSidebarID">Feeds</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <template v-if="islogged">
            <b-nav-item @click="logout">Sign Out</b-nav-item>
          </template>

          <template v-else>
            <b-nav-item :to="{ name: 'Login' }">Sign In</b-nav-item>
            <b-nav-item :to="{ name: 'Register' }">Sign Up</b-nav-item>
          </template>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "Navbar",

  props: {
    islogged: { type: Boolean }
  },

  data() {
    return {
      FeedsSidebarID: "sidebar-feeds"
    };
  },

  methods: {
    logout(event) {
      event.preventDefault();

      this.$store
        .dispatch("logout")
        .then(() => {
          this.$router
            .push({ name: "Home" })
            // pushing to the same route raises error
            // silencing it here
            .catch(() => {});
        })
        .catch(error => {
          this.$bvToast.toast(error, {
            title: "Error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    }
  }
};
</script>
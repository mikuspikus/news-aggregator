<template>
  <div id="login">
    <b-container fluid>
      <b-row class="pt-3" />

      <template v-if="loading">
        <b-spinner variant="dark" />
      </template>

      <template v-else-if="ok">
        <b-row class="text-left">
          <b-col cols="4"></b-col>
          <b-col class="pt-5 pb-5">
            <user-form :uuid="uuid" :username="user.username" :email="user.email" />
          </b-col>
          <b-col cols="4"></b-col>
        </b-row>
      </template>

      <template v-else>
        <b-row class="text-left">
          <b-col />
          <b-col cols="8" class="pt-5 pb-5">
            <b-jumbotron
              bg-variant="dark"
              text-variant="white"
              border-variant="dark"
              class="m-0"
              header
            >
              <template v-slot:header>Error occuried</template>
              <template v-slot:lead>User service is probably unavailible</template>
            </b-jumbotron>
          </b-col>
          <b-col />
        </b-row>
      </template>
    </b-container>
  </div>
</template>

<script>
import UserForm from "../components/user/UserForm.vue";
import ehandler from "../utility/errorhandler.js";

export default {
  name: "user-view",

  data() {
    return {
      loading: true,
      ok: true,
      uuid: this.$route.params.uuid,
      user: {}
    };
  },

  created() {
    this.fetchUserData();
  },

  methods: {
    fetchUserData() {
      this.$http.user({ url: `users/${this.uuid}`, method: "GET" })
        .then(response => {
          this.loading = false;
          this.user = response.data;
        })
        .catch(error => {
          this.loading = false;
          this.ok = false;
          ehandler.error(
            this,
            error,
            "User tetching Error",
            `user (UUID: ${this.uuid} not found`
          );
          // this.$bvToast.toast(error.message, {
          //   title: "Error",
          //   autoHideDelay: 5000,
          //   toaster: "b-toaster-bottom-center"
          // });
        });
    }
  },

  components: {
    UserForm
  }
};
</script>
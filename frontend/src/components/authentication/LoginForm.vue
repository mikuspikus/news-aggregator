<template>
  <div id="login-from">
    <b-card
      border-variant="dark"
      header="Sign in"
      header-text-variant="white"
      header-tag="header"
      header-bg-variant="dark"
      header-class="text-center"
    >
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="input-group-usernmae" label="Username:" label-for="input-username">
          <b-form-input
            id="input-usernmae"
            v-model="form.username"
            type="text"
            required
            placeholder="Enter username"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-pwd" label="Password:" label-for="input-pwd">
          <b-form-input
            id="input-pwd"
            v-model="form.pwd"
            required
            type="password"
            placeholder="Enter password"
          ></b-form-input>
        </b-form-group>

        <b-button class="mr-1" type="submit" variant="outline-dark">Sign in</b-button>
        <b-button class="ml-1" type="reset" variant="dark">Reset</b-button>
      </b-form>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "LoginForm",

  data() {
    return {
      show: true,
      form: {
        username: "",
        pwd: ""
      }
    };
  },

  methods: {
    onSubmit(event) {
      event.preventDefault();

      let username = this.form.username;
      let password = this.form.pwd;
      this.$store
        .dispatch("login", { username, password })
        .then(() => this.$router.push("/"))
        .catch(error => {
          this.$bvToast.toast(error, {
            title: "Error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    },

    onReset(event) {
      event.preventDefault();

      this.form.username = "";
      this.form.pwd = "";

      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
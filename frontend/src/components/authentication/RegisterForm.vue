<template>
  <div id="register-form">
    <b-card
      border-variant="dark"
      header="Sign up"
      header-text-variant="white"
      header-tag="header"
      header-bg-variant="dark"
      header-class="text-center"
    >
      <template v-for="(eitems, ename) in errors">
        <error-card :key="ename" :ename="ename" :eitems="eitems"/>
      </template>

      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="input-group-usernmae" label="Your username:" label-for="input-username">
          <b-form-input
            id="input-usernmae"
            v-model="form.username"
            type="text"
            required
            placeholder="Enter username"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-email" label="Your email:" label-for="input-email">
          <b-form-input
            id="input-email"
            v-model="form.email"
            required
            type="email"
            placeholder="Enter email"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-pwd" label="Your password:" label-for="input-pwd">
          <b-form-input
            id="input-pwd"
            v-model="form.pwd"
            required
            type="password"
            placeholder="Enter password"
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-pwd-confirmed"
          label="Your password (confirmed):"
          label-for="input-pwd-confirmed"
        >
          <b-form-input
            id="input-pwd-confirmed"
            v-model="form.pwdconf"
            required
            type="password"
            placeholder="Enter password"
          ></b-form-input>
        </b-form-group>

        <b-button class="mr-1" type="submit" variant="outline-dark">Sign up</b-button>
        <b-button class="ml-1" type="reset" variant="dark">Reset</b-button>
      </b-form>
    </b-card>
  </div>
</template>

<script>
import ErrorCard from "../utility/ErrorCard.vue";
import ehandler from "../../utility/errorhandler.js";
export default {
  name: "RegisterForm",

  components: { ErrorCard },

  data() {
    return {
      show: true,
      errors: {},
      form: {
        username: "",
        email: "",
        pwd: "",
        pwdconf: ""
      }
    };
  },

  methods: {
    onSubmit(event) {
      event.preventDefault();
      this.errors = {}

      if (this.form.pwd !== this.form.pwdconf) {
        this.errors = {password: ["Your passwords do not match"]};
        return;
      }

      const username = this.form.username;
      const password = this.form.pwd;
      const email = this.form.email;

      this.$store
        .dispatch("register", {
          user: { username, password, email },
          vue: this
        })
        .then(() => this.$router.push("/"))
        .catch(error => {
          const { data, code } = ehandler.formerror(error);

          if (code) {
            this.errors = data;
          } else {
            this.$bvToast.toast(data, {
              title: "Register Error",
              autoHideDelay: 5000,
              toaster: "b-toaster-bottom-center"
            });
          }
        });
    },

    onReset(event) {
      event.preventDefault();

      this.form.username = "";
      this.form.pwd = "";
      this.form.pwdconf = "";
      this.form.email = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
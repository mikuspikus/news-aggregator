<template>
  <div id="user-form">
    <b-card
      border-variant="dark"
      :header="uuid"
      header-text-variant="white"
      header-tag="header"
      header-bg-variant="dark"
      header-class="text-center"
    >
      <template v-for="(eitems, ename) in errors">
        <error-card :key="ename" :ename="ename" :eitems="eitems" />
      </template>
      <b-form @submit="onSubmit">
        <b-form-group id="input-group-usernmae" label="Username:" label-for="input-username">
          <b-form-input
            id="input-usernmae"
            v-model="form.username"
            type="text"
            disabled
            required
            placeholder="Enter username"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-email" label="Email:" label-for="input-email">
          <b-form-input
            id="input-email"
            v-model="form.email"
            required
            type="email"
            :disabled="!isOwner"
            placeholder="Enter email"
          ></b-form-input>
        </b-form-group>

        <template v-if="isOwner">
          <b-form-group id="input-group-pwd" label="Your password:" label-for="input-pwd">
            <b-form-input
              id="input-pwd"
              v-model="form.pwd"
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
              type="password"
              placeholder="Enter password"
            ></b-form-input>
          </b-form-group>

          <b-button class="mr-1" type="submit" variant="outline-dark">Change</b-button>
        </template>
      </b-form>
    </b-card>
  </div>
</template>

<script>
import ehandler from "../../utility/errorhandler.js";
import ErrorCard from "../utility/ErrorCard.vue";
export default {
  name: "user-form",

  components: { ErrorCard },

  props: {
    uuid: String,
    username: String,
    email: String
  },

  data() {
    return {
      errors: {},
      form: {
        username: this.username,
        email: this.email,
        pwd: "",
        pwdconf: ""
      }
    };
  },

  methods: {
    patch(userdata) {
      this.$http
        .user({
          url: `users/${this.uuid}`,
          data: userdata,
          method: "PATCH"
        })
        .then(response => {
          const data = response.data;
          this.form.email = data.email;
        })
        .catch(error => {
          const { data, code } = ehandler.formerror(error);

          if (code) {
            this.errors = data;
          } else {
            this.$bvToast.toast(data, {
              title: "News Form Error",
              autoHideDelay: 5000,
              toaster: "b-toaster-bottom-center"
            });
          }
        });
    },

    onSubmit(event) {
      event.preventDefault();
      this.errors = {};

      if (this.form.pwd !== this.form.pwdconf) {
        this.errors = { password: ["Your passwords do not match"] };
        return;
      }
      const password = this.form.pwd;

      let userdata = {
        email: this.form.email
      };

      if (password) {
        userdata["password"] = password;
      }

      this.patch(userdata);
    }
  },

  computed: {
    isOwner() {
      return this.$store.getters.uuid === this.uuid;
    }
  }
};
</script>
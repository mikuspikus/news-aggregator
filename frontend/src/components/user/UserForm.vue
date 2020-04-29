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
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="input-group-usernmae" label="Username:" label-for="input-username">
          <b-form-input
            id="input-usernmae"
            v-model="form.username"
            type="text"
            :disabled="!isOwner"
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
        </template>
      </b-form>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "user-form",

  props: {
    uuid: String,
    username: String,
    email: String
  },

  data() {
    return {
      show: true,
      form: {
        username: this.username,
        email: this.email,
        pwd: "",
        pwdconf: ""
      }
    };
  },

  methods: {
    onSubmit(event) {
      event.preventDefault();
    },

    onReset(event) {
      event.preventDefault();
    }
  },

  computed: {
    isOwner() {
      return this.$store.getters.uuid === this.uuid;
    }
  }
};
</script>
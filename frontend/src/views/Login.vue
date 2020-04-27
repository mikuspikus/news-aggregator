<template>
  <div id="login">
    <b-container fluid>
      <b-row class="text-left">
        <b-col cols="4"></b-col>
        <b-col class="pt-5 pb-5">
          <login-form />
        </b-col>
        <b-col cols="4"></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import LoginForm from "../components/authentication/LoginForm.vue";

export default {
  name: "login-view",

  components: {
    LoginForm
  }
};
</script>
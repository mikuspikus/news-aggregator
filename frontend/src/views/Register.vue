<template>
  <div id="register">
    <b-container fluid>
      <b-row class="text-left">
        <b-col cols="4"></b-col>
        <b-col class="pt-5 pb-5">
          <register-form />
        </b-col>
        <b-col cols="4"></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import RegisterForm from "../components/authentication/RegisterForm.vue";

export default {
  name: "register-view",

  components: {
    RegisterForm
  }
};
</script>
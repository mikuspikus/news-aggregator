<template>
  <div id="login">
    <b-container fluid>
      <b-row class="text-left">
        <b-col cols="4"></b-col>
        <b-col class="pt-5 pb-5">
          <user-form :uuid="uuid" />
        </b-col>
        <b-col cols="4"></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import UserForm from "../components/user/UserForm.vue";

export default {
  name: "user-view",

  data() {
    return {
      uuid: this.$route.params.uuid
    };
  },

  components: {
    UserForm
  }
};
</script>
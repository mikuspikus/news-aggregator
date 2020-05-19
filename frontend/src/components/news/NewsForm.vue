<template>
  <div id="news">
    <template v-for="(eitems, ename) in errors">
      <error-card :key="ename" :ename="ename" :eitems="eitems" />
    </template>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="input-group-title" label="Title:" label-for="input-title">
        <b-form-input
          id="input-title"
          v-model="form.title"
          type="text"
          required
          placeholder="Enter title"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-url" label="URL:" label-for="input-url">
        <b-form-input id="input-url" v-model="form.url" type="url" required placeholder="Enter URL"></b-form-input>
      </b-form-group>

      <b-button class="mr-1" type="submit" variant="outline-dark">Submit</b-button>
      <b-button class="ml-1" type="reset" variant="dark">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import ehandler from "../../utility/errorhandler.js";
import ErrorCard from "../utility/ErrorCard.vue";
export default {
  name: "news-form",

  components: { ErrorCard },

  data() {
    return {
      errors: {},
      show: true,
      form: {
        title: "",
        url: ""
      }
    };
  },

  methods: {
    post(data) {
      this.$http
        .news({
          url: "news",
          data: data,
          method: "POST"
        })
        .then(response => {
          this.$router.push({
            name: "NewsSingle",
            params: { uuid: response.data.id }
          });
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
      this.errors = {}
      this.$emit("refetch-news");

      let news_data = {
        title: this.form.title,
        url: this.form.url,
        author: this.$store.getters.uuid
      };
      this.post(news_data);
    },

    onReset(event) {
      event.preventDefault();

      this.form.title = "";
      this.form.url = "";

      this.show = false;
      // magic trick to reset/clear native browser form validation state
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
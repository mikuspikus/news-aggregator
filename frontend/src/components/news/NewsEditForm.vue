<template>
  <div id="news">
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
export default {
  name: "news-form",

  props: {
    news_uuid: String,
    user_uuid: String,
    title: String,
    url: String,
    edited: String,
    edit: Boolean
  },

  data() {
    return {
      show: true,
      form: {
        title: this.title,
        url: this.url
      }
    };
  },

  methods: {
    patch(data) {
      this.$http.news({
        url: `news/${this.news_uuid}`,
        data: data,
        method: "PATCH"
      })
        .then(response => {
          console.log(response);
          this.$emit("update:title", response.data.title);
          this.$emit("update:url", response.data.url);
          this.$emit("update:edited", response.data.edited);
          this.$emit("update:edit", false);
        })
        .catch(error => {
          this.$bvToast.toast(error.message, {
            title: "News editing",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    },

    onSubmit(event) {
      event.preventDefault();
      const news = {
        id: this.news_uuid,
        author: this.user_uuid,
        url: this.form.url,
        title: this.form.title
      };
      this.patch(news);
    },

    onReset(event) {
      event.preventDefault();

      this.form.title = this.title;
      this.form.url = this.url;

      this.show = false;
      // magic trick to reset/clear native browser form validation state
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
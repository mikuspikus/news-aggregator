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
    title: { type: String, default: null },
    url: { type: String, default: null },
    edit: { typr: Boolean },
    uuid: { type: String, default: null }
  },

  data() {
    return {
      show: true,
      form: {
        title: this.title !== null ? this.title : "",
        url: this.url !== null ? this.url : ""
      }
    };
  },

  computed: {
    isNew() {
      return !(this.title || this.url || this.uuid);
    }
  },

  methods: {
    post(data) {
      this.$http.news({
        url: "news",
        data: data,
        method: "POST"
      })
        .then(response => {
          this.$router.push({
            name: "NewsSingle",
            params: { uuid: response.data.uuid }
          });
        })
        .catch(error => {
          this.$bvToast.toast(error.message, {
            title: "Error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    },

    patch(data) {
      this.$http.news({
        url: `news/${this.uuid}`,
        data: data,
        method: "PATCH"
      })
        .then(() => {
          this.$emit('reload')
        })
        .catch(error => {
          this.$bvToast.toast(error.message, {
            title: "Error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    },

    onSubmit(event) {
      event.preventDefault();

      this.$emit("update:title", this.form.title);
      this.$emit("update:url", this.form.url);
      this.$emit("update:edit", false);

      let news_data = {
        title: this.form.title,
        url: this.form.url,
        author: this.$store.getters.uuid
      };

      if (this.isNew) {
        this.post(news_data);
      } else {
        this.patch(news_data);
      }
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
<template>
  <div id="feed-from">
    <b-card
      border-variant="light"
      header="Feed"
      header-text-variant="dark"
      header-tag="header"
      header-bg-variant="light"
      text-variant="dark"
      header-class="text-center"
      class="m-1 text-left"
    >
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group id="input-group-name" label="Feed name:" label-for="input-name">
          <b-form-input
            id="input-name"
            v-model="form.name"
            type="text"
            required
            placeholder="Enter feed name"
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-url" label="Feed URL:" label-for="input-url">
          <b-form-input
            id="input-url"
            v-model="form.url"
            type="url"
            required
            placeholder="Enter feed url"
          ></b-form-input>
        </b-form-group>

        <b-button class="mr-1" type="submit" variant="outline-dark">Submit</b-button>
        <b-button class="ml-1" type="reset" variant="dark">Reset</b-button>
      </b-form>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "feed-form",

  props: {
    user_uuid: String
  },

  data() {
    return {
      show: true,
      form: {
        name: '',
        url: ''
      }
    };
  },

  methods: {
    post(feed) {
      this.$http.rssparser({
        url: 'feeds',
        data: feed,
        method: "POST"
      })
        .then(() => {
          this.$emit("reload-feeds");
        })
        .catch(error => {
          this.$bvToast.toast(error.message, {
            title: "Feed adding error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    },

    onSubmit(event) {
      event.preventDefault();
      const feed = {
        user: this.user_uuid,
        name: this.form.name,
        url: this.form.url
      }
      this.post(feed)
    },

    onReset(event) {
      event.preventDefault();
      this.form.name = "";
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
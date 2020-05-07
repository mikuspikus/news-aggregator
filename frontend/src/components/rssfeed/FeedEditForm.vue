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
import ehandler from "../../utility/errorhandler.js";
export default {
  name: "feed-form",

  props: {
    id: Number,
    user_uuid: String,
    name: String,
    url: String,
    edit: Boolean
  },

  data() {
    return {
      show: true,
      form: {
        name: this.name,
        url: this.url
      }
    };
  },

  methods: {
    patch(feed) {
      this.$http
        .rssparser({
          url: `feeds/${this.id}`,
          data: feed,
          method: "PATCH"
        })
        .then(response => {
          this.$emit("update:name", response.data.name);
          this.$emit("update:url", response.data.url);
          this.$emit("update:edit", false);
          this.$emit("refetch-feed");
        })
        .catch(error => {
          ehandler.error(this, error, "Feed editing error", "Feed not found");
          // if (error.response) {
          //   switch (error.response.status) {
          //     case 401:
          //       this.$router.push({ name: "Login" });
          //       break;
          //   }
          // } else {
          //   this.$bvToast.toast(error.message, {
          //     title: "Feed editing error",
          //     autoHideDelay: 5000,
          //     toaster: "b-toaster-bottom-center"
          //   });
          // }
        });
    },

    onSubmit(event) {
      event.preventDefault();

      const feed = {
        id: this.id,
        user: this.user_uuid,
        name: this.form.name,
        url: this.form.url
      };

      this.patch(feed);
    },

    onReset(event) {
      event.preventDefault();

      this.form.name = this.name;
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
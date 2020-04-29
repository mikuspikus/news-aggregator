<template>
  <div id="comment">
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-comment"
        label="Your comment:"
        label-for="comment-textarea"
        description="Enter at least 10 characters"
      >
        <b-textarea
          id="comment-textarea"
          v-model="form.body"
          :state="form.body.length >= 8"
          placeholder="Write here..."
          rows="3"
          max-rows="6"
        ></b-textarea>
      </b-form-group>

      <b-button class="mr-1" type="submit" variant="outline-dark">Submit</b-button>
      <b-button class="ml-1" type="reset" variant="dark">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "comment-form",

  props: {
    user_uuid: { type: String },
    news_uuid: { type: String }
  },

  data() {
    return {
      show: true,
      form: {
        body: ""
      }
    };
  },

  methods: {
    post(comment) {
      this.$httpcomment({
        url: "comments",
        data: comment,
        method: "POST"
      })
        .then(() => {
          this.$emit("reload-comments");
        })
        .catch();
    },

    onSubmit(event) {
      event.preventDefault();
      const comment = {
        author: this.user_uuid,
        news: this.news_uuid,
        body: this.form.body
      };

      this.post(comment);
    },

    onReset(event) {
      event.preventDefault();

      this.form.body = "";

      this.show = false;
      // magic trick to reset/clear native browser form validation state
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
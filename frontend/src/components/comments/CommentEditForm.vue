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
  name: "comment-edit-form",

  props: {
    id: Number,
    user_uuid: String,
    news_uuid: String,
    edited: String,
    body: String,
    edit: Boolean
  },

  data() {
    return {
      show: true,
      form: {
        body: this.body
      }
    };
  },

  methods: {
    patch(comment) {
      this.$httpcomment({
        url: `comments/${this.id}`,
        data: comment,
        method: "PATCH"
      })
        .then(response => {
          this.$emit("update:body", response.data.body);
          this.$emit("update:edited", response.data.edited);
          this.$emit("update:edit", false);
        })
        .catch(error => {
          this.$bvToast.toast(error.message, {
            title: "Editing error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    },

    onSubmit(event) {
      event.preventDefault();

      const comment = {
        id: this.id,
        author: this.user_uuid,
        news: this.news_uuid,
        body: this.form.body
      };

      this.patch(comment);
    },

    onReset(event) {
      event.preventDefault();

      this.form.body = this.body;

      this.show = false;
      // magic trick to reset/clear native browser form validation state
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
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

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "comment-form",

  props: {
      uuid: String
  },

  data() {
    return {
      show = true,
      form: {
        body: ''
      }
    };
  },

  methods: {
    onSubmit(event) {
      event.preventDefault();
    },

    onReset(event) {
      event.preventDefault();
      this.form.body = '';
      this.show = false;
      // magic trick to reset/clear native browser form validation state
      this.$nextTick(() => { this.show = true })
    }
  }
};
</script>
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

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "news-form",

  props: {
      uuid: String
  },

  data() {
    return {
      show = true,
      form: {
        title: '',
        url: ''
      }
    };
  },

  methods: {
    onSubmit(event) {
      event.preventDefault();
    },

    onReset(event) {
      event.preventDefault();

      this.form.title = '';
      this.form.url = '';

      this.show = false;
      // magic trick to reset/clear native browser form validation state
      this.$nextTick(() => { this.show = true })
    }
  }
};
</script>
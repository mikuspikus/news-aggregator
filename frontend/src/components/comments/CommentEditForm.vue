<template>
  <div id="comment">
    <template v-for="(eitems, ename) in errors">
      <error-card :key="ename" :ename="ename" :eitems="eitems" />
    </template>
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
import ehandler from "../../utility/errorhandler.js";
import ErrorCard from "../utility/ErrorCard.vue";
export default {
  name: "comment-edit-form",

  components: {ErrorCard},

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
      errors: {},
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
<template>
  <div id="index">
    <b-container fluid>
      <b-row class="pt-5" />
      <b-row>
        <b-col />
        <b-col cols="8">
          <news-single :news_uuid="news_uuid" />
        </b-col>
        <b-col />
      </b-row>

      <b-row class="pt-3" />

      <b-row v-if="isLoggedIn">
        <b-col />
        <b-col cols="8">
          <b-card class="text-left">
            <comment-form
              :news_uuid="news_uuid"
              :user_uuid="userUUID"
              v-on:reload-comments="fetchComments()"
            />
          </b-card>
        </b-col>
        <b-col />
      </b-row>

      <b-row class="pt-3" />

      <b-row v-for="comment in comments" :key="comment.id">
        <b-col />
        <b-col cols="8">
          <comment
            v-on:reload-comments="fetchComments()"
            :id="comment.id"
            :user_uuid="comment.author"
            :news_uuid="news_uuid"
            :body="comment.body"
            :created="comment.created"
            :edited="comment.edited"
          />
        </b-col>
        <b-col />
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Comment from "../components/comments/Comment.vue";
import NewsSingle from "../components/news/NewsSingle.vue";
import CommentForm from "../components/comments/CommentForm.vue";
export default {
  name: "news-single-view",

  components: {
    Comment,
    CommentForm,
    NewsSingle
  },

  data() {
    return {
      news_uuid: this.$route.params.uuid,
      comments: []
    };
  },

  created() {
    this.fetchComments();
  },

  methods: {
    fetchComments() {
      this.$httpcomment({
        url: "comments",
        method: "GET",
        params: { news: this.uuid }
      })
        .then(response => {
          this.comments = response.data;
        })
        .catch(error => {
          this.$bvToast.toast(error.message, {
            title: "Error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    }
  },

  computed: {
    userUUID() {
      return this.$store.getters.uuid;
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  }
};
</script>
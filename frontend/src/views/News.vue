<template>
  <div id="index">
    <b-container fluid>
      <b-row class="pt-3" />

      <b-row class="pt-5" />
      <b-row>
        <b-col />
        <b-col cols="8">
          <news-single :news_uuid="news_uuid" />
        </b-col>
        <b-col />
      </b-row>

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

      <template v-if="comments_status.loading">
        <b-spinner class="mt-5" />
      </template>

      <template v-else-if="comments_status.ok">
        <b-row v-for="(comment, index) in comments" :key="comment.id">
          <b-col />
          <b-col cols="8">
            <comment
              v-on:reload-comments="fetchComments"
              v-on:delete-comment-by-index="removeDeletedComment"
              :index="index"
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
      </template>

      <template v-else>
        <b-row class="text-left">
          <b-col />
          <b-col cols="8" class="pt-5 pb-5">
            <b-jumbotron
              bg-variant="dark"
              text-variant="white"
              border-variant="dark"
              class="m-0"
              header
            >
              <template v-slot:header>Error occuried</template>
              <template v-slot:lead>Comments service is probably unavailible</template>
            </b-jumbotron>
          </b-col>
          <b-col />
        </b-row>
      </template>
    </b-container>
  </div>
</template>

<script>
import Comment from "../components/comments/Comment.vue";
import NewsSingle from "../components/news/NewsSingle.vue";
import CommentForm from "../components/comments/CommentForm.vue";
// import ehandler from "../utility/errorhandler.js";
export default {
  name: "news-single-view",

  components: {
    Comment,
    CommentForm,
    NewsSingle
  },

  data() {
    return {
      // news_status: {ok: true, loading: true},
      comments_status: { ok: true, loading: true },
      news_uuid: this.$route.params.uuid,
      comments: []
    };
  },

  created() {
    this.fetchComments();
  },

  methods: {
    removeDeletedComment(index) {
      this.comments.splice(index, 1);
    },

    fetchComments() {
      this.$httpcomment({
        url: "comments",
        method: "GET",
        params: { news: this.uuid }
      })
        .then(response => {
          this.comments_status.loading = false;
          this.comments = response.data;
        })
        .catch(error => {
          this.comments_status.loading = false;
          this.comments_status.ok = false;
          // ehandler.error(
          //   this,
          //   error,
          //   "Comments fetching Error",
          //   `news (UUID: ${this.news_uuid}) not found`
          // );
          this.$bvToast.toast(error.message, {
            title: "Comments fetching Error",
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
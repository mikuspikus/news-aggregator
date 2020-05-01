<template>
  <div id="comment">
    <b-card class="text-left m-0 p-0" no-body>
      <b-card-header header-border-variant="dark" header-bg-variant="dark" class="m-0 p-0">
        <b-navbar type="dark">
          <b-navbar-brand :to="{name: 'User', params: {uuid: comment.author}}">{{ author }}</b-navbar-brand>
          <template v-if="isOwner">
            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
              <b-button
                class="m-0 p-0"
                variant="dark"
                border-variant="dark"
                v-b-tooltip.hover.left="'Edit comment'"
                @click="edit = !edit"
              >
                <b-icon icon="pencil-square"></b-icon>
              </b-button>

              <b-button
                class="m-0 p-0"
                variant="dark"
                border-variant="dark"
                v-b-tooltip.hover.right="'Delete comment'"
              >
                <b-icon icon="x-square-fill" aria-hidden="true"></b-icon>
              </b-button>
            </b-navbar-nav>
          </template>
        </b-navbar>
      </b-card-header>

      <b-card-body class="text-left">
        <template v-if="edit">
          <comment-edit-form
            :id="comment.id"
            :user_uuid="comment.author"
            :news_uuid="comment.news"
            :edited.sync="comment.edited"
            :body.sync="comment.body"
            :edit.sync="edit"
          />
        </template>

        <template v-else>
          <b-card-text>{{ comment.body }}</b-card-text>
        </template>
      </b-card-body>
      <template v-slot:footer>
        <small class="text-muted p-0 m-0">{{ footer }}</small>
      </template>
    </b-card>
  </div>
</template>

<script>
import CommentEditForm from "../comments/CommentEditForm.vue";
// import ehandler from "../../utility/errorhandler.js";

export default {
  components: {
    CommentEditForm
  },

  props: {
    index: Number,
    id: Number,
    user_uuid: String,
    news_uuid: String,
    body: String,
    created: String,
    edited: String
  },

  data() {
    return {
      edit: false,
      comment: {
        id: this.id,
        author: this.user_uuid,
        news: this.news_uuid,
        body: this.body,
        created: this.created,
        edited: this.edited
      },
      user: {}
    };
  },

  created() {
    this.fetchCommentAuthor();
  },

  methods: {
    deleteComment() {
      this.$httpcomment({
        url: `comment/${this.id}`,
        method: "DELETE"
      })
        .then(this.$emit("delete-comment-by-index", this.index))
        .catch(error => {
          this.$bvToast.toast(error.message, {
            title: "Comment delete error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
          // ehandler.error(
          //   this,
          //   error,
          //   "Comment delete error",
          //   "comment has been already deleted"
          // );
        });
    },

    fetchCommentAuthor() {
      this.$httpuser({
        url: `users/${this.comment.author}`,
        method: "GET"
      })
        .then(response => {
          this.user = response.data;
        })
        .catch(error => {
          // ehandler.error(this, error, "Comment author error", "reasons");
          this.$bvToast.toast(error.message, {
            title: "Comment author fetching error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    }
  },

  computed: {
    author() {
      return this.user.username ? this.user.username : this.user_uuid;
    },

    isLogged() {
      return this.$store.getters.isLoggedIn;
    },

    isOwner() {
      return this.isLogged && this.$store.getters.uuid === this.comment.author;
    },

    footer() {
      return this.comment.created === this.comment.edited
        ? `Created at ${this.comment.created}`
        : `Created at ${this.comment.created} | Edited at ${this.comment.edited}`;
    }
  }
};
</script>

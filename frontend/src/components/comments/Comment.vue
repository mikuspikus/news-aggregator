<template>
  <div id="comment">
    <b-card class="text-left m-0 p-0" no-body>
      <b-card-header header-border-variant="dark" header-bg-variant="dark" class="m-0 p-0">
        <b-navbar type="dark">
          <b-navbar-brand :to="{name: 'User', params: {uuid: comment.author.uuid}}">{{ comment.author.username }}</b-navbar-brand>
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
          <comment-form v-bind:body.sync="comment.body" v-bind:edit.sync="edit" />
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
import CommentForm from "../comments/CommentForm.vue";

export default {
  components: {
    CommentForm
  },

  props: {
    cinfo: { type: Object, default: null }
  },

  data() {
    return {
      edit: false,
      comment: {
        author: { uuid: "1", username: "Comment author" },
        body: "Somebody once told me",
        created: "created date",
        edited: "edited date"
      }
    };
  },

  methods: {},

  computed: {
    isLogged() {
      return this.$store.getters.isLoggedIn;
    },

    isOwner() {
      return (
        this.isLogged &&
        this.cinfo !== null &&
        this.$store.getters.username === this.cinfo.user
      );
    },

    footer() {
      return this.comment.created === this.comment.edited
        ? `Created at ${this.comment.created}`
        : `Created at ${this.comment.created} | Edited at ${this.comment.edited}`;
    }
  }
};
</script>

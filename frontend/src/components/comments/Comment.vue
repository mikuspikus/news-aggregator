<template>
  <div id="comment">
    <b-card no-body>
      <b-card-header header-tag="b-navbar">
        <b-navbar toggleable="lg" type="dark" variant="dark">
          <b-navbar-brand href="#">{{ comment.author }}</b-navbar-brand>

          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-button
              variant="outline-light"
              v-b-tooltip.hover
              title="Edit comment"
              @click="editForm"
            >
              <b-icon icon="pencil-square"></b-icon>
            </b-button>

            <b-button variant="outline-light" v-b-tooltip.hover title="Delete comment">
              <b-icon icon="x" aria-hidden="true"></b-icon>
            </b-button>
          </b-navbar-nav>
        </b-navbar>
      </b-card-header>

      <b-card-body class="text-left">
        <template v-if="edit">
          <comment-form v-bind:body.sync="comment.body" v-bind:edit.sync="edit"/>
        </template>

        <template v-else>
          <b-card-text>{{ comment.body }}</b-card-text>
        </template>
      </b-card-body>
      <template v-slot:footer>
        <small class="text-muted">{{ footer }}</small>
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

  data() {
    return {
      edit: false,
      comment: {
        author: "Comment author",
        body: "Somebody once told me",
        created: "created date",
        edited: "edited date"
      }
    };
  },

  methods: {
    editForm(event) {
      event.preventDefault();
      this.edit = !this.edit;
    }
  },

  computed: {
    footer() {
      return this.comment.created === this.comment.edited
        ? `Created at ${this.comment.created}`
        : `Created at ${this.comment.created} | Edited at ${this.comment.edited}`;
    }
  }
};
</script>

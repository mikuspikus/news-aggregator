<template>
  <div id="news">
    <b-card no-body class="text-left m-0 p-0">
      <b-card-header header-border-variant="dark" header-bg-variant="light" class="m-0 p-0">
        <b-navbar type="light">
          <b-navbar-nav variant="light">
            <b-navbar-brand class="ml-0 pl-0" href="#">{{ news.title }}</b-navbar-brand>
            <b-nav-item disabled variant="light">by</b-nav-item>
            <b-navbar-brand
              :to="{ name: 'User', params: { uuid: news.author.uuid }}"
              variant="light"
            >{{ news.author.username }}</b-navbar-brand>
          </b-navbar-nav>

          <template v-if="isOwner">
            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
              <b-button
                class="m-0 p-0"
                variant="light"
                border-variant="light"
                v-b-tooltip.hover.left="'Edit news'"
                @click="edit = !edit"
              >
                <b-icon icon="pencil-square"></b-icon>
              </b-button>

              <b-button
                class="m-0 p-0"
                variant="light"
                border-variant="light"
                v-b-tooltip.hover.right="'Delete news'"
              >
                <b-icon icon="x-square-fill" aria-hidden="true"></b-icon>
              </b-button>
            </b-navbar-nav>
          </template>
        </b-navbar>
      </b-card-header>

      <b-card-body class="text-left">
        <template v-if="edit">
          <news-form
            v-bind:title.sync="news.title"
            v-bind:url.sync="news.url"
            v-bind:edit.sync="edit"
          />
        </template>

        <template v-else>
          <b-card-text>
            <b-link :href="news.url">
            {{ news.url }}
            </b-link>
          </b-card-text>
        </template>
      </b-card-body>
      <template v-slot:footer>
        <small class="text-muted">{{ footer }}</small>
      </template>
    </b-card>
  </div>
</template>

<script>
import NewsForm from "../news/NewsForm.vue";

export default {
  components: {
    NewsForm
  },

  props: {
    ninfo: { type: Object, default: null }
  },

  data() {
    return {
      edit: false,
      news: {
        author: {uuid: '1', username: "news author"},
        title: "news title",
        url: "https://news.url",
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
    isLogged() {
      return this.$store.getters.isLoggedIn;
    },

    isOwner() {
      return (
        this.isLogged &&
        this.ninfo !== null &&
        this.$store.getters.username === this.ninfo.username
      );
    },

    footer() {
      return this.news.created === this.news.edited
        ? `Created at ${this.news.created}`
        : `Created at ${this.news.created} | Edited at ${this.news.edited}`;
    }
  }
};
</script>

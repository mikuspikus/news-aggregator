<template>
  <div id="news">
    <b-card no-body class="text-left m-0 p-0">
      <b-card-header header-border-variant="dark" header-bg-variant="light" class="m-0 p-0">
        <b-navbar type="light">
          <b-navbar-nav variant="light">
            <b-navbar-brand class="ml-0 pl-0">{{ news.title }}</b-navbar-brand>
            <b-nav-item disabled variant="light">by</b-nav-item>
            <b-navbar-brand
              :to="{ name: 'User', params: { uuid: news.author.id }}"
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
          <news-edit-form
            :news_uuid="news_uuid"
            :user_uuid="userUUID"
            :title.sync="news.title"
            :url.sync="news.url"
            :edited.sync="news.edited"
            :edit.sync="edit"
            v-on:reload-news="fetchData()"
          />
        </template>

        <template v-else>
          <b-card-text>
            <b-link :href="news.url">{{ news.url }}</b-link>
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
import NewsEditForm from "../news/NewsEditForm.vue";

export default {
  components: {
    NewsEditForm
  },

  props: {
    news_uuid: { type: String }
  },

  data() {
    return {
      edit: false,
      news: { author: { id: null, username: null } }
    };
  },

  methods: {
    fetchData() {
      this.$httpnews({ url: `news/${this.news_uuid}`, method: "GET" })
        .then(response => {
          this.news = response.data;

          this.$httpuser({ url: `users/${this.news.author}`, method: "GET" })
            .then(response => {
              this.news.author = response.data;
            })
            .catch(error => {
              this.$bvToast.toast(error.message, {
                title: "Error",
                autoHideDelay: 5000,
                toaster: "b-toaster-bottom-center"
              });
            });
        })
        .catch(error => {
          this.$bvToast.toast(error.message, {
            title: "Error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    },
    editForm(event) {
      event.preventDefault();
      this.edit = !this.edit;
    }
  },

  created() {
    this.fetchData();
  },

  computed: {
    userUUID() {
      return this.$store.getters.uuid;
    },
    isLogged() {
      return this.$store.getters.isLoggedIn;
    },

    isOwner() {
      return this.isLogged && this.$store.getters.uuid === this.news.author.id;
    },

    footer() {
      return this.news.created === this.news.edited
        ? `Created at ${this.news.created}`
        : `Created at ${this.news.created} | Edited at ${this.news.edited}`;
    }
  }
};
</script>

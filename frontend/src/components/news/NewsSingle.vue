<template>
  <div id="news">
    <template v-if="news_status.loading">
      <b-spinner class="mt-3" />
    </template>

    <template v-else-if="news_status.ok">
      <b-card no-body class="text-left m-0 p-0">
        <b-card-header header-border-variant="dark" header-bg-variant="light" class="m-0 p-0">
          <b-navbar type="light">
            <b-navbar-nav variant="light">
              <b-navbar-brand class="ml-0 pl-0">{{ news.title }}</b-navbar-brand>
              <b-nav-text class="mr-3">by</b-nav-text>
              <b-navbar-brand
                :to="{ name: 'User', params: { uuid: id }}"
                variant="light"
              >{{ username }}</b-navbar-brand>
            </b-navbar-nav>

            <b-navbar-nav class="ml-auto">
              <template v-if="isLoggedIn">
                <b-button
                  v-if="!vote.upvoted"
                  class="m-0 p-0"
                  variant="light"
                  border-variant="light"
                  v-b-tooltip.hover.top="'Upvote'"
                  @click="upvote"
                >
                  <b-icon icon="arrow-up" />
                </b-button>

                <b-button
                  v-if="!vote.downvoted"
                  class="m-0 p-0"
                  variant="light"
                  border-variant="light"
                  v-b-tooltip.hover.top="'Downvote'"
                  @click="downvote"
                >
                  <b-icon icon="arrow-down" />
                </b-button>
              </template>
              <b-nav-text>Score: {{ formatScore(news.score) }}</b-nav-text>
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
                  @click="deleteNews"
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
    </template>

    <template v-else>
      <b-jumbotron
        bg-variant="dark"
        text-variant="white"
        border-variant="dark"
        class="m-0 text-left"
        header
      >
        <template v-slot:header>Error occuried</template>
        <template v-slot:lead>News service is probably unavailible</template>
      </b-jumbotron>
    </template>
  </div>
</template>

<script>
import NewsEditForm from "../news/NewsEditForm.vue";
// import ehandler from "../../utility/errorhandler.js";

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
      vote: { upvoted: false, downvoted: false },
      news_status: { loading: true, ok: true },
      news: { author: { id: null, username: null } }
    };
  },

  methods: {
    formatScore(score) {
      return score.toFixed(1);
    },

    upvote() {
      this.voteaction(true);
      this.vote.downvoted = false;
      this.vote.upvoted = true;
    },

    downvote() {
      this.voteaction(false);
      this.vote.downvoted = true;
      this.vote.upvoted = false;
    },

    voteaction(is_up) {
      this.$http
        .news({
          url: `news/${this.news_uuid}/vote`,
          data: { is_up: is_up },
          // headers: { Authorization: `Bearer ${this.$store.getters.token}` },
          method: "POST"
        })
        .then(response => {
          this.news = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    deleteNews() {
      this.$http
        .news({
          url: `news/${this.news_uuid}`,
          method: "DELETE"
        })
        .then(() => {
          this.$router.push({ name: "Home" });
        })
        .catch(error => {
          this.$bvToast.toast(error.message, {
            title: "News deleting error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
          // ehandler.error(
          //   this,
          //   error,
          //   "News delete Error",
          //   "news (UUID: ${this.news_uuid}) not found"
          // );
        });
    },

    fetchVote() {
      this.$http
        .news({
          url: `news/${this.news_uuid}/vote`,
          method: "GET"
        })
        .then(response => {
          this.vote = response.data;
        })
        .catch();
    },

    fetchUser() {
      this.$http
        .user({
          url: `users/${this.news.author}`,
          method: "GET"
        })
        .then(response => {
          this.news.author = response.data;
        })
        .catch(error => {
          // ehandler.error(this, error, 'News fetching Error', `news (UUID: ${this.news_uuid}) not found`)
          this.$bvToast.toast(error.message, {
            title: "User fetching error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    },

    fetchNews() {
      this.$http
        .news({
          url: `news/${this.news_uuid}`,
          // headers: { Authorization: `Bearer ${this.$store.getters.token}` },
          method: "GET"
        })
        .then(response => {
          this.news_status.loading = false;
          this.news_status.ok = true;

          this.news = response.data;

          this.fetchUser();
          this.fetchVote();
        })
        .catch(error => {
          this.news_status.loading = false;
          this.news_status.ok = false;

          // ehandler.error(
          //   this,
          //   error,
          //   "News fetching Error",
          //   `news (UUID: ${this.news_uuid}) not found`
          // );
          this.$bvToast.toast(error.message, {
            title: "News fetching error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    }
  },

  created() {
    this.fetchNews();
  },

  computed: {
    username() {
      return this.news.author.username
        ? this.news.author.username
        : this.news.author;
    },

    id() {
      return this.news.author.id ? this.news.author.id : this.news.author;
    },

    userUUID() {
      return this.$store.getters.uuid;
    },
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },

    isOwner() {
      return this.isLoggedIn && this.$store.getters.uuid === this.id;
    },

    footer() {
      return this.news.created === this.news.edited
        ? `Created at ${this.news.created}`
        : `Created at ${this.news.created} | Edited at ${this.news.edited}`;
    }
  }
};
</script>

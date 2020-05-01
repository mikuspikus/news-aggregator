<template>
  <div id="sidebar">
    <b-sidebar id="sidebar-feeds" title="Feeds" bg-variant="dark" text-variant="light" shadow>
      <div class="px-3 py-2">
        <template v-if="!ok">
          <b-jumbotron
            bg-variant="light"
            text-variant="dark"
            border-variant="light"
            class="m-0"
            header
          >
            <template v-slot:lead>Feed service is probably unavailible</template>
          </b-jumbotron>
        </template>

        <template v-else>
          <feed-form :user_uuid="userUUID" v-on:reload-feeds="fetchFeeds" />

          <template v-if="loading">
            <b-spinner variant="light" />
          </template>

          <template v-else>
            <div role="tablist">
              <feed
                v-for="(feed, index) in feeds"
                :key="feed.id"
                :user_uuid="userUUID"
                :index="index"
                :id="feed.id"
                :title="feed.name"
                :url="feed.url"
                v-on:delete-feed-by-index="removeDeletedFeed"
              />
            </div>
          </template>
        </template>
      </div>
    </b-sidebar>
  </div>
</template>

<script>
import Feed from "../rssfeed/Feed.vue";
import FeedForm from "../rssfeed/FeedForm.vue";
import ehandler from "../../utility/errorhandler.js";

export default {
  name: "feeds",

  components: { Feed, FeedForm },

  data() {
    return {
      loading: true,
      ok: true,
      feeds: [],
      parsedfeeds: []
    };
  },

  computed: {
    userUUID() {
      return this.$store.getters.uuid;
    }
  },

  created() {
    this.fetchFeeds();
  },

  methods: {
    removeDeletedFeed(index) {
      this.feeds.splice(index, 1);
    },

    fetchFeeds() {
      this.$http.rssparser({
        url: "feeds",
        params: { user: this.userUUID },
        method: "GET"
      })
        .then(response => {
          this.loading = false;
          this.feeds = response.data;
        })
        .catch(error => {
          this.loading = false;
          this.ok = false;
          ehandler.error(this, error, "Feeds fetching Error")
          // this.$bvToast.toast(error.message, {
          //   title: "Feeds getting error",
          //   autoHideDelay: 5000,
          //   toaster: "b-toaster-bottom-center"
          // });
        });
    }
  }
};
</script>
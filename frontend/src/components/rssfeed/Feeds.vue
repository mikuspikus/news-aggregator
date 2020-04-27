<template>
  <div id="sidebar">
    <b-sidebar id="sidebar-feeds" title="Feeds" bg-variant="dark" text-variant="light" shadow>
      <div class="px-3 py-2">
        <feed-form />
        <div role="tablist">
          <feed v-for="(feed, index) in feeds" :key="feed.title" :feed="feed" :index="index" />
        </div>
      </div>
    </b-sidebar>
  </div>
</template>

<script>
import Feed from "../rssfeed/Feed.vue";
import FeedForm from "../rssfeed/FeedForm.vue";

export default {
  name: "feeds",

  components: { Feed, FeedForm },

  props: {},

  data() {
    return {
      feeds: [
        {
          title: "Memes title",
          url: "memes.com",
          items: [
            { title: "Memes", url: "https://memes.com" },
            { title: "джигурда", url: "https://джигурда.рф" }
          ]
        },
        {
          title: "Example title",
          url: "example.com",
          items: [{ title: "Example", url: "https://example.com" }]
        }
      ]
    };
  }
};
</script>
<template>
  <div id="sidebar">
    <b-sidebar id="sidebar-feeds" title="Feeds" bg-variant="dark" text-variant="light" shadow>
      <div class="px-3 py-2">
        <div role="tablist">
          <feed v-for="(feed, index) in feeds" :key="feed.title" :feed="feed" :index="index" />
        </div>
      </div>
    </b-sidebar>
  </div>
</template>

<script>
import Feed from "../rssfeed/Feed.vue";
export default {
  name: "feeds",

  components: { Feed },

  props: {},

  data() {
    return {
      feeds: [
        {
          title: "Memes title",
          items: [{ title: "Memes", url: "memes.com" }]
        },
        {
          title: "Example title",
          items: [{ title: "Example", url: "example.com" }]
        }
      ]
    };
  }
};
</script>
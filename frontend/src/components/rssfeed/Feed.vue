<template>
  <div id="feed">
    <b-card no-body class="mb-1" text-variant="dark">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block v-b-toggle="'accordion-' + index" variant="dark">{{ feed.title }}</b-button>
      </b-card-header>
      <b-collapse :id="'accordion-' + index" visible accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-link :href="fitem.url" v-for="fitem in feed.items" :key="fitem.title">{{ fitem.title }}</b-link>
        </b-card-body>
      </b-collapse>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "feed",

  data() {
    return {
      // feed: {
      //   title: "Example title",
      //   items: [{ title: "Memes", url: "memes.com" }]
      // }
    };
  },

  props: {
    index: { Type: Number, default: 1 },
    feed: { Type: Object, default: null }
  }
};
</script>
<template>
  <div id="feed">
    <b-card no-body class="mb-1" text-variant="dark">
      <b-card-header
        header-border-variant="dark"
        header-bg-variant="dark"
        class="p-0 m-0"
        role="tab"
      >
        <b-navbar type="dark">
          <b-navbar-brand v-b-toggle="'accordion-' + index">{{ feed.title }}</b-navbar-brand>
          <template v-if="isOwner">
            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
              <b-button
                class="m-0 p-0"
                variant="dark"
                border-variant="dark"
                v-b-tooltip.hover.left="'Edit feed'"
                @click="edit = !edit"
              >
                <b-icon icon="pencil-square"></b-icon>
              </b-button>

              <b-button
                class="m-0 p-0"
                variant="dark"
                border-variant="dark"
                @click="deleteItem"
                v-b-tooltip.hover.right="'Delete feed'"
              >
                <b-icon icon="x-square-fill" aria-hidden="true"></b-icon>
              </b-button>
            </b-navbar-nav>
          </template>
        </b-navbar>
      </b-card-header>
      <template v-if="edit">
        <feed-form :name.sync="feed.title" :url.sync="feed.url" :edit.sync="edit" />
      </template>

      <template v-else>
        <b-collapse :id="'accordion-' + index" visible accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <b-link
              v-for="fitem in feed.items"
              :key="fitem.title"
              :href="fitem.url"
            >{{ fitem.title }}<br/></b-link>
          </b-card-body>
        </b-collapse>
      </template>
    </b-card>
  </div>
</template>

<script>
import FeedForm from "../rssfeed/FeedForm.vue";
export default {
  name: "feed",

  components: { FeedForm },

  data() {
    return {
      edit: false
      // feed: {
      //   title: "Example title",
      //   items: [{ title: "Memes", url: "memes.com" }]
      // }
    };
  },

  props: {
    index: { Type: Number, default: 1 },
    feed: { Type: Object, default: null }
  },

  computed: {
    isOwner() {
      return true;
    }
  },

  methods: {
    deleteItem() {}
  }
};
</script>
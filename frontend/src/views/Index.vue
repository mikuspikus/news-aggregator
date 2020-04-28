<template>
  <div id="index">
    <b-container fluid class="pt-5">
      <b-row v-if="isLoggedIn">
        <b-col />

        <b-col cols="8" class="mb-5 text-left">
          <b-card
            border-variant="dark"
            header="Post news"
            header-text-variant="light"
            header-tag="header"
            header-bg-variant="dark"
            header-class="text-center"
            class="m-1 text-left"
          >
            <news-form />
          </b-card>
        </b-col>

        <b-col />
      </b-row>
      <template v-for="shortnews in news">
        <b-row :key="shortnews.uuid">
          <b-col />
          <b-col cols="8">
            <news-short
              :uuid="shortnews.uuid"
              :title="shortnews.title"
              :url="shortnews.url"
              :created="shortnews.created"
            />
          </b-col>
          <b-col />
        </b-row>
      </template>
    </b-container>
  </div>
</template>

<script>
import NewsShort from "../components/news/NewsShort.vue";
import NewsForm from "../components/news/NewsForm.vue";

export default {
  name: "index-view",

  components: { NewsShort, NewsForm },

  computed:{
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },

  data() {
    return {
      news: [
        {
          uuid: "1",
          title: "Example title 1",
          url: "example.com",
          created: "27.4.2020"
        },
        {
          uuid: "2",
          title: "Example title 2",
          url: "example.com",
          created: "27.4.2020"
        },
        {
          uuid: "3",
          title: "Example title 3",
          url: "example.com",
          created: "27.4.2020"
        }
      ]
    };
  }
};
</script>
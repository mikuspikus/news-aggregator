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
        <b-row :key="shortnews.id">
          <b-col />
          <b-col cols="8">
            <news-short
              :uuid="shortnews.id"
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

  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },

  created() {
    this.$httpnews({ url: "news", methos: "GET" })
      .then(response => {
        this.news = response.data;
      })
      .catch(error => {
        this.$bvToast.toast(error.message, {
          title: "Error",
          autoHideDelay: 5000,
          toaster: "b-toaster-bottom-center"
        });
      });
  },

  data() {
    return {
      news: []
    };
  }
};
</script>
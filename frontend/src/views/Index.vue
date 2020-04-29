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

      <b-row class="pt-3" />

      <template v-if="loading">
        <b-spinner variant="dark" />
      </template>

      <template v-else-if="ok">
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
      </template>

      <template v-else>
        <b-row class="text-left">
          <b-col />
          <b-col cols="8" class="pt-5 pb-5">
            <b-jumbotron
              bg-variant="dark"
              text-variant="white"
              border-variant="dark"
              class="m-0"
              header
            >
              <template v-slot:header>Error occuried</template>
              <template v-slot:lead>News service is probably unavailible</template>
            </b-jumbotron>
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
import ehandler from "../utility/errorhandler.js";
export default {
  name: "index-view",

  components: { NewsShort, NewsForm },

  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },

  created() {
    this.fetchNews();
  },

  methods: {
    fetchNews() {
      
      this.$httpnews({ url: "news", method: "GET" })
        .then(response => {
          this.loading = false;
          this.news = response.data;
        })
        .catch(error => {
          this.loading = false;
          this.ok = false;
          ehandler.error(this, error, "News loading Error", "reasons");
          // this.$bvToast.toast(error.message, {
          //   title: "News loading error",
          //   autoHideDelay: 5000,
          //   toaster: "b-toaster-bottom-center"
          // });
        });
    }
  },

  data() {
    return {
      loading: true,
      ok: true,
      news: []
    };
  }
};
</script>
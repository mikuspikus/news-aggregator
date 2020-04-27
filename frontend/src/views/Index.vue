<template>
  <div id="index">
    <b-container fluid class="pt-5">
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

export default {
  name: "index",

  components: { NewsShort },

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
  },
};
</script>
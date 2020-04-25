<template>
  <div id="index">
    <navbar />
    <feeds />

    <b-container fluid>
      <b-row class="text-center">
        <b-col></b-col>
        <b-col cols="8">
          <single-news />
        </b-col>
        <b-col></b-col>
      </b-row>

      <b-row>
        <b-col></b-col>
        <b-col cols="8">
          <comment />
        </b-col>
        <b-col></b-col>
      </b-row>
    </b-container>

  </div>
</template>

<script>
import Navbar from "../components/utility/Navbar.vue";
import Feeds from "../components/rssfeed/Feeds.vue";
import Comment from '../components/comments/Comment.vue'
import SingleNews from "../components/news/SingleNews.vue";

export default {
  components: {
    Navbar,
    Feeds,
    Comment,
    SingleNews
  }
};
</script>
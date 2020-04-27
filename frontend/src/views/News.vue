<template>
  <div id="index">
    <b-container fluid>
      <b-row class="pt-5"/>
      <b-row>
        <b-col/>
        <b-col cols="8">
          <news-single />
        </b-col>
        <b-col/>
      </b-row>

      <b-row class="pt-3"/>

      <b-row>
        <b-col/>
        <b-col cols="8">
          <comment />
        </b-col>
        <b-col/>
      </b-row>

      <b-row>
        <b-col/>
        <b-col cols="8">
          <comment />
        </b-col>
        <b-col/>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Comment from "../components/comments/Comment.vue";
import NewsSingle from "../components/news/NewsSingle.vue";
export default {
  name: 'news-single-view',

  components: {
    Comment,
    NewsSingle
  }
};
</script>
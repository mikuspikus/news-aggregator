<template>
  <div id="news-short">
    <b-card class="m-0 p-0 text-left">
      <b-card-text class="p-0 m-0">
        <b-link :to="{ name: 'NewsSingle', params: { uuid: uuid }}">{{ title }}</b-link>
      </b-card-text>
      <template v-slot:footer>
        <small class="text-muted p-0 m-0">Created at {{ created }}</small>
      </template>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "news-short",

  props: {
    uuid: { type: String },
    title: { type: String },
    url: { type: String },
    created: { type: String }
  }
};
</script>
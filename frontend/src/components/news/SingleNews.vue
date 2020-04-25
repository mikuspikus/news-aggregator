<template>
  <div id="comment">
    <b-card no-body>
      <b-card-header header-tag="b-navbar">
        <b-navbar toggleable="lg" type="dark" variant="dark">
          <!-- <b-navbar-brand href="#">{{ news.title }}</b-navbar-brand>
          <b-navbar-brand variant="light">by</b-navbar-brand>
          <b-navbar-brand href="#" variant="light">{{ news.author }}</b-navbar-brand>-->

          <!-- <b-navbar-nav>
            <b-nav-item href="#" variant="light">{{ news.title }}</b-nav-item>
            <b-nav-item variant="light">by</b-nav-item>
            <b-nav-item href="#" variant="light">{{ news.author }}</b-nav-item>
          </b-navbar-nav>-->

          <b-navbar-nav>
            <b-navbar-brand href="#">{{ news.title }}</b-navbar-brand>
            <b-nav-item variant="light">by</b-nav-item>
            <b-navbar-brand href="#" variant="light">{{ news.author }}</b-navbar-brand>
          </b-navbar-nav>

          <!-- <b-navbar-nav>
            <b-nav-item href="#" variant="light">{{ news.title }}</b-nav-item>
            <b-navbar-brand variant="light">by</b-navbar-brand>
            <b-nav-item href="#" variant="light">{{ news.author }}</b-nav-item>
          </b-navbar-nav>-->

          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-button
              variant="outline-light"
              v-b-tooltip.hover
              title="Edit comment"
              @click="editForm"
            >
              <b-icon icon="pencil-square"></b-icon>
            </b-button>

            <b-button variant="outline-light" v-b-tooltip.hover title="Delete comment">
              <b-icon icon="x" aria-hidden="true"></b-icon>
            </b-button>
          </b-navbar-nav>
        </b-navbar>
      </b-card-header>

      <b-card-body class="text-left">
        <template v-if="edit">
          <news-form v-bind:title.sync="news.title" v-bind:url.sync="news.url" v-bind:edit.sync="edit"/>
        </template>

        <template v-else>
          <b-card-text>{{ news.url }}</b-card-text>
        </template>
      </b-card-body>
      <template v-slot:footer>
        <small class="text-muted">{{ footer }}</small>
      </template>
    </b-card>
  </div>
</template>

<script>
import NewsForm from "../news/NewsForm.vue";

export default {
  components: {
    NewsForm
  },

  data() {
    return {
      edit: false,
      news: {
        author: "news author",
        title: "news title",
        url: "news url",
        created: "created date",
        edited: "edited date"
      }
    };
  },

  methods: {
    // change(obj) {
    //   this.news.title = obj.title;
    //   this.news.url = obj.url;
    // },
    editForm(event) {
      event.preventDefault();
      this.edit = !this.edit;
    }
  },

  computed: {
    footer() {
      return this.news.created === this.news.edited
        ? `Created at ${this.news.created}`
        : `Created at ${this.news.created} | Edited at ${this.news.edited}`;
    }
  }
};
</script>

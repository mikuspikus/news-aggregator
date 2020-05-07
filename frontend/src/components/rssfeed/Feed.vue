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
          <b-navbar-brand v-b-toggle="'accordion-' + index">{{ title }}</b-navbar-brand>
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
                @click="deleteFeed"
                v-b-tooltip.hover.right="'Delete feed'"
              >
                <b-icon icon="x-square-fill" aria-hidden="true"></b-icon>
              </b-button>
            </b-navbar-nav>
          </template>
        </b-navbar>
      </b-card-header>
      <template v-if="edit">
        <feed-edit-form
          :id="id"
          :user_uuid="userUUID"
          :name.sync="title"
          :url.sync="url"
          :edit.sync="edit"
          v-on:refetch-feed="fetchParsedFeed"
        />
      </template>

      <template v-else>
        <b-collapse :id="'accordion-' + index" accordion="my-accordion" role="tabpanel">
          <b-card-body>
            <template v-for="(eitems, ename) in errors">
              <error-card :key="ename" :ename="ename" :eitems="eitems" />
            </template>
            <b-link v-for="entry in entries" :key="entry.title" :href="entry.link">
              {{ entry.title }}
              <br />
            </b-link>
          </b-card-body>
        </b-collapse>
      </template>
    </b-card>
  </div>
</template>

<script>
import FeedEditForm from "../rssfeed/FeedEditForm.vue";
import ehandler from "../../utility/errorhandler.js";
import ErrorCard from "../utility/ErrorCard.vue";

export default {
  name: "feed",

  components: { FeedEditForm, ErrorCard },

  props: {
    id: Number,
    user_uuid: String,
    index: Number,
    title: String,
    url: String
  },

  data() {
    return {
      errors: {},
      edit: false,
      entries: []
    };
  },

  created() {
    this.fetchParsedFeed();
  },

  computed: {
    isOwner() {
      return this.$store.getters.uuid === this.user_uuid;
    }
  },

  methods: {
    fetchParsedFeed() {
      this.errors = {};
      this.entries = [];
      this.$http
        .rssparser({ url: `feeds/${this.id}/parse`, method: "GET" })
        .then(response => {
          this.entries = response.data.entries;
        })
        .catch(error => {
          const { data, code } = ehandler.feedparseerror(error);

          this.errors = { "Feed parsing error": [data] };

          this.$bvToast.toast(data, {
            title: code
              ? `Feed parsing error with code ${code}`
              : "Feed parsing error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    },

    deleteFeed() {
      this.$http
        .rssparser({
          url: `feeds/${this.id}`,
          method: "DELETE"
        })
        .then(() => {
          this.$emit("delete-feed-by-index", this.index);
        })
        .catch(error => {
          this.$bvToast.toast(error.message, {
            title: "Feed deleting error",
            autoHideDelay: 5000,
            toaster: "b-toaster-bottom-center"
          });
        });
    }
  }
};
</script>
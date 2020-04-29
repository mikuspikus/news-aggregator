<template>
  <div id="not-found">
    <b-container fluid>
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
            <template v-slot:header>404 Not Found</template>

            <template v-slot:lead>You were redirect to this page because {{ reason }}</template>
          </b-jumbotron>
        </b-col>
        <b-col />
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: "not-found-views",

  props: {
    reason: { type: String, default: "URL not found" }
  }
};
</script>
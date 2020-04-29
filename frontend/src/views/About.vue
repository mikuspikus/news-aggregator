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
            <template v-slot:header>About</template>

            <template v-slot:lead>Example implementation of news agragator with RSS-feed parser with Django 3, Django Rest Framework and Vue.js 2</template>
          </b-jumbotron>
        </b-col>
        <b-col />
      </b-row>
    </b-container>
  </div>
</template>

<template>
  <div id="error-card">
    <b-list-group class="mb-1">
      <b-list-group-item v-for="eitem in eitems" :key="eitem" active button variant="dark">
        <h5 class="mb-1">{{ ename }}</h5>
        <p class="mb-1">{{ eitem }}</p>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
export default {
  props: {
    ename: { type: String, required: true },
    eitems: { type: Array, required: true }
  }
};
</script>
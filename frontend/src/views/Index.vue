<template>
    <div id = "index">
        <navbar/>
        <feeds/>
    </div>
</template>

<script>
import navbar from '../components/utility/Navbar.vue'
import Feeds from '../components/rssfeed/Feeds.vue'
export default {
    components: {
        navbar, Feeds
    }
}
</script>
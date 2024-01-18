<template>
    <!--     <div v-if="store.user">
        <div v-if="store.user.username"> -->
    <router-view></router-view>
</template>
  
<script>
import { ref } from 'vue'
import { store } from './store/store.js'

export default {
    name: 'App',
    setup() {
        return {
            drawer: ref(false),
            miniState: ref(true),
        }
    },
    data() {
        return {
            store,

        }
    },
    created() {
        window.addEventListener('beforeunload', (e) => {
            if (store.warning) {
                e.preventDefault()
                e.returnValue = ''
            }
        })
    },
    /* methods: {
        processLogout() {
            this.$router.push({ name: 'Login' })
        }
    } */
}
</script>

<style>
@import './assets/styles/main.css';
@import './assets/styles/quasar.css';
</style>
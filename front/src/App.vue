<template>
    <q-layout view="hHh LpR fFf" class="shadow-2">

        <q-page-container>
            <q-page class="q-pa-md">

                <Header v-if="store.user && store.user.username"></Header>
                <Sidebar v-if="store.user && store.user.username"></Sidebar>

                <router-view></router-view>

            </q-page>
        </q-page-container>

    </q-layout>
</template>
  
<script>
import { ref } from 'vue'
import { store } from './store/store.js'
import Header from './components/Header.vue'
import Sidebar from './components/Sidebar.vue'

export default {
    name: 'App',
    components: { Header, Sidebar },
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
}
</script>

<style>
@import './assets/styles/main.css';
@import './assets/styles/quasar.css';
</style>
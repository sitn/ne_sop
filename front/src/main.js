import { createApp } from 'vue'
import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import { Quasar } from 'quasar'
import App from './App.vue'
import Items from '@/views/Items.vue'
import Persons from '@/views/Persons.vue'
import Events from '@/views/Events.vue'
import Statistics from '@/views/Statistics.vue'

const routes = [
    { path: '/items', name: 'Items', component: Items },
    { path: '/persons', name: 'Persons', component: Persons },
    { path: '/events', name: 'Events', component: Events },
    { path: '/statistics', name: 'Statistics', component: Statistics }
]

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHashHistory(),
    routes, // short for `routes: routes`
})

const app = createApp(App)
app.use(Quasar, {
    config: {
    },

})
app.use(router)
app.mount('#q-app')
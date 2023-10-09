import { createApp } from 'vue'
import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import { Quasar } from 'quasar'
import App from './App.vue'
import ItemsList from './views/ItemsList.vue'
import EntitiesList from './views/EntitiesList.vue'
import EventsList from './views/EventsList.vue'
import Event from './views/Event.vue'
import NewEvent from './views/NewEvent.vue'
import Statistics from './views/Statistics.vue'
import Item from './views/Item.vue'
import NewItem from './views/NewItem.vue'
import Entity from './views/Entity.vue'
import NewEntity from './views/NewEntity.vue'
// import UsersList from './views/UsersList.vue'
import User from './views/User.vue'
import NewUser from './views/NewUser.vue'
import Login from './views/Login.vue'
import Admin from './views/Admin.vue'
import Help from './views/Help.vue'

const routes = [
    { path: '/items', name: 'ItemsList', component: ItemsList },
    { path: '/items/:id', name: 'Item', component: Item, props: true },
    { path: '/items/new', name: 'NewItem', component: NewItem },
    { path: '/entities', name: 'EntitiesList', component: EntitiesList },
    { path: '/entities/:id', name: 'Entity', component: Entity, props: true },
    { path: '/entities/new', name: 'NewEntity', component: NewEntity },
    { path: '/events', name: 'EventsList', component: EventsList },
    { path: '/events/:id', name: 'Event', component: Event, props: true },
    { path: '/events/new', name: 'NewEvent', component: NewEvent },
    { path: '/statistics', name: 'Statistics', component: Statistics },
    /* { path: '/users', name: 'UsersList', component: UsersList }, */
    { path: '/login', name: 'Login', component: Login },
    { path: '/admin', name: 'Admin', component: Admin },
    { path: '/admin/users/:id', name: 'User', component: User, props: true },
    { path: '/admin/users/new', name: 'NewUser', component: NewUser },
    { path: '/help', name: 'Help', component: Help }
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
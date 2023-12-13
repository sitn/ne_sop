import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import { store } from './store/store.js'

import ItemsList from './views/ItemsList.vue'
import EntitiesList from './views/EntitiesList.vue'
import EventsList from './views/EventsList.vue'
import Event from './views/Event.vue'
import EventUniversal from './views/EventUniversal.vue'
import NewEvent from './views/NewEvent.vue'
import Statistics from './views/Statistics.vue'
import Item from './views/Item.vue'
import NewItem from './views/NewItem.vue'
import ItemUniversal from './views/ItemUniversal.vue'
import Entity from './views/Entity.vue'
import NewEntity from './views/NewEntity.vue'
import EntityUniversal from './views/EntityUniversal.vue'
import User from './views/User.vue'
import NewUser from './views/NewUser.vue'
import Login from './views/Login.vue'
import Admin from './views/Admin.vue'
import Help from './views/Help.vue'

const routes = [
    { path: '/', redirect: '/items' },
    { path: '/items', name: 'ItemsList', component: ItemsList },
    /*
    { path: '/items/:id', name: 'Item', component: Item, props: true },
    { path: '/items/new', name: 'NewItem', component: NewItem },
    */
    { path: '/items/:id', name: 'Item', component: ItemUniversal, props: true },
    { path: '/items/new', name: 'NewItem', component: ItemUniversal },
    { path: '/entities', name: 'EntitiesList', component: EntitiesList },
    /*
    { path: '/entities/:id', name: 'Entity', component: Entity, props: true },
    { path: '/entities/new', name: 'NewEntity', component: NewEntity },
    */
    { path: '/entities/:id', name: 'Entity', component: EntityUniversal, props: true },
    { path: '/entities/new', name: 'NewEntity', component: EntityUniversal },
    { path: '/events', name: 'EventsList', component: EventsList },
    /*
    { path: '/events/:id', name: 'Event', component: Event, props: true },
    { path: '/events/new', name: 'NewEvent', component: NewEvent },
    */
    { path: '/events/:id', name: 'Event', component: EventUniversal, props: true },
    { path: '/events/new', name: 'NewEvent', component: EventUniversal },
    { path: '/statistics', name: 'Statistics', component: Statistics },
    { path: '/login', name: 'Login', component: Login },
    { path: '/admin', name: 'Admin', component: Admin },
    { path: '/admin/users/:id', name: 'User', component: User, props: true },
    { path: '/admin/users/new', name: 'NewUser', component: NewUser },
    { path: '/help', name: 'Help', component: Help }
]

export const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHashHistory(),
    routes // short for `routes: routes`
})

// navigation guards
router.beforeEach(async (to, from) => {

    store.navigation.from = from.fullPath
    store.navigation.to = to.fullPath
    //  return false to cancel the navigation
    console.log(`from: ${from}, to: ${to}`)

    // DISPLAY WARNING DIALOG
    if (store.warning) {

        console.log(from)
        console.log(to)

        store.exit = true
        return false

    } else {
        return true
    }

})


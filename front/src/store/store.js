// store.js
import { reactive } from 'vue'
import entities from '../assets/data/entities.json'
import items from '../assets/data/items.json'
// import events from '../assets/data/events.json'
import users from '../assets/data/users.json'

export const store = reactive({
    dev: true,
    session: { "user": "Test user" },
    entities: entities,
    items: items,
    events: items.map((x) => (x.events)).flat(1),
    users: users,
    updateEvents() {
        this.events = this.items.map((x) => (x.events)).flat(1)

        // this.items.forEach((x) => )

    }
})
// store.js
import { reactive } from 'vue'
import entities from '../assets/data/entities.json'
import items from '../assets/data/items.json'
import events from '../assets/data/events.json'
import users from '../assets/data/users.json'

export const store = reactive({
    dev: false,
    session: { "user": null },
    valid: null,
    entities: entities,
    items: items,
    events: events, // items.map((x) => (x.events)).flat(1),
    documents: items.map((x) => (x.documents)).flat(1),
    attachements: items.map((x) => (x.attachements)).flat(1),
    users: users,
    updateEvents() {
        this.events = this.items.map((x) => (x.events)).flat(1)
        // this.items.forEach((x) => )
    },
    updateDocuments() {
        this.documents = this.items.map((x) => (x.documents)).flat(1)
    },
    updateAttachements() {
        this.attachements = this.items.map((x) => (x.attachements)).flat(1)
    }

})
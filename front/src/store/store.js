// store.js
import { reactive } from 'vue'
import { EntityTypes } from './entity-types.js'
import entities from '../assets/data/entities.json'
import items from '../assets/data/items.json'
import events from '../assets/data/events.json'
import users from '../assets/data/users.json'
import { sleep } from '../store/shared.js'
// import { router } from '../router.js'

export const didi = reactive({
    entityTypes: null,
    async get() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/entity-type/', {
                method: 'GET',
                redirect: 'follow'
            })
            this.entityTypes = await response.json()

        } catch (error) {
            console.error(error)
        }
    },
})

export const store = reactive({
    dev: true,
    session: { "user": null },
    valid: null,
    loading: false,
    warning: false,
    exit: false,
    navigation: { "from": null, "to": null },
    entityTypes: null,
    entities: entities,
    entity: null,
    itemTypes: null,
    items: items,
    events: events, // items.map((x) => (x.events)).flat(1),
    documents: items.map((x) => (x.documents)).flat(1),
    attachements: items.map((x) => (x.attachements)).flat(1),
    users: users,
    async getItems() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/item/', {
                method: 'GET',
                redirect: 'follow'
            })
            this.items = await response.json()

        } catch (error) {
            console.error(error)
        }
    },
    async getItemTypes() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/item-type/', {
                method: 'GET',
                redirect: 'follow'
            })
            this.itemTypes = await response.json()

        } catch (error) {
            console.error(error)
        }
    },
    async getEntity(id) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}`, {
                method: 'GET',
                redirect: 'follow'
            })
            this.entity = await response.json()
            console.log(this.entity)

        } catch (error) {
            console.error(error)
        }
    },
    async getEntities() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/entity/', {
                method: 'GET',
                redirect: 'follow'
            })
            this.entities = await response.json()

        } catch (error) {
            console.error(error)
        }
    },
    async getEntityTypes() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/entity-type/', {
                method: 'GET',
                redirect: 'follow'
            })
            this.entityTypes = await response.json()

        } catch (error) {
            console.error(error)
        }
    },
    async getEvents() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/event/', {
                method: 'GET',
                redirect: 'follow'
            })
            this.events = await response.json()

        } catch (error) {
            console.error(error)
        }
    },
    async getEventTypes() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/event-type/', {
                method: 'GET',
                redirect: 'follow'
            })
            this.eventTypes = await response.json()

        } catch (error) {
            console.error(error)
        }
    },
    async getTemplates() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/template/', {
                method: 'GET',
                redirect: 'follow'
            })
            this.templates = await response.json()

        } catch (error) {
            console.error(error)
        }
    },
    updateEvents() {
        this.events = this.items.map((x) => (x.events)).flat(1)
        // this.items.forEach((x) => )
    },
    updateDocuments() {
        this.documents = this.items.map((x) => (x.documents)).flat(1)
    },
    updateAttachements() {
        this.attachements = this.items.map((x) => (x.attachements)).flat(1)
    },


})
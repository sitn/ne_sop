// store.js
import { reactive } from 'vue'
import { EntityTypes } from './entity-types.js'
import entities from '../assets/data/entities.json'
import items from '../assets/data/items.json'
import events from '../assets/data/events.json'
import users from '../assets/data/users.json'
import { sleep } from '../store/shared.js'
// import { router } from '../router.js'

export const store = reactive({
    dev: true,
    session: { "user": null },
    valid: null,
    loading: true,
    warning: false,
    exit: false,
    navigation: { "from": null, "to": null },
    entityTypes: null,
    entities: [], // entities,
    entity: null,
    itemTypes: null,
    items: items,
    events: [], // events, // items.map((x) => (x.events)).flat(1),
    documents: items.map((x) => (x.documents)).flat(1),
    attachements: items.map((x) => (x.attachements)).flat(1),
    users: users,
    /* ITEMS */
    async getItems() {
        try {

            this.loading = true
            const response = await fetch('http://127.0.0.1:8000/api/item/', {
                method: 'GET',
                redirect: 'follow'
            })
            this.items = await response.json()
            this.loading = false

        } catch (error) {
            console.error(error)
        }
    },
    async getItemTypes() {
        try {

            this.loading = true
            const response = await fetch('http://127.0.0.1:8000/api/item-type/', {
                method: 'GET',
                redirect: 'follow'
            })
            this.itemTypes = await response.json()
            this.loading = false

        } catch (error) {
            console.error(error)
        }
    },
    async setReady(obj, val) {
        this.loading = val
        console.log(`loading: ${this.loading}`)
    },
    /* ENTITIES */
    async addEntity(data) {
        try {

            /*
            data = {
                "name": "Didi 9",
                "type_id": 2,
                "type": "sfdsf",
                "description": "",
                "street": "Château Rue de la Collégiale 12",
                "city": "Neuchâtel",
                "postalcode": "2002",
                "region": "Neuchâtel",
                "country": "Suisse",
                "website": "https://www.ne.ch/autorites/DDTE/SDTE/",
                "email": "Secretariat.DDTE@ne.ch",
                "telephone": "+41 32 889 67 00",
                "valid": true
            }
            */

            const response = await fetch(`http://127.0.0.1:8000/api/entity/`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })
                .then(response => response.json())
                .then(result => console.log(result))
                .catch(error => console.log('error', error))

            // res = await response.json()
            // console.log(res)

            // this.entities = await response.json()
            // console.log(this.entities)

        } catch (error) {
            console.error(error)
        }

    },
    async updateEntity(id, data) {
        console.log('store.updateEntity()')
        console.log(data)
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}/`, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })
                .then(response => response.json())
                .then(result => {
                    console.log('result')
                    console.log(result)
                })
                .catch(error => console.log('error', error))

        } catch (error) {
            console.error(error)
        }

    },
    async getEntity(id) {
        try {

            this.loading = true
            console.log(`loading: ${this.loading}`)
            const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}`, {
                method: 'GET',
                redirect: 'follow'
            })
            this.entity = await response.json()
            console.log(this.entity)
            // await this.setReady(this.entity, false)
            this.loading = false
            console.log(`loading: ${this.loading}`)
            // 

        } catch (error) {
            console.error(error)
        }
    },
    async deleteEntity(id) {
        try {

            this.loading = true
            console.log(`loading: ${this.loading}`)
            const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}`, {
                method: 'DELETE',
                redirect: 'follow'
            })
                .then(response => response.json())
                .then(result => {
                    console.log(result)
                    this.entities = this.entities.filter((x) => (x.id !== id))
                })
                .catch(error => console.log('error', error))

            this.loading = false
            console.log(`loading: ${this.loading}`)

        } catch (error) {
            console.error(error)
        }
    },
    // query parameters, number of results, page, filters
    // API - GET ALL RECORDS
    async getEntities(name = "", page = 1, size = 10) {
        try {

            this.loading = false
            const response = await fetch(`http://127.0.0.1:8000/api/entity?page=${page}&size=${size}&name=${name}`, {
                method: 'GET',
                redirect: 'follow'
            })
            this.entities = await response.json()
                .then(
                    this.loading = false
                )
            console.log(this.entities)

        } catch (error) {
            console.error(error)
        }
    },
    async getEntities2() {

        let h = new Headers()
        h.append('Content-Type', 'application/json')

        let url = `http://127.0.0.1:8000/api/entity/`
        let req = new Request(url, {
            method: 'GET',
            headers: h
        })

        fetch(`http://127.0.0.1:8000/api/entity/`)
            .then(res => res.json())
            .then(data => {
                this.entities = data
                this.loading = false
            })
            .catch(error => console.warn('error', error))

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
    /* EVENTS */
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
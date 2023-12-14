// store.js
import { reactive } from 'vue'
import users from '../assets/data/users.json'
import { sleep } from '../store/shared.js'

export const store = reactive({
    dev: true,
    loading: true,
    warning: false,
    exit: false,
    navigation: { "from": null, "to": null },
    users: users,

    // GET LIST OF ENTITIES
    async getEntities(search = "", type = [], page = 1, size = 10, sortBy = "", descending = "false") {
        try {

            // await sleep(1300)
            const response = await fetch(`http://127.0.0.1:8000/api/entity?page=${page}&size=${size}&search=${search}&type=${type}&sortby=${sortBy}&descending=${descending}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET ENTITY DETAILS
    async getEntity(id) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // UPDATE ENTITY
    async updateEntity(id, data) {
        try {
            // await sleep(1000)
            const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}/`, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

        } catch (error) {
            console.error(error)
        }

    },

    // ADD ENTITY
    async addEntity(data) {
        try {

            // await sleep(1000)
            const response = await fetch(`http://127.0.0.1:8000/api/entity/`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

        } catch (error) {
            console.error(error)
        }

    },

    // DELETE ENTITY
    async deleteEntity(id) {
        try {

            // await sleep(1000)
            const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}`, {
                method: 'DELETE',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET ENTITY TYPES
    async getEntityTypes() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/entity-type/', {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET LIST OF ITEMS
    async getItems(search = "", page = 1, size = 10, sortBy = "", descending = "false") {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/item?page=${page}&size=${size}&sortby=${sortBy}&descending=${descending}&search=${search}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET ITEM DETAILS
    async getItem(id) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/new-item/${id}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // UPDATE ITEM
    async updateItem(id, data) {
        try {
            // await sleep(1000)
            const response = await fetch(`http://127.0.0.1:8000/api/new-item/${id}/`, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

        } catch (error) {
            console.error(error)
        }

    },

    // ADD NEW ITEM
    async addItem(data) {
        try {

            // http://127.0.0.1:8000/api/item/
            // await sleep(1000)
            const response = await fetch(`http://127.0.0.1:8000/api/new-item/`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

        } catch (error) {
            console.error(error)
        }

    },

    // DELETE ITEM
    async deleteItem(id) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/item/${id}`, {
                method: 'DELETE',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET ITEM TYPES
    async getItemTypes() {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/item-type`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET ITEM STATUS
    async getItemStatus() {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/item-status`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },


    // GET LIST OF EVENTS
    async getEvents(search = "", item = "", page = 1, size = 10, sortBy = "", descending = "false") {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/event?page=${page}&size=${size}&sortby=${sortBy}&descending=${descending}&item=${item}&search=${search}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET EVENT DETAILS
    async getEvent(id) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/event/${id}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // UPDATE EVENT
    async updateEvent(id, data) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/event/${id}/`, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

        } catch (error) {
            console.error(error)
        }

    },

    // ADD NEW EVENT
    async addEvent(data) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/event/`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await response.json()

        } catch (error) {
            console.error(error)
        }

    },

    // DELETE EVENT
    async deleteEvent(id) {
        try {

            const response = await fetch(`http://127.0.0.1:8000/api/event/${id}`, {
                method: 'DELETE',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET EVENT TYPES
    async getEventTypes() {
        try {

            const response = await fetch('http://127.0.0.1:8000/api/event-type/', {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

})
// store.jsoldFormData
import { ref } from 'vue'
import { reactive } from 'vue'
import users from '../assets/data/users.json'
const host = import.meta.env.VITE_API_URL
const dev = import.meta.env.VITE_DEV.toLowerCase() === 'true'

export const store = reactive({
    dev: dev,
    loading: true,
    warning: false,
    exit: false,
    navigation: { "from": null, "to": null },
    oldFormData: null,
    newFormData: null,

    entity: { old: null, new: null },
    item: { old: null, new: null },
    document: { old: null, new: null },
    event: { old: null, new: null },

    documents: [],
    users: users,
    user: null,
    drawer: ref(false),

    // UPDATE UNSAVED CHANGES WARNING PANEL
    updateWarning(obj) {

        let oldDataString = obj.old
            .replaceAll(/"id":\d+,/gi, '')
            .replaceAll(/"uuid":"[a-z0-9-]+",/gi, '')
            .replaceAll(/"created":"[0-9.:\s]+",/gi, '')
            .replaceAll(/"template_id":\d+,/gi, '')
            .replaceAll(/"author_id":\d+,/gi, '')
            .replaceAll(/"author":"[^"]+",/gi, '')

        let newDataString = obj.new
            .replaceAll(/"id":\d+,/gi, '')
            .replaceAll(/"uuid":"[a-z0-9-]+",/gi, '')
            .replaceAll(/"created":"[0-9.:\s]+",/gi, '')
            .replaceAll(/"template_id":\d+,/gi, '')
            .replaceAll(/"author_id":\d+,/gi, '')
            .replaceAll(/"author":"[^"]+",/gi, '')

        /*    
        console.log('oldDataString')
        console.log(oldDataString)
        console.log('newDataString')
        console.log(newDataString)
        */

        if (oldDataString !== newDataString) {
            this.warning = true
            // console.log('NOT EQUAL')
        } else {
            this.warning = false
            // console.log('EQUAL')
        }

    },

    // GET CURRENT USER
    async getCurrentUser() {
        try {

            // await sleep(1300)
            const response = await fetch(`${host}/api/current-user/`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET LIST OF SERVICES
    /*
    async getServices(search = "", page = 1, size = 10, sortBy = "", descending = "false") {
        try {

            const response = await fetch(`${host}/api/service?page=${page}&size=${size}&search=${search}&sortby=${sortBy}&descending=${descending}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },
    */

    // GET LIST OF ENTITIES
    async getEntities(search = "", type = [], service = "", page = 1, size = 10, sortBy = "", descending = "false") {
        try {

            // await sleep(1300)
            const response = await fetch(`${host}/api/entity?page=${page}&size=${size}&search=${search}&type=${type}&service=${service}&sortby=${sortBy}&descending=${descending}`, {
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

            const response = await fetch(`${host}/api/entity/${id}`, {
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
            const response = await fetch(`${host}/api/entity/${id}/`, {
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
            const response = await fetch(`${host}/api/entity/`, {
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
            const response = await fetch(`${host}/api/entity/${id}`, {
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

            const response = await fetch(`${host}/api/entity-type/`, {
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

            const response = await fetch(`${host}/api/item?page=${page}&size=${size}&sortby=${sortBy}&descending=${descending}&search=${search}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    // GET ITEM DETAILS
    async getItem(id, summary = false) {
        try {

            let url = ""
            if (summary) {
                url = `${host}/api/item-summary/${id}`
            } else {
                url = `${host}/api/item/${id}`
            }

            const response = await fetch(url, {

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
            let documents = data.documents
            let data_nodocs = Object.assign({}, data)
            // let data_nodocs = JSON.parse(JSON.stringify(data))
            delete data_nodocs.documents

            const response = await fetch(`${host}/api/item/${id}/`, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data_nodocs),
                redirect: 'follow',
            })

            await response.json()
            await this.prepareAddDocuments(documents, data_nodocs)

            return await this.getItem(id)

        } catch (error) {
            console.error(error)
        }

    },


    // ADD NEW ITEM
    async addItem(data) {
        let documents = data.documents
        let data_nodocs = Object.assign({}, data)
        // let data_nodocs = JSON.parse(JSON.stringify(data))
        delete data_nodocs.documents

        try {
            const response = await fetch(`${host}/api/item/`, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data_nodocs),
                redirect: 'follow',
            })

            let tmp = await response.json()

            await this.prepareAddDocuments(documents, tmp)

            return await this.getItem(tmp.id)

        } catch (error) {
            console.error(error)
        }
    },

    // DELETE ITEM
    async deleteItem(id) {
        try {

            const response = await fetch(`${host}/api/item/${id}`, {
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

            const response = await fetch(`${host}/api/item-type`, {
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

            const response = await fetch(`${host}/api/item-status`, {
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

            const response = await fetch(`${host}/api/event?page=${page}&size=${size}&sortby=${sortBy}&descending=${descending}&item=${item}&search=${search}`, {
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

            const response = await fetch(`${host}/api/event/${id}`, {
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

            const response = await fetch(`${host}/api/event/${id}/`, {
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

            const response = await fetch(`${host}/api/event/`, {
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

            const response = await fetch(`${host}/api/event/${id}`, {
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

            const response = await fetch(`${host}/api/event-type/`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },


    // GET LIST OF TEMPLATES FOR THIS ITEM TYPE
    async getTemplatesByItemType(type_id) {
        try {

            const response = await fetch(`${host}/api/template-types?itemtype_id=${type_id}`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },


    // PREPARE UPLOAD DOCUMENTS
    async prepareAddDocuments(documents, item) {
        documents = documents.filter(x => x.id === undefined)

        let promises = []
        documents.forEach(x => {
            let formData = new FormData()
            formData.append('file', x.file)
            formData.append('filename', x.filename)
            formData.append('created', x.created)
            formData.append('template', x.template)
            formData.append('template_id', x.template_id)
            formData.append('size', x.size)
            formData.append('note', x.note)
            formData.append('author_id', x.author_id)
            formData.append('item', item.id)

            promises.push(store.addDocument(formData, x.filename))
        })

        return await Promise.all(promises)
            .catch(error => console.log('error', error))
    },


    // UPLOAD DOCUMENT
    async addDocument(formData) {
        try {

            const response = await fetch(`${host}/api/document/`, {
                method: 'POST',
                body: formData,
                redirect: 'follow'
            })
            await response.json()

        } catch (error) {
            console.error(error)
        }
    },


    // DOWNLOAD DOCUMENT BY ID
    async downloadDocument(document_id) {
        try {

            window.open(
                `${host}/api/document/${document_id}/`,
                {
                    method: 'GET',
                    redirect: 'follow'
                }
            )

        } catch (error) {
            console.error(error)
        }
    },


    // DELETE DOCUMENT BY ID
    async deleteDocument(document_id) {
        try {

            const response = await fetch(`${host}/api/document/${document_id}/`,
                {
                    method: 'DELETE',
                    redirect: 'follow'
                }
            )

            await response.json()


        } catch (error) {
            console.error(error)
        }
    },

    // GET ITEM STATISTICS
    async getNumberOfItemsDepositedPerYear() {

        try {
            const response = await fetch(`${host}/api/item-type-statistics-deposited`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    async getNumberOfItemsTreatedPerYear() {

        try {
            const response = await fetch(`${host}/api/item-type-statistics-treated`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    async getNumberOfServiceItemsPerYear() {

        try {
            const response = await fetch(`${host}/api/service-statistics`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    async getStatisticItemStatus() {

        try {
            const response = await fetch(`${host}/api/item-status-statistics`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

    async getStatisticItemUrgentWritten() {

        try {
            const response = await fetch(`${host}/api/item-urgent-written-statistics`, {
                method: 'GET',
                redirect: 'follow'
            })
            return await response.json()

        } catch (error) {
            console.error(error)
        }
    },

})
// store.jsoldFormData
import { ref } from 'vue'
import { reactive } from 'vue'
// import users from '../assets/data/users.json'
const host = import.meta.env.VITE_API_URL
const dev = import.meta.env.VITE_DEV.toLowerCase() === 'true'

export const store = reactive({
    dev: dev, // enable/disable development mode
    loading: true,
    // warning: false,
    // exit: false,
    navigation: { "from": null, "to": null },
    dialogs: { warning: false, exit: false, error: false },
    errormessage: '',
    drawer: ref(false),

    // filters: { items: null, entities: null },
    entity: { old: null, new: null },
    item: { old: null, new: null },
    document: { old: null, new: null },
    event: { old: null, new: null },
    documents: [],
    // users: users,
    user: null,

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
            this.dialogs.warning = true
            // console.log('NOT EQUAL')
        } else {
            this.warning = false
            this.dialogs.warning = false
            // console.log('EQUAL')
        }

    },

    // HANDLE HTTP FETCH RESPONSE
    async handleResponse(response) {

        let payload = await response.json()

        // handle server errors
        if (response.ok) {

            return payload

        } else {

            this.dialogs.error = true
            this.errormessage = payload
            return
            // throw new Error('Ceci est une erreur')

        }

    },

    // GET CURRENT USER
    async getCurrentUser() {
        try {

            // await sleep(1300)
            const query = new URL(`${host}/api/current-user/`)
            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

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
    async getEntities(filter = {}, page = 1, size = 10, sortBy = "", descending = "false") {
        try {

            const query = new URL(`${host}/api/entity?`)
            query.searchParams.append("page", page)
            query.searchParams.append("size", size)
            query.searchParams.append("sortBy", sortBy)
            query.searchParams.append("descending", descending)

            for (const [key, value] of Object.entries(filter)) {
                if (value) {
                    // console.log(`${key}: ${value}`)
                    query.searchParams.append(key, value)
                }
            }
            // const query = `${host}/api/entity?page=${page}&size=${size}&search=${filter.search}&type=${filter.type}&service=${filter.service}&sortby=${sortBy}&descending=${descending}`

            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            console.error(error)
        }
    },

    // GET ENTITY DETAILS
    async getEntity(id) {
        try {

            const query = new URL(`${host}/api/entity/${id}`)
            const response = await fetch(query, {
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
            const query = new URL(`${host}/api/entity/${id}/`)
            const response = await fetch(query, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await this.handleResponse(response)

        } catch (error) {
            console.error(error)
        }

    },

    // ADD ENTITY
    async addEntity(data) {

        try {

            // await sleep(1000)
            const query = new URL(`${host}/api/entity/`)
            const response = await fetch(query, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }

    },

    // DEACTIVATE ENTITY
    async deactivateEntity(id) {
        try {

            // await sleep(1000)
            const response = await fetch(`${host}/api/entity-deactivate/${id}/`, {
                method: 'PUT',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    // // DELETE ENTITY
    // async deleteEntity(id) {
    //     try {

    //         // await sleep(1000)
    //         const response = await fetch(`${host}/api/entity/${id}`, {
    //             method: 'DELETE',
    //             redirect: 'follow'
    //         })
    //         return await response.json()

    //     } catch (error) {
    //         console.error(error)
    //     }
    // },

    // GET ENTITY TYPES
    async getEntityTypes() {
        try {

            const query = new URL(`${host}/api/entity-type/`)
            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    // GET LIST OF ITEMS
    // async getItems(search = "", page = 1, size = 10, sortBy = "", descending = "false") {
    async getItems(filter = {}, page = 1, size = 10, sortBy = "", descending = "false") {
        try {

            // console.log('getItems')
            // console.log(filter)

            const query = new URL(`${host}/api/item?`)
            query.searchParams.append("page", page)
            query.searchParams.append("size", size)
            query.searchParams.append("sortBy", sortBy)
            query.searchParams.append("descending", descending)

            for (const [key, value] of Object.entries(filter)) {
                if (value) {
                    // console.log(`${key}: ${value}`)
                    query.searchParams.append(key, value)
                }
            }

            // let query = `${host}/api/item?page=${page}&size=${size}&sortby=${sortBy}&descending=${descending}&search=${filter.search}&number=${filter.number}&title=${filter.title}&status=${filter.status.join()}&type=${filter.type.join()}`
            // console.log(query)

            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    // GET ITEM DETAILS
    async getItem(id, summary = false) {
        try {
            let query
            if (summary) {
                query = new URL(`${host}/api/item-summary/${id}`)
            } else {
                query = new URL(`${host}/api/item/${id}`)
            }

            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })
            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
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

            const query = new URL(`${host}/api/item/${id}/`)
            const response = await fetch(query, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data_nodocs),
                redirect: 'follow',
            })

            // await response.json()
            await this.handleResponse(response)
            await this.prepareAddDocuments(documents, data_nodocs)

            return await this.getItem(id)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
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
            const query = new URL(`${host}/api/item/`)
            const response = await fetch(query, {
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
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    // DELETE ITEM
    async deleteItem(id) {
        try {
            const query = new URL(`${host}/api/item/${id}`)
            const response = await fetch(query, {
                method: 'DELETE',
                redirect: 'follow'
            })
            return await this.handleResponse(response)

        } catch (error) {
            console.error(error)
        }
    },

    // GET ITEM TYPES
    async getItemTypes() {
        try {
            const query = new URL(`${host}/api/item-type`)
            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    // GET ITEM STATUS
    async getItemStatus() {
        try {
            const query = new URL(`${host}/api/item-status`)
            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },


    // GET LIST OF EVENTS
    // async getEvents(search = "", item = "", page = 1, size = 10, sortBy = "", descending = "false") {
    async getEvents(filter = {}, page = 1, size = 10, sortBy = "", descending = "false") {
        try {

            const query = new URL(`${host}/api/event?`)
            query.searchParams.append("page", page)
            query.searchParams.append("size", size)
            query.searchParams.append("sortBy", sortBy)
            query.searchParams.append("descending", descending)

            for (const [key, value] of Object.entries(filter)) {
                if (value) {
                    // console.log(`${key}: ${value}`)
                    query.searchParams.append(key, value)
                }
            }

            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    // GET EVENT DETAILS
    async getEvent(id) {
        try {
            const query = new URL(`${host}/api/event/${id}`)
            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            console.error(error)
        }
    },

    // UPDATE EVENT
    async updateEvent(id, data) {
        try {
            const query = new URL(`${host}/api/event/${id}/`)
            const response = await fetch(query, {
                method: 'PUT',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }

    },

    // ADD NEW EVENT
    async addEvent(data) {
        try {

            const query = new URL(`${host}/api/event/`)
            const response = await fetch(query, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
                redirect: 'follow',
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }

    },

    // DELETE EVENT
    async deleteEvent(id) {
        try {

            const query = new URL(`${host}/api/event/${id}`)
            const response = await fetch(query, {
                method: 'DELETE',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    // GET EVENT TYPES
    async getEventTypes() {
        try {

            const query = new URL(`${host}/api/event-type/`)
            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },


    // GET LIST OF TEMPLATES FOR THIS ITEM TYPE
    async getTemplatesByItemType(type_id) {
        try {
            const query = new URL(`${host}/api/template-types`)
            query.searchParams.append("itemtype_id", type_id)

            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
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
            formData.append('item', item.id)

            promises.push(store.addDocument(formData, x.filename))
        })

        return await Promise.all(promises)
            .catch(error => console.log('error', error))
    },


    // UPLOAD DOCUMENT
    async addDocument(formData) {
        try {

            const query = new URL(`${host}/api/document/`)
            const response = await fetch(query, {
                method: 'POST',
                body: formData,
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
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
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },


    // DELETE DOCUMENT BY ID
    async deleteDocument(document_id) {
        try {

            const query = new URL(`${host}/api/document/${document_id}/`)
            const response = await fetch(query,
                {
                    method: 'DELETE',
                    redirect: 'follow'
                }
            )

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    // GET ITEM STATISTICS
    async getNumberOfItemsDepositedPerYear() {

        try {
            const query = new URL(`${host}/api/item-type-statistics-deposited`)
            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    async getNumberOfItemsTreatedPerYear() {

        try {
            const query = new URL(`${host}/api/item-type-statistics-treated`)
            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    async getNumberOfServiceItemsPerYear() {

        try {
            const query = new URL(`${host}/api/service-statistics`)
            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    async getStatisticItemStatus() {

        try {
            const query = new URL(`${host}/api/item-status-statistics`)
            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

    async getStatisticItemUrgentWritten() {

        try {
            const query = new URL(`${host}/api/item-urgent-written-statistics`)
            const response = await fetch(query, {
                method: 'GET',
                redirect: 'follow'
            })

            return await this.handleResponse(response)

        } catch (error) {
            // handle network and CORS errors (fetch promise rejected)
            this.dialogs.error = true
            console.error(error)
        }
    },

})
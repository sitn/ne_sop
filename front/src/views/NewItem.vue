<template>
    <div class="">

        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Objets parlementaires" to="/items" />
                    <q-breadcrumbs-el label="Nouvel objet" />
                </q-breadcrumbs>
            </div>

            <!-- FORM -->
            <ItemForm v-model="item" :edit="edit"></ItemForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @edit-event="setEditMode"></FloatingButtons>

        </q-layout>

    </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import documents from '../assets/data/documents.json'
import itemTypes from '../assets/data/item-types.json'
import ItemForm from "../components/ItemForm.vue"
import FloatingButtons from "../components/FloatingButtons.vue"

const subset = ["Parlementaire", "Groupe parlementaire", "Autre"]
const authors = store.entities.filter(e => subset.includes(e.type))

export default {
    name: 'NewItem',
    components: { ItemForm, FloatingButtons },
    props: { 'model': Object },
    emits: [],
    setup() {
        return {}
    },

    data() {
        return {
            store,
            edit: true,
            wait: false,
            item: {
                "id": uuidv4(),
                "number": "",
                "type": "",
                "title": "",
                "status": "",
                "content": "",
                "urgent": false,
                "writtenResponse": false,
                "oralResponse": false,
                "fight": false,
                "author": "",
                "response": "",
                "comment": "",
                "request": "",
                "documents": [],
                "attachements": [],
                "servicesAlt": [],
                "services": {
                    "lead": null,
                    "support": []
                },
                "events": [],
                "valid": false
            },
            itemTypes: itemTypes,
            authorOptions: authors, //entities.filter(e => e.type.includes("Parlementaire","Groupe politique","Commission parlementaire instituée")),
            addEntityDialog: false,
            serviceOptions: store.entities.filter((e) => (e.type === "Service de l'état"))
        }
    },
    computed: {
        actionButtons() {
            return {
                save: this.item.valid ? 'active' : 'disable',
                deletion: 'none'
            }
        }
    },
    beforeCreate() {
    },
    created() {
    },
    mounted() {
    },
    methods: {
        async save(redirectTo) {
            // TODO - POST NEW RECORD TO DATABASE
            console.log(`${this.$options.name}.vue | save()`)
            this.wait = true
            await sleep(Math.random() * 1300)
            store.items.push(this.item)
            this.wait = false

            if (redirectTo !== null) {
                this.$router.push({ path: redirectTo })
            }

            // this.$router.push({ name: 'ItemsList' })
        },
        setEditMode(val) {
            console.log(`${this.$options.name}.vue | setEditMode(${val})`)
            this.edit = val
        },
        addEntity() {
            console.log('Add new entity')
            this.addEntityDialog = true
        },
        addNewEntity(val) {

            console.log('Item.vue | addNewEntity()')
            console.log(val)

            let newOption = {
                "id": uuidv4(),
                "name": val.name,
                "type": val.type,
                "description": val.description,
                "street": val.street,
                "city": val.city,
                "postalCode": val.postalCode,
                "region": val.region,
                "country": val.country,
                "website": val.website,
                "email": val.email,
                "telephone": val.telephone,
            }

            console.log('newOption')
            console.log(newOption)

            if (!this.authorOptions.map((x) => (x.name)).includes(newOption.name)) {
                // entities.push(newOption)
                this.store.entities.push(newOption)
                // this.authorOptions.push(val)
                this.item.author = newOption
                // POST NEW ENTITY TO DATABASE

            }

        },
        filterFn(val, update, abort) {
            update(() => {
                const needle = val.toLowerCase()
                this.authorOptions = authors.filter(v => v.name.toLowerCase().indexOf(needle) > -1)
            })
        }
    }
}
</script>

<style scoped></style>
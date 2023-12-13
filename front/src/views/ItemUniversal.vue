<template>
    <div class="" v-if="!store.loading">
        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Objets parlementaires (UNIVERSAL)" to="/items" />
                    <q-breadcrumbs-el :label="item.number.toString()" />
                </q-breadcrumbs>
            </div>

            <!-- FORM -->
            <ItemForm v-model="item" :mode="mode" :edit="edit" ref="ItemForm"></ItemForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="false" :wait="wait" :buttons="actionButtons" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode"></FloatingButtons>

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

            <!-- ADD NEW ENTITY DIALOG -->
            <q-dialog v-model="addEntityDialog">
                <NewEntityDialog @addNewEntity="addNewEntity"></NewEntityDialog>
            </q-dialog>

        </q-layout>

    </div>
</template>

<script>
import { store } from '../store/store.js'
import ItemForm from "../components/ItemForm.vue"
import FloatingButtons from "../components/FloatingButtons.vue"
import NewEntityDialog from "./NewEntityDialog.vue"
import DeleteDialog from '../components/DeleteDialog.vue'

export default {
    name: 'Item',
    components: { ItemForm, FloatingButtons, NewEntityDialog, DeleteDialog },
    props: {},
    emits: [],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            dialog: { deletion: false },
            mode: "update",
            edit: false,
            wait: false,
            item: {
                "number": "",
                "type": "",
                "title": "",
                "status": "",
                "description": "",
                "urgent": false,
                "writtenresponse": false,
                "oralresponse": false,
                /* "fight": false, */
                "author": null,
                "lead": null,
                "support": [],
                "events": [],
                "response": "",
                "comment": "",
                "request": "",
                "documents": [],
                "attachements": [],
                "valid": false
            },
            index: store.items.findIndex((e) => (e.id === this.$route.params.id)),
            addEntityDialog: false,
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
    async created() {

        console.log(this.$route.params)
        console.log(`this.$route.params.id: ${this.$route.params.id}`)
        if (this.$route.params.hasOwnProperty('id')) {
            this.store.loading = true
            this.item = await store.getItem(this.$route.params.id)
            this.store.loading = false
        }
        this.store.loading = false

        /*
        this.store.loading = true
        this.item = await store.getItem(this.$route.params.id)

        this.store.loading = false

        console.log(`id: ${this.$route.params.id}`)
        console.log(store.items)
        console.log('this.item')
        console.log(this.item)
        */

        // store.saveButton = true
        // this.item = Object.assign({}, store.items[0])
        //this.item = Object.assign({}, store.items.find((e) => (e.id === this.$route.params.id)))

        // this.item = Object.assign({}, store.items.find((e) => (e.id === 1)))

    },
    methods: {
        async save() {

            console.log(`${this.$options.name}.vue | save()`)

            this.wait = true
            if (this.item.id) {
                this.item = await store.updateItem(this.item.id, this.item)
            } else {
                this.item = await store.addItem(this.item)
            }
            this.wait = false

            // TODO: POST RECORD TO DATABASE
            /*
            let message = await store.updateItem(this.$route.params.id, this.item)
            if (message) {
                this.wait = false
                console.log(message)

                if (redirectTo !== null) {
                    this.$router.push({ path: redirectTo })
                }
            }
            */

            /*
            console.log(`${this.$options.name}.vue | save()`)
            this.wait = true
            await sleep(Math.random() * 1300)
            let ind = store.items.findIndex((e) => (e.id === this.$route.params.id))
            store.items[ind] = Object.assign({}, this.item)
            this.wait = false

            if (redirectTo !== null) {
                this.$router.push({ path: redirectTo })
            }
            */

        },
        handleDeletion() {
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: DELETE RECORD IN DATABASE
            console.log(`${this.$options.name}.vue | remove()`)
            store.items.splice(this.index, 1)
            this.$router.push({ name: 'ItemsList' })
        },
        setEditMode(val) {
            console.log(`${this.$options.name}.vue | setEditMode(${val})`)
            this.edit = val
            // this.$refs.ItemForm.validateForm()
        },
        addEntity() {
            console.log('Item.vue | Add new entity')
            this.addEntityDialog = true
        },
        async addNewEntity(val) {

            console.log(`${this.$options.name} | addNewEntity()`)

            let newEntity = await store.addEntity(val)
            this.authorOptions.unshift(newEntity)
            console.log(this.authorOptions)
            // this.authorOptions = await store.getEntities("", [2, 3], 1, 50)
            this.item.author = newEntity.id

        },
        /*
        filterFn(val, update, abort) {
            update(() => {
                // TODO - GET RECORDS FROM DATABASE
                const needle = val.toLowerCase()
                // this.authorOptions = entities.filter((v) => v.name.toLowerCase().indexOf(needle) > -1)

                this.authorOptions = store.entities.filter((e) => subset.includes(e.type)).filter((v) => v.name.toLowerCase().indexOf(needle) > -1)

            })
        }
        */

    }
}
</script>

<style scoped></style>
<template>
    <div class="" v-if="!store.loading">
        <div v-if="(item && item.id) || $route.name === 'NewItem'">

            <q-layout>

                <!-- BREADCRUMBS NAVIGATION -->
                <div class="q-pa-sm q-gutter-sm">
                    <q-breadcrumbs style="font-size: 16px">
                        <q-breadcrumbs-el label="Objets parlementaires" to="/items" />
                        <q-breadcrumbs-el :label="item.number.toString()" />
                    </q-breadcrumbs>
                </div>

                <!-- FORM -->
                <ItemForm v-model="item" :edit="edit" ref="ItemForm"></ItemForm>
                <!-- <ItemForm v-model="item" :mode="mode" :edit="edit" ref="ItemForm"></ItemForm> -->

                <!-- FLOATING ACTION BUTTONS -->
                <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode"></FloatingButtons>

                <!-- DELETE DIALOG -->
                <!-- <DeleteDialog v-model="dialog.deletion" @delete-event="remove" /> -->

                <!-- ADD NEW ENTITY DIALOG -->
                <!--
                <q-dialog v-model="addEntityDialog">
                    <NewEntityDialog @addNewEntity="addNewEntity"></NewEntityDialog>
                </q-dialog> 
                -->

            </q-layout>
        </div>

        <div v-else>
            <NotFound></NotFound>
        </div>

    </div>
</template>

<script>
import { store } from '../store/store.js'
import NotFound from '../components/NotFound.vue'
import ItemForm from "../components/ItemForm.vue"
import FloatingButtons from "../components/FloatingButtons.vue"
import NewEntityDialog from "./NewEntityDialog.vue"
import DeleteDialog from '../components/DeleteDialog.vue'

export default {
    name: 'Item',
    components: { ItemForm, FloatingButtons, NewEntityDialog, DeleteDialog, NotFound },
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
            edit: false,
            wait: false,
            item: {},
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
    watch: {
        async $route(to, from) {

            if (to.name === "NewItem" && from.href !== to.href) {
                this.initialize_item()
                this.edit = true
                this.$router.push({ name: 'NewItem' })
            }
            if (this.$route.params.hasOwnProperty('id')) {
                this.store.loading = true
                this.item = await store.getItem(this.$route.params.id)
                this.store.loading = false
            }
            this.store.loading = false

        }
    },
    async created() {
        this.initialize_item()

        if (this.$route.name === "NewItem") {
            this.edit = true
        }

        // console.log(`this.$route.params.id: ${this.$route.params.id}`)
        if (this.$route.params.hasOwnProperty('id')) {
            this.store.loading = true
            this.item = await store.getItem(this.$route.params.id)
            this.store.loading = false
        }
        this.store.loading = false

    },
    methods: {
        initialize_item() {
            this.item = {
                "number": "",
                "type": null,
                "title": "",
                "status": "",
                "description": "",
                "urgent": false,
                "writtenresponse": false,
                "oralresponse": false,
                "autonotify": false,
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
            }
        },
        async save(redirectTo) {

            // console.log(`${this.$options.name}.vue | save()`)
            this.wait = true

            let response

            if (this.item.id) {
                // update existing record
                response = await store.updateItem(this.item.id, this.item)
            } else {
                // create a new record
                response = await store.addItem(this.item)
            }

            this.wait = false

            // update item
            if (response) {
                this.item = response
                store.item.old = JSON.stringify(this.item)
            }

            // redirection
            if (redirectTo !== null) {
                this.$router.push({ path: redirectTo })
            }

        },
        handleDeletion() {
            this.dialog.deletion = true
        },
        async remove() {
            // console.log(`${this.$options.name}.vue | remove()`)
            this.$router.push({ name: 'ItemsList' })
        },
        setEditMode(val) {
            // console.log(`${this.$options.name}.vue | setEditMode(${val})`)
            this.edit = val
        },
        addEntity() {
            this.addEntityDialog = true
        },
        async addNewEntity(val) {

            //console.log(`${this.$options.name} | addNewEntity()`)
            let newEntity = await store.addEntity(val)
            this.authorOptions.unshift(newEntity)
            // console.log(this.authorOptions)
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
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
            <ItemForm v-model="item" :mode="mode" :edit="edit"></ItemForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @edit-event="setEditMode"></FloatingButtons>

        </q-layout>

    </div>
</template>

<script>
import { store } from '../store/store.js'
import ItemForm from "../components/ItemForm.vue"
import FloatingButtons from "../components/FloatingButtons.vue"

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
            mode: "create",
            edit: true,
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

            // await sleep(Math.random() * 1300)
            // store.items.push(this.item)

            let message = await store.addItem(this.item)
            console.log(message)
            console.log(this.item)

            this.wait = false

            /*
            if (message) {
                this.$router.push({ name: 'ItemsList' })

                console.log(message)
                this.wait = false

       
            }
                */
            /*
        console.log(`redirectTo ${redirectTo}`)
        if (redirectTo !== null) {

            // this.$router.push({ path: redirectTo })
            // this.$router.push({ name: 'ItemsList' })
        }
        */

        },
        setEditMode(val) {
            console.log(`${this.$options.name}.vue | setEditMode(${val})`)
            this.edit = val
        },
        addEntity() {
            console.log('Add new entity')
            this.addEntityDialog = true
        },
    }
}
</script>

<style scoped></style>
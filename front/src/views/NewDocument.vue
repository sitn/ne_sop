<template>
    <div class="">

        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <!-- <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Calendrier" to="/itemlist" />
                    <q-breadcrumbs-el label="Nouvel événement" />
                </q-breadcrumbs>
            </div> -->

            <!--  <div>valid: {{ valid }}</div> -->
            <!--  <div>store.valid: {{ store.valid }}</div> -->

            <!-- FORM -->
            <DocumentForm v-model="document" :item_type="" :edit="edit" @validation-document="handleValidation"></DocumentForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-document="save" @edit-document="setEditMode"></FloatingButtons>

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-document="remove" />

        </q-layout>
    </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import FloatingButtons from "../components/FloatingButtons.vue"
import DeleteDialog from '../components/DeleteDialog.vue'
import DocumentForm from "../components/DocumentForm.vue"

export default {
    name: 'NewDocument',
    components: { FloatingButtons, DeleteDialog, DocumentForm },
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
            // actionButtons: {},
            edit: true,
            wait: false,
            valid: null,
            document: {
                // to be completed
                // to be completed
                // to be completed
                // to be completed
                // to be completed
                // to be completed
                // to be completed
                // to be completed
                // to be completed
                // to be completed
                // to be completed
                // to be completed
            },
            index: store.documents.findIndex((e) => (e.id === this.$route.params.id))
        }
    },
    computed: {
        actionButtons() {
            return {
                save: this.document.valid ? 'active' : 'disable',
                deletion: 'none'
            }
        }
    },
    created() {
    },
    mounted() {
        // this.valid ? this.actionButtons.save = 'active' : this.actionButtons.save = 'disable'
        // store.valid ? this.actionButtons.save = 'active' : this.actionButtons.save = 'disable'
    },

    methods: {
        async save(redirectTo) {

            // this.$refs.DocumentForm.validateForm() // VALIDATE FORM

            // TODO: POST RECORD TO DATABASE
            console.log(`${this.$options.name} | save()`)
            // console.log(`${this.$options.name} | this.$refs.DocumentForm.valid = ${this.$refs.DocumentForm.valid}`)

            this.wait = true
            await sleep(Math.random() * 1300)
            // store.items.filter((x) => (x.documents.findIndex(y => (y.id) === this.document.id))) = this.document
            // store.items.find((x) => (x.documents.findIndex((y) => (y.id === this.document.id))))
            store.items.forEach((x, j) => {
                let k = x.documents.findIndex(y => (y.id === this.document.id))
                if (k !== -1) {
                    store.items[j].documents[k] = Object.assign({}, this.document)
                    store.updateDocuments()
                }
            })

            store.documents.push(Object.assign({}, this.document))
            this.wait = false

            if (redirectTo !== null) {
                this.$router.push({ path: redirectTo })
            }

            // this.$router.push({ name: 'DocumentsList' })
        },
        handleValidation(val) {
            this.valid = val
            this.valid ? this.actionButtons.save = 'active' : this.actionButtons.save = 'disable'
            // store.valid ? this.actionButtons.save = 'active' : this.actionButtons.save = 'disable'
            console.log(`${this.$options.name} | handleValidation()`)
            // this.actionButtons.save = 'disable'
        },
        handleDeletion() {
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: DELETE RECORD IN DATABASE
            console.log(`${this.$options.name} | remove()`)
            store.documents.splice(this.index, 1)
            this.$router.push({ name: 'ItemList' })
        },
        setEditMode(val) {
            console.log(`${this.$options.name} | setEditMode(${val})`)
            this.edit = val
            // this.$refs.DocumentForm.validateForm()
        }
    }
}
</script>

<style scoped></style>
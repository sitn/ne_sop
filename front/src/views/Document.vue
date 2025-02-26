<template>
    <div class="" v-if="!store.loading">
        <div v-if="(document && document.id) || this.$route.name === 'NewDocument'">
            <q-layout>

                <!-- BREADCRUMBS NAVIGATION -->
                <div class="q-pa-sm q-gutter-sm">
                    <q-breadcrumbs style="font-size: 16px">
                        <q-breadcrumbs-el label="Documents" to="/documents" />
                        <q-breadcrumbs-el :label="document.title" />
                    </q-breadcrumbs>
                </div>

                <!-- FORM -->
                <DocumentForm v-model="document" :edit="edit"></DocumentForm>

                <!-- FLOATING ACTION BUTTONS -->
                <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode" v-if="store.user.is_manager"></FloatingButtons>

                <!-- DELETE DIALOG -->
                <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

            </q-layout>
        </div>

        <div v-else>
            <NotFound></NotFound>
        </div>
    </div>
</template>

<script>
import { store } from '../store/store.js'
import FloatingButtons from "../components/FloatingButtons.vue"
import DeleteDialog from '../components/DeleteDialog.vue'
import DocumentForm from "../components/DocumentForm.vue"
import NotFound from '../components/NotFound.vue'


export default {
    name: 'Document',
    components: { FloatingButtons, DeleteDialog, DocumentForm, NotFound },
    props: {},
    emits: [],
    data() {
        return {
            store,
            loaded: false,
            dialog: { deletion: false },
            edit: false,
            wait: false,
            document: {},
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
    watch: {
        async $route(to, from) {

            if (to.name === "NewDocument" && from.href !== to.href) {
                // this.initialize_document() // TODO
                this.edit = true
                this.$router.push({ name: 'NewDocument' })
            }

            if (this.$route.params.hasOwnProperty('id')) {
                this.store.loading = true
                this.document = await store.getDocument(this.$route.params.id)
                this.store.loading = false
            }
            this.store.loading = false

        }
    },
    async created() {
        // this.initialize_document()

        if (this.$route.name === "NewDocument") {
            this.edit = true
        }

        // console.log(`this.$route.params.id: ${this.$route.params.id}`)
        if (this.$route.params.hasOwnProperty('id')) {
            this.store.loading = true
            this.document = await store.getDocument(this.$route.params.id)
            this.store.loading = false
        }
        this.store.loading = false

    },
    methods: {
        initialize_document() {
            this.document = {
                "title": "",
                "reference": "",
                "type": "",
                "note": "",
                "filename": "",
            }
        },
        async save(redirectTo) {


            // console.log(`${this.$options.name}.vue | save()`)
            this.wait = true

            let response

            if (this.document.id) {
                // update existing record
                response = await store.updateDocument(this.document.uuid, this.document)
            } else {
                // create a new record
                response = await store.addDocument(this.document)
            }

            this.wait = false

            // update document
            if (response) {
                this.document = response
                store.document.old = JSON.stringify(this.document)
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
            this.$router.push({ name: 'DocumentsList' })
        },
        setEditMode(val) {
            // console.log(`${this.$options.name}.vue | setEditMode(${val})`)
            this.edit = val
        }
    },

}
</script>

<style scoped></style>
<template>
    <div class="row q-px-none q-my-md items-center">

        <!-- ADD NEW DOCUMENT BUTTON -->
        <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6">
            <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" @click="addDocument()" :disable="!edit">
                <q-tooltip class="bg-black">Ajouter un document</q-tooltip>
            </q-btn>
        </div>

    </div>

    <!-- DOCUMENTS TABLE -->
    <q-table :rows="documents" :columns="columns" row-key="date" v-model:pagination="pagination" class="q-my-md" :loading="loading">
        <template v-slot:body="props">
            <q-tr :props="props">
                <q-td key="filename" :props="props">
                    <div class="text-bold overflow-ellipsis">{{ props.row.filename }} ({{ formatBytes(props.row.size) }})<q-tooltip anchor="bottom middle">{{ props.row.filename }} ({{ formatBytes(props.row.size) }})</q-tooltip></div>
                    <div class="overflow-ellipsis">{{ props.row.template }}</div>
                </q-td>
                <!--
                <q-td key="template" :props="props">
                    {{ props.row.template }}
                </q-td>
                -->
                <!--
                <q-td key="author" :props="props">
                    {{ props.row.author }}
                </q-td>
                -->
                <q-td key="created" :props="props">
                    <div class="text-bold">{{ props.row.created }}</div>
                    <div>{{ props.row.author }}</div>
                </q-td>
                <q-td key="note" :props="props">
                    {{ props.row.note }}
                </q-td>
                <q-td key="actions" :props="props">
                    <div class="float-right">
                        <q-btn dense round flat color="grey" name="download" @click="" :href="`${store.host}/api/document/${props.row.id}/`" icon="sym_o_download" :disable="!edit" v-if="props.row.id">
                            <q-tooltip class="bg-black">Télécharger</q-tooltip>
                        </q-btn>
                        <!--
                        <q-btn dense round flat color="grey" name="download" @click="store.downloadDocument(props.row.id)" icon="sym_o_download" :disable="!edit" v-if="props.row.id">
                            <q-tooltip class="bg-black">Télécharger</q-tooltip>
                        </q-btn>
                        -->
                        <!-- <q-btn dense round flat color="blue" name="edit" @click="handleEdition(props.row)" icon="sym_o_edit" :disable="!edit">
                            <q-tooltip class="bg-black">Modifier</q-tooltip>
                        </q-btn> -->
                        <q-btn dense round flat color="red" name="delete" @click="handleDeletion(props.row)" icon="sym_o_delete" :disable="!edit">
                            <q-tooltip class="bg-black">Supprimer</q-tooltip>
                        </q-btn>
                    </div>
                </q-td>
            </q-tr>
        </template>
    </q-table>

    <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
        {{ documents }}
    </div>

    <!-- ADD NEW DIALOG -->
    <q-dialog v-model="dialog.newDocument">
        <NewDocumentDialog v-model="documents" :item_type="type"></NewDocumentDialog>
    </q-dialog>

    <!-- EDIT DOCUMENT DIALOG -->
    <!-- <q-dialog v-model="dialog.edit">
        <EditDocumentDialog v-model="selected" :item_type="type"></EditDocumentDialog>
    </q-dialog> -->

    <!-- DELETE DIALOG -->
    <DeleteDialog v-model="dialog.deletion" @delete-event="deleteRessource(selected)" :content="dialog_content" />
</template>

<script>
import { date } from 'quasar'
import { store } from '../store/store.js'
import { formatBytes } from '../store/shared.js'
import NewDocumentDialog from "../views/NewDocumentDialog.vue"
// import EditDocumentDialog from '../views/EditDocumentDialog.vue'
import DeleteDialog from './DeleteDialog.vue'

const host = import.meta.env.VITE_API_URL

const columns = [
    { name: 'filename', align: 'left', label: 'Fichier', field: 'filename', sortable: true, style: 'max-width: 250px; width: 250px' },
    /*{ name: 'template', align: 'left', label: 'Type', field: 'template', sortable: true }, */
    /*{ name: 'author', align: 'left', label: 'Ajouté par', field: 'author', sortable: true },*/
    { name: 'created', align: 'left', label: 'Ajouté le', field: 'created', sortable: true, style: 'max-width: 110px; width: 110px' },
    { name: 'note', align: 'left', label: 'Notes', field: 'note', sortable: true, style: 'max-width: 190px; width: 190px; white-space: normal;' },
    { name: 'actions', align: 'right', label: '', field: 'action', sortable: false, style: 'max-width: 120px; width: 80px' }
]

export default {
    name: 'DocumentsTable',
    // components: { NewDocumentDialog, EditDocumentDialog, DeleteDialog },
    components: { NewDocumentDialog, DeleteDialog },
    props: { 'type': Number, 'edit': Boolean, 'modelValue': Object },
    emits: ['update:modelValue'],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            date: date,
            selected: null,
            dialog: { newDocument: false, deletion: false },
            columns: columns,
            dialog_content: undefined,
            loading: false,
            pagination: {
                rowsNumber: 0,
                sortBy: "date",
                descending: false,
                page: 1,
                rowsPerPage: 20,
            },
        }
    },
    computed: {
        documents: {
            get() {
                return this.modelValue
            },
            set(documents) {
                this.$emit('update:modelValue', documents)
            }
        }
    },
    async created() {

        this.loading = true

        this.data = await this.documents

        this.rows = this.data.results
        this.pagination.rowsNumber = this.data.nrows
        this.loading = false

    },
    methods: {
        formatBytes,
        addDocument() {
            this.dialog.newDocument = true
        },
        /*
        handleEdition(val) {
             this.selected = val
             this.dialog.edit = true
        },
        */
        handleDeletion(val) {
            this.selected = val
            this.dialog_content = `Supprimer définitivement le document '${val.filename}' ?`
            this.dialog.deletion = true
        },
        async deleteRessource(ressource) {
            this.documents = this.documents.filter(x => x.filename !== ressource.filename)
            if (ressource.id !== undefined) {
                this.loading = true
                store.deleteDocument(ressource.id)
                this.loading = false
            }
        },
    }
}
</script>

<style scoped>
.overflow-ellipsis{
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>
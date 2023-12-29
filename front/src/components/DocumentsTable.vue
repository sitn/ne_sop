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
    <q-table :rows="documents" :columns="columns" row-key="date" class="q-my-md">
        <template v-slot:body="props">
            <q-tr :props="props">
                <q-td key="filename" :props="props">
                    <div class="text-bold">{{ props.row.filename }} ({{ formatBytes(props.row.size) }})</div>
                    <div>{{ props.row.template }}</div>
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
                        <q-btn dense round flat color="grey" name="download" @click="store.downloadDocument(props.row.id)" icon="sym_o_download" :disable="!edit" v-if="props.row.id">
                            <q-tooltip class="bg-black">Télécharger</q-tooltip>
                        </q-btn>
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

    <!-- EDIT EVENT DIALOG -->
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

const columns = [
    { name: 'filename', align: 'left', label: 'Fichier', field: 'filename', sortable: true },
    /*{ name: 'template', align: 'left', label: 'Type', field: 'template', sortable: true }, */
    /*{ name: 'author', align: 'left', label: 'Ajouté par', field: 'author', sortable: true },*/
    { name: 'created', align: 'left', label: 'Ajouté le', field: 'created', sortable: true },
    { name: 'note', align: 'left', label: 'Notes', field: 'note', sortable: true },
    { name: 'actions', align: 'right', label: '', field: 'action', sortable: false }
]

export default {
    name: 'DocumentsTable',
    // components: { NewDocumentDialog, EditDocumentDialog, DeleteDialog },
    components: { NewDocumentDialog, DeleteDialog },
    props: { 'type': Number, 'edit': Boolean, 'modelValue': Object }, //  'events': Object,
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
    created() {
    },
    mounted() {
    },
    methods: {
        formatBytes,
        addDocument() {
            this.dialog.newDocument = true
        },
        // handleEdition(val) {
        //     this.selected = val
        //     this.dialog.edit = true
        // },
        handleDeletion(val) {
            this.selected = val
            this.dialog_content = `Supprimer définitivement le document '${val.filename}' ?`
            this.dialog.deletion = true
        },
        async deleteRessource(ressource) {
            this.documents = this.documents.filter(x => x.filename !== ressource.filename)
            if (ressource.id !== undefined) {
                store.deleteDocument(ressource.id)
            }
        },
    }
}
</script>

<style scoped></style>
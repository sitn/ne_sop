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
                    {{ props.row.filename }} ({{ formatBytes(props.row.filesize) }})
                </q-td>
                <q-td key="template" :props="props">
                    {{ props.row.template }}
                </q-td>
                <!-- <q-td key="author" :props="props">
                    {{ props.row.author }}
                </q-td> -->
                <!-- <q-td key="date" :props="props">
                    {{ props.row.date }}
                </q-td> -->
                <q-td key="created" :props="props">
                    {{ date.formatDate(props.row.created, 'DD.MM.YYYY HH:mm:ss') }}
                </q-td>
                <q-td key="note" :props="props">
                    {{ props.row.note }}
                </q-td>
                <q-td key="actions" :props="props">
                    <div class="float-right">
                        <q-btn dense round flat color="grey" name="edit" @click="console.log(props.row)" icon="sym_o_download" :disable="!edit">
                            <q-tooltip class="bg-black">Télécharger</q-tooltip>
                        </q-btn>
                        <q-btn dense round flat color="red" name="delete" @click="handleDeletion(props.row.id)" icon="sym_o_delete" :disable="!edit">
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
        <NewDocumentDialog v-model="documents" :type="type"></NewDocumentDialog>
    </q-dialog>

    <!-- DELETE DIALOG -->
    <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />
</template>

<script>
import { date } from 'quasar'
import { store } from '../store/store.js'
import { formatBytes } from '../store/shared.js'
import NewDocumentDialog from "../views/NewDocumentDialog.vue"
import DeleteDialog from './DeleteDialog.vue'

const columns = [
    { name: 'filename', align: 'left', label: 'Fichier', field: 'filename', sortable: true },
    // { name: 'filesize', align: 'left', label: 'Taille', field: 'filesize', sortable: true },
    // { name: 'format', align: 'left', label: 'Format', field: 'format', sortable: true },
    // { name: 'version', align: 'center', label: 'version', field: 'version', sortable: true },
    { name: 'template', align: 'left', label: 'Type', field: 'template', sortable: true },
    // { name: 'author', align: 'left', label: 'Ajouté par', field: 'author', sortable: true },
    { name: 'created', align: 'left', label: 'Ajouté le', field: 'created', sortable: true },
    { name: 'note', align: 'left', label: 'Notes', field: 'note', sortable: true },
    { name: 'actions', align: 'right', label: '', field: 'action', sortable: false }
]

export default {
    name: 'DocumentsTable',
    components: { NewDocumentDialog, DeleteDialog },
    props: { 'type': String, 'edit': Boolean, 'modelValue': Object }, //  'events': Object,
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
        // date,
        formatBytes,
        addDocument() {
            this.dialog.newDocument = true
        },
        handleDeletion(val) {
            this.selected = val
            this.dialog.deletion = true
        },
        async remove() {
            this.documents = this.documents.filter((x) => (x.id !== this.selected))
        },
        async downloadRessource(ressource) {
            let filepath = [
                import.meta.env.VITE_OP_PATH,
                '20' + this.item.number.split('.')[0],
                this.item.number.split('.')[1],
                ressource.filename
            ].join('\\')
            console.log('filepath', 'file:///' + filepath)
            // window.open('file://' +  filepath, "_blank")
        },
    }
}
</script>

<style scoped></style>
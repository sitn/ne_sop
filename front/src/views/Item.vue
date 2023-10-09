<template>
    <div class="">
        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Objets parlementaires" to="/items" />
                    <q-breadcrumbs-el :label="item.number.toString()" />
                </q-breadcrumbs>
            </div>

            <!-- FORM -->
            <ItemForm v-model="item" :edit="edit"></ItemForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="false" :wait="wait" :buttons="{ 'save': true, 'deletion': true }" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode"></FloatingButtons>

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

            <!-- ADD NEW ENTITY DIALOG -->
            <q-dialog v-model="addEntityDialog">
                <NewEntityDialog @addNewEntity="addNewEntity"></NewEntityDialog>
            </q-dialog>


            <!-- ADD NEW DOCUMENT DIALOG -->
            <q-dialog v-model="addDocumentDialog">
                <NewDocumentDialog></NewDocumentDialog>
            </q-dialog>

            <!-- Dialog for creating first model in documents -->
            <q-dialog v-model="showAddFirstDocumentDialog">
                <q-card>
                    <q-card-section>
                        <div class="text-h6">Ajouter un nouveau modèle aux documents ?</div>
                    </q-card-section>

                    <q-card-section class="row q-pt-sm">
                        <div class="row">
                            <div class="col-1" style="text-align: center;">
                                <q-icon name="warning" color="warning" size="3em" />
                            </div>
                            <div class="col-11 q-pl-md">
                                <span class="q-ml-sm" style="float: left;">En cliquant sur confirmer, une version originale du modèle "<b>{{ formalDocumentModels.filter(e => e.id == selectedFormalDocumentModel)[0].name }}</b>" sera ajoutée aux documents.</span>
                            </div>
                        </div>
                    </q-card-section>

                    <q-card-actions align="right">
                        <q-btn flat label="Annuler" color="primary" v-close-popup />
                        <q-btn flat label="Confirmer" color="primary" v-close-popup @click="saveNewFirstDocument" />
                    </q-card-actions>
                </q-card>
            </q-dialog>

            <!-- Dialog for adding new version of document -->
            <q-dialog v-model="showAddDocumentDialog" persistent>
                <q-card style="min-width: 600px">
                    <q-card-section>
                        <div class="text-h6">Ajouter un document</div>
                    </q-card-section>

                    <q-card-section class="q-pt-sm q-gutter-sm">
                        <p>
                            Sélectionner le fichier Word à enregistrer. <br>
                            Il sera enregistré comme une nouvelle version du modèle "<b>{{ formalDocumentModels.filter(e => e.id == selectedFormalDocumentModel)[0].name }}</b>". Pour changer le type de modèle, il faut modifier la valeur sélectionnée dans le champ "Modèle de document".
                        </p>
                        <q-file outlined v-model="newFile" label="Fichier" accept=".doc, .docx" @update:model-value="updatenewFile">

                            <template v-slot:prepend>
                                <q-icon name="attach_file" />
                            </template>
                            <template v-if="newFile" v-slot:append>
                                <q-icon name="cancel" @click.stop.prevent="newFile = null" class="cursor-pointer" />
                            </template>
                        </q-file>
                    </q-card-section>

                    <q-card-actions align="right" class="text-primary">
                        <q-btn flat label="Annuler" v-close-popup />
                        <q-btn flat label="Enregistrer" v-close-popup :disable="newFile === null" @click="saveNewDocument" />
                    </q-card-actions>
                </q-card>
            </q-dialog>

        </q-layout>

    </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import documents from '../assets/data/documents.json'
import itemTypes from '../assets/data/item-types.json'
import templates from '../assets/data/templates.json'
import ItemForm from "../components/ItemForm.vue"
import FloatingButtons from "../components/FloatingButtons.vue"
import NewEntityDialog from "./NewEntityDialog.vue"
import NewDocumentDialog from "./NewDocumentDialog.vue"
import DeleteDialog from '../components/DeleteDialog.vue'


// import NewEventDialog from "./NewEventDialog.vue"

const documentsColumns = [
    { name: 'version', align: 'center', label: 'version', field: 'version', sortable: true },
    { name: 'type', align: 'left', label: 'Type', field: 'filename', sortable: true },
    { name: 'author', align: 'left', label: 'Auteur', field: 'author', sortable: true },
    { name: 'date', align: 'left', label: 'Date', field: 'date', sortable: true },
    { name: 'note', align: 'left', label: 'Note', field: 'note', sortable: true },
    { name: 'actions', align: 'right', label: '', field: 'action' }
]

const formalDocumentColumns = [
    { name: 'version', align: 'center', label: 'version', field: 'version', sortable: true },
    { name: 'filename', align: 'left', label: 'Fichier', field: 'filename', sortable: true },
    { name: 'filesize', align: 'left', label: 'Taille', field: 'filesize', sortable: true },
    { name: 'auteur', align: 'left', label: 'Auteur', field: 'author', sortable: true },
    { name: 'date', align: 'left', label: 'Date', field: 'date', sortable: true },
    { name: 'note', align: 'left', label: 'Note', field: 'note', sortable: true },
    { name: 'action', align: 'left', label: '', field: 'action' }
]

const attachementColumns = [
    { name: 'filename', align: 'left', label: 'Fichier', field: 'filename', sortable: true },
    { name: 'filesize', align: 'left', label: 'Taille', field: 'filesize', sortable: true },
    { name: 'format', align: 'left', label: 'Format', field: 'format', sortable: true },
    { name: 'auteur', align: 'left', label: 'Auteur', field: 'author', sortable: true },
    { name: 'date', align: 'left', label: 'Date', field: 'date', sortable: true },
    { name: 'note', align: 'left', label: 'Note', field: 'note', sortable: true },
    { name: 'action', align: 'left', label: '', field: 'action' }
]

const eventsColumns = [
    { name: "date", align: "left", label: "Date", field: "date", sortable: true },
    { name: "time", align: "left", label: "Heure", field: "", sortable: true },
    { name: "type", align: "left", label: "Type", field: "eventType", sortable: true },
    { name: "actions", align: "right", label: "", field: "", sortable: false }
]

const subset = ["Parlementaire", "Groupe parlementaire", "Autre"]

export default {
    name: 'Item',
    components: { ItemForm, FloatingButtons, NewEntityDialog, NewDocumentDialog, DeleteDialog },
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
            item: null,
            index: store.items.findIndex((e) => (e.id === this.$route.params.id)),
            itemTypes: itemTypes,
            formalDocumentRowsUnfiltered: documents.filter((e) => (e.ressourcetype === 'formal')),
            formalDocumentRows: [],
            formalDocumentColumns: formalDocumentColumns,
            attachementRows: documents.filter((e) => (e.ressourcetype === 'attachement')),
            attachementColumns: attachementColumns,
            documentsColumns: documentsColumns,
            eventsColumns: eventsColumns,
            authorOptions: store.entities.filter(e => subset.includes(e.type)), // authors,
            addEntityDialog: false,
            addDocumentDialog: false,
            serviceOptions: store.entities.filter((e) => (e.type === "Service de l'état")),
            formalDocumentModels: templates,
            selectedFormalDocumentModel: -1,
            showAddDocumentDialog: false,
            newFile: null,
            showAddFirstDocumentDialog: false,
        }
    },
    computed: {
    },
    created() {
        store.saveButton = true
        this.item = Object.assign({}, store.items.find((e) => (e.id === this.$route.params.id)))
    },
    mounted() {

        this.formalDocumentRows = this.formalDocumentRowsUnfiltered
        this.updateFormalDocumentModelFilter(this.selectedFormalDocumentModel)
        this.updateNumberOfFormalDocumentsByModel()
    },
    methods: {
        async load() {
            // TODO: GET RECORD FROM DATABASE
            console.log(`${this.$options.name}.vue | load()`)
        },
        async save() {
            // TODO: POST RECORD TO DATABASE
            console.log(`${this.$options.name}.vue | save()`)
            this.wait = true
            await sleep(Math.random() * 1300)
            let ind = store.items.findIndex((e) => (e.id === this.$route.params.id))
            store.items[ind] = Object.assign({}, this.item)
            this.wait = false
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
        },
        addEntity() {
            console.log('Item.vue | Add new entity')
            this.addEntityDialog = true
        },
        addDocument() {
            console.log('Item.vue | Add new entity')
            this.addDocumentDialog = true
        },
        async addNewEntity(val) {

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
                store.entities.push(newOption)
                // this.authorOptions.push(val)
                this.item.author = newOption
                // POST NEW ENTITY TO DATABASE

                console.log('authorOptions')
                console.log(this.authorOptions)
            }

        },
        filterFn(val, update, abort) {
            update(() => {
                // TODO - GET RECORDS FROM DATABASE
                const needle = val.toLowerCase()
                // this.authorOptions = entities.filter((v) => v.name.toLowerCase().indexOf(needle) > -1)
                this.authorOptions = store.entities.filter((e) => subset.includes(e.type)).filter((v) => v.name.toLowerCase().indexOf(needle) > -1)
            })
        },
        async downloadRessource(ressource) {
            let filepath = [
                import.meta.env.VITE_OP_PATH,
                '20' + this.item.number.split('.')[0],
                this.item.number.split('.')[1],
                ressource.filename
            ].join('\\')

            console.log('filepath', 'file:///' + filepath)
            // window.open('file://' +  filepath, "_blank");
        },

        updateFormalDocumentModelFilter(value) {
            if (value < 0) {
                this.formalDocumentRows = this.formalDocumentRowsUnfiltered;
            } else {
                this.formalDocumentRows = this.formalDocumentRowsUnfiltered.filter(e => e.model_id == value);
            }
        },

        updateNumberOfFormalDocumentsByModel() {
            this.formalDocumentModels.forEach(e => {
                e.nbVersions = this.formalDocumentRowsUnfiltered.filter(x => x.model_id == e.id).length;
            });

            this.formalDocumentModels.sort((a, b) => (a.nbVersions < b.nbVersions) ? 1 : -1);

            this.formalDocumentModels.unshift({
                id: -1,
                nbVersions: this.formalDocumentRowsUnfiltered.length,
                name: "Tous",
            });
        },

        updatenewFile(filepath) {
            console.log('updated new file path', filepath);
        },

        saveNewDocument() {
            console.log('save new version', this.newFile)
        },

        saveNewFirstDocument() {
            console.log('save new first version document', this.formalDocumentModels.filter(e => e.id == this.selectedFormalDocumentModel)[0].name);
        },

        openAddNewFormalDocumentDialog() {
            let nbModelVersions = this.formalDocumentRowsUnfiltered.filter(e => e.model_id == this.selectedFormalDocumentModel).length;

            if (nbModelVersions === 0) {
                this.showAddFirstDocumentDialog = true;
            } else if (nbModelVersions > 0) {
                this.showAddDocumentDialog = true;
            }
        },
    }
}
</script>

<style scoped></style>
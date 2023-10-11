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
import templates from '../assets/data/templates.json'
import ItemForm from "../components/ItemForm.vue"
import FloatingButtons from "../components/FloatingButtons.vue"

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
    { name: "actions", align: "center", label: "", field: "", sortable: false }
]

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
            // actionButtons: { save: 'active', deletion: 'none' },
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
            formalDocumentRowsUnfiltered: documents.filter((e) => (e.ressourcetype === 'formal')),
            formalDocumentRows: [],
            formalDocumentColumns: formalDocumentColumns,
            attachementRows: documents.filter((e) => (e.ressourcetype === 'attachement')),
            attachementColumns: attachementColumns,
            eventsColumns: eventsColumns,
            authorOptions: authors, //entities.filter(e => e.type.includes("Parlementaire","Groupe politique","Commission parlementaire instituée")),
            addEntityDialog: false,
            serviceOptions: store.entities.filter((e) => (e.type === "Service de l'état")),
            formalDocumentModels: templates,
            selectedFormalDocumentModel: -1,
            showAddDocumentDialog: false,
            newFile: null,
            showAddFirstDocumentDialog: false,
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

        this.formalDocumentRows = this.formalDocumentRowsUnfiltered;
        this.updateFormalDocumentModelFilter(this.selectedFormalDocumentModel);
        this.updateNumberOfFormalDocumentsByModel();

    },
    methods: {
        async save() {
            // TODO - POST NEW RECORD TO DATABASE
            console.log(`${this.$options.name}.vue | save()`)
            this.wait = true
            await sleep(Math.random() * 1300)
            store.items.push(this.item)
            this.wait = false

            this.$router.push({ name: 'ItemsList' })
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
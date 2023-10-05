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

            <Form title="Objets parlementaires" :edit="false" :toggle="true" @edit-event="setEditMode">

                <template v-slot:body>

                    <!-- GENERAL INFORMATION SECTION -->
                    <FormSection title="Informations générales" class="q-mt-none">
                        <template v-slot:content>
                            <div class="text-h6">Informations générales</div>

                            <div class="row q-col-gutter-lg q-py-md">

                                <!-- REFERENCE NUMBER TEXT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input bg-color="white" outlined v-model="item.number" label="N°" :disable="!edit" />
                                </div>

                                <!-- TYPE SELECT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-select bg-color="white" outlined v-model="item.type" :options="itemTypes" label="Type" :disable="!edit">
                                    </q-select>
                                </div>

                            </div>

                            <div class="row q-col-gutter-lg q-py-md">

                                <!-- TITLE TEXT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input bg-color="white" outlined v-model="item.title" label="Titre" :disable="!edit" />
                                </div>

                                <!-- AUTHOR SELECT/CREATE FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-select bg-color="white" outlined v-model="item.author" use-input :options="authorOptions" option-label="name" option-value="name" @filter="filterFn" label="Auteur" emit-value clearable :disable="!edit">

                                        <template v-slot:option="scope">
                                            <q-item v-bind="scope.itemProps">
                                                <q-item-section>
                                                    <q-item-label>{{ scope.opt.name }}</q-item-label>
                                                    <q-item-label caption>{{ scope.opt.type }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                        </template>

                                        <template v-slot:after>
                                            <q-btn round unelevated color="blue-grey-8" icon="sym_o_person_add" @click="addEntity()" :disable="!edit">
                                                <q-tooltip class="bg-black">Ajouter une nouvelle option</q-tooltip>
                                            </q-btn>
                                        </template>

                                    </q-select>
                                </div>

                            </div>

                            <!-- CONTENT TEXT AREA FIELD -->
                            <div class="row q-col-gutter-lg q-py-md">
                                <div class="col">
                                    <q-input bg-color="white" outlined v-model="item.content" label="Description" type="textarea" :disable="!edit" />
                                </div>
                            </div>

                            <!-- TODO REMOVE/DEV DISPLAY JSON-->
                            <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                                <div>item</div>
                                <div>{{ item }}</div>
                            </div>

                            <!-- TODO REMOVE/DEV DISPLAY JSON-->
                            <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                                <div>store.item</div>
                                <div>{{ store.items.find((e) => (e.id === this.$route.params.id)) }}</div>
                            </div>

                        </template>
                    </FormSection>

                    <!-- PROCESSING SECTION -->
                    <FormSection title="Traitement">
                        <template v-slot:content>
                            <div class="text-h6">Traitement</div>

                            <div class="row q-col-gutter-lg q-py-md">

                                <!-- PRIMARY SERVICE SELECT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-select bg-color="white" outlined v-model="item.services.lead" :options="serviceOptions" option-label="name" option-value="id" label="Service principal" clearable :disable="!edit">
                                        <template v-slot:option="scope">
                                            <q-item v-bind="scope.itemProps">
                                                <q-item-section>
                                                    <q-item-label>{{ scope.opt.name }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                        </template>
                                    </q-select>
                                </div>

                                <!-- SUPPORT SERVICE SELECT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-select bg-color="white" outlined v-model="item.services.support" :options="serviceOptions" option-label="name" option-value="id" label="Service(s) en appui" multiple clearable :disable="!edit">
                                        <template v-slot:option="scope">
                                            <q-item v-bind="scope.itemProps">
                                                <q-item-section>
                                                    <q-item-label>{{ scope.opt.name }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                        </template>
                                    </q-select>
                                </div>

                            </div>

                            <div class="row q-py-md">

                                <!-- URGENT CHECKBOX FIELD -->
                                <q-item tag="label" v-ripple :disable="!edit">
                                    <q-item-section avatar>
                                        <q-checkbox v-model="item.urgent" val="true" color="blue" :disable="!edit" />
                                    </q-item-section>
                                    <q-item-section>
                                        <q-item-label>Urgent</q-item-label>
                                        <q-item-label caption>Demande nécessite un traitement prioritaire</q-item-label>
                                    </q-item-section>
                                </q-item>

                                <!-- WRITTEN RESPONSE CHECKBOX FIELD -->
                                <q-item tag="label" v-ripple :disable="!edit">
                                    <q-item-section avatar>
                                        <q-checkbox v-model="item.writtenResponse" val="true" color="blue" :disable="!edit" />
                                    </q-item-section>
                                    <q-item-section>
                                        <q-item-label>Réponse écrite</q-item-label>
                                        <q-item-label caption>Demande nécessite une réponse écrite</q-item-label>
                                    </q-item-section>
                                </q-item>

                                <!-- ORAL RESPONSE CHECKBOX FIELD -->
                                <q-item tag="label" v-ripple :disable="!edit">
                                    <q-item-section avatar>
                                        <q-checkbox v-model="item.oralResponse" val="true" color="blue" :disable="!edit" />
                                    </q-item-section>
                                    <q-item-section>
                                        <q-item-label>Réponse orale</q-item-label>
                                        <q-item-label caption>Demande nécessite une réponse orale</q-item-label>
                                    </q-item-section>
                                </q-item>

                            </div>

                        </template>
                    </FormSection>

                    <!-- EVENTS SECTION -->
                    <FormSection title="Calendrier">
                        <template v-slot:content>
                            <div class="text-h6">Calendrier</div>

                            <div class="row q-px-none q-my-md items-center">

                                <!-- ADD NEW EVENT BUTTON -->
                                <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6">
                                    <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" @click="addEvent()" :disable="!edit">
                                        <q-tooltip class="bg-black">Ajouter un évenement au calendrier</q-tooltip>
                                    </q-btn>
                                </div>

                            </div>

                            <!-- EVENTS TABLE -->
                            <q-table :rows="item.events" :columns="eventsColumns" row-key="date" class="q-my-md">
                                <template v-slot:body="props">
                                    <q-tr :props="props">
                                        <q-td key="date" :props="props">
                                            {{ props.row.date }}
                                        </q-td>
                                        <q-td key="time" :props="props">
                                            {{ props.row.time }}
                                        </q-td>
                                        <q-td key="type" :props="props">
                                            {{ props.row.eventType }}
                                        </q-td>
                                        <q-td key="actions" :props="props">
                                            <q-btn dense round flat color="red" name="delete" @click="console.log(props.row)" icon="sym_o_delete" :disable="!edit">
                                                <q-tooltip class="bg-black">Supprimer</q-tooltip>
                                            </q-btn>
                                        </q-td>
                                    </q-tr>
                                </template>
                            </q-table>

                            <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                                {{ item.events }}
                            </div>

                        </template>
                    </FormSection>

                    <!-- FORMAL DOCUMENTS SECTION -->
                    <FormSection title="Documents">
                        <template v-slot:content>
                            <div class="text-h6">TEST - Documents formels</div>

                            <div class="row q-px-none q-my-md items-center">

                                <!-- ADD NEW DOCUMENT BUTTON -->
                                <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6">
                                    <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" @click="addDocument()" :disable="!edit">
                                        <q-tooltip class="bg-black">Ajouter un document</q-tooltip>
                                    </q-btn>
                                </div>

                            </div>

                            <!-- DOCUMENTS TABLE -->
                            <q-table :rows="item.documents" :columns="documentsColumns" row-key="date" class="q-my-md">
                                <template v-slot:body="props">
                                    <q-tr :props="props">
                                        <q-td key="version" :props="props">
                                            {{ props.row.version }}
                                        </q-td>
                                        <q-td key="type" :props="props">
                                            {{ props.row.type }}
                                        </q-td>
                                        <q-td key="author" :props="props">
                                            {{ props.row.author }}
                                        </q-td>
                                        <q-td key="date" :props="props">
                                            {{ props.row.date }}
                                        </q-td>
                                        <q-td key="note" :props="props">
                                            {{ props.row.note }}
                                        </q-td>
                                        <q-td key="actions" :props="props">
                                            <q-btn dense round flat color="grey" name="edit" @click="console.log(props.row)" icon="sym_o_note_add" :disable="!edit">
                                                <q-tooltip class="bg-black">Modifier</q-tooltip>
                                            </q-btn>
                                            <q-btn dense round flat color="grey" name="edit" @click="console.log(props.row)" icon="sym_o_download" :disable="!edit">
                                                <q-tooltip class="bg-black">Télécharger</q-tooltip>
                                            </q-btn>
                                            <q-btn dense round flat color="red" name="delete" @click="console.log(props.row)" icon="sym_o_delete" :disable="!edit">
                                                <q-tooltip class="bg-black">Supprimer</q-tooltip>
                                            </q-btn>
                                        </q-td>
                                    </q-tr>
                                </template>
                            </q-table>


                            <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                                {{ item.events }}
                            </div>

                        </template>
                    </FormSection>

                    <!-- FORMAL DOCUMENTS SECTION -->
                    <FormSection title="Documents">
                        <template v-slot:content>
                            <div class="text-h6">Documents formels</div>

                            <div class="q-py-sm q-gutter-md row">
                                <q-select v-model="selectedFormalDocumentModel" :options="formalDocumentModels" :option-label="'name'" :option-value="'id'" label="Modèle de document" map-options emit-value @update:model-value="updateFormalDocumentModelFilter" style="min-width: 400px" bg-color="white" outlined>

                                    <template v-slot:option="scope">
                                        <q-item v-bind="scope.itemProps">
                                            <!--
                                            <q-item-section avatar>
                                                <q-icon name="email" />
                                            </q-item-section>
                                            -->
                                            <q-item-section>
                                                <q-item-label>{{ scope.opt.name }}</q-item-label>
                                            </q-item-section>
                                            <q-item-section side>
                                                <q-badge :color="scope.opt.nbVersions > 0 ? 'green' : 'grey'">
                                                    {{ scope.opt.nbVersions }}
                                                </q-badge>
                                            </q-item-section>
                                        </q-item>
                                    </template>
                                </q-select>

                                <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" @click="openAddNewFormalDocumentDialog" :disabled="selectedFormalDocumentModel < 0">
                                    <q-tooltip class="bg-black">Ajouter un document</q-tooltip>
                                </q-btn>

                            </div>

                            <div class="q-py-md">

                                <q-table :title="`${this.formalDocumentRows.length} version(s)`" :rows="formalDocumentRows" :columns="formalDocumentColumns" row-key="name">
                                    <template v-slot:body="props">
                                        <q-tr :props="props">
                                            <q-td key="version" :props="props">
                                                {{ props.row.version }}
                                            </q-td>
                                            <q-td key="filename" :props="props">
                                                <a href="#" @click.prevent="downloadRessource(props.row)">
                                                    {{ props.row.filename }}
                                                </a>
                                            </q-td>
                                            <q-td key="filesize" :props="props">
                                                {{ props.row.filesize }}
                                            </q-td>
                                            <q-td key="auteur" :props="props">
                                                {{ props.row.author }}
                                            </q-td>
                                            <q-td key="date" :props="props">
                                                {{ props.row.date }}
                                            </q-td>
                                            <q-td key="note" :props="props">
                                                {{ props.row.note }}
                                            </q-td>
                                            <q-td key="action" :props="props">
                                                <q-btn dense round flat color="red" name="delete" @click="console.log(props.row)" icon="sym_o_delete" :disable="!edit">
                                                    <q-tooltip class="bg-black">Supprimer</q-tooltip>
                                                </q-btn>
                                            </q-td>
                                        </q-tr>
                                    </template>
                                </q-table>
                            </div>

                            <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                                {{ formalDocumentRowsUnfiltered }}
                            </div>

                        </template>
                    </FormSection>

                    <!-- ATTACHEMENTS SECTION -->
                    <FormSection title="Pièces jointes">
                        <template v-slot:content>
                            <div class="text-h6">Pièces jointes</div>

                            <div class="row q-px-none q-my-md items-center">

                                <!-- ADD NEW ATTACHEMENT BUTTON -->
                                <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6">
                                    <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" @click="" :disable="!edit">
                                        <q-tooltip class="bg-black">Ajouter une pièce jointe</q-tooltip>
                                    </q-btn>
                                </div>

                            </div>

                            <q-table :title="`${this.attachementRows.length} fichier(s)`" :rows="attachementRows" :columns="attachementColumns" row-key="name">
                                <template v-slot:body="props">
                                    <q-tr :props="props">
                                        <q-td key="version" :props="props">
                                            {{ props.row.version }}
                                        </q-td>
                                        <q-td key="filename" :props="props">
                                            <a href="#" @click.prevent="downloadRessource(props.row)">
                                                {{ props.row.filename }}
                                            </a>
                                        </q-td>
                                        <q-td key="filesize" :props="props">
                                            {{ props.row.filesize }}
                                        </q-td>
                                        <q-td key="format" :props="props">
                                            {{ props.row.format }}
                                        </q-td>
                                        <q-td key="auteur" :props="props">
                                            {{ props.row.author }}
                                        </q-td>
                                        <q-td key="date" :props="props">
                                            {{ props.row.date }}
                                        </q-td>
                                        <q-td key="note" :props="props">
                                            {{ props.row.note }}
                                        </q-td>
                                        <q-td key="action" :props="props">
                                            <q-btn dense round flat color="red" name="delete" @click="console.log(props.row)" icon="sym_o_delete" :disable="!edit">
                                                <q-tooltip class="bg-black">Supprimer</q-tooltip>
                                            </q-btn>
                                        </q-td>
                                    </q-tr>
                                </template>
                            </q-table>

                        </template>
                    </FormSection>

                </template>

            </Form>

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
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"
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
    components: { Form, FormSection, FloatingButtons, NewEntityDialog, NewDocumentDialog, DeleteDialog },
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
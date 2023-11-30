<template>
    <Form :model="item" :edit="edit">

        <template v-slot:body>

            <!-- GENERAL INFORMATION SECTION -->
            <FormSection title="Informations générales" class="q-mt-none">
                <template v-slot:content>

                    <div class="row q-col-gutter-lg q-py-md">

                        <!-- REFERENCE NUMBER TEXT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input bg-color="white" outlined v-model="item.number" label="N°" :rules="[v => checkFilled(v)]" :disable="!edit" />
                        </div>

                        <!-- TYPE SELECT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-select bg-color="white" outlined v-model="item.type" :options="store.itemTypes" option-label="name" option-value="id" emit-value map-options label="Type" clearable :rules="[v => checkFilled(v)]" :disable="!edit">
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

                    <div class="row q-col-gutter-lg q-py-md">

                        <!-- TITLE TEXT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input bg-color="white" outlined v-model="item.title" label="Titre" :rules="[v => checkFilled(v)]" :disable="!edit" />
                        </div>

                        <!-- AUTHOR SELECT/CREATE FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-select bg-color="white" outlined v-model="item.author" use-input :options="authorOptions" option-label="name" option-value="id" emit-value map-options @filter="filterFn" label="Auteur" clearable :rules="[v => checkFilled(v)]" :disable="!edit">

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

                    <div class="row q-col-gutter-lg q-py-md">

                        <!-- PRIMARY SERVICE SELECT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-select bg-color="white" outlined v-model="item.lead" :options="serviceOptions" option-label="name" option-value="id" emit-value map-options label="Service principal" clearable :rules="[v => checkFilled(v)]" :disable="!edit">
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
                            <q-select bg-color="white" outlined v-model="item.support" :options="serviceOptions" option-label="name" option-value="id" emit-value map-options label="Service(s) en appui" multiple clearable :disable="!edit">
                                <template v-slot:option="scope">
                                    <q-item v-bind="scope.itemProps">
                                        <q-item-section side>
                                            <q-checkbox :model-value="scope.selected" @update:model-value="scope.toggleOption(scope.opt)" />
                                        </q-item-section>
                                        <q-item-section>
                                            <q-item-label>{{ scope.opt.name }}</q-item-label>
                                        </q-item-section>
                                    </q-item>
                                </template>
                            </q-select>
                        </div>


                    </div>

                    <div class="row q-col-gutter-lg q-py-md">

                        <!-- STATUS SELECT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-select bg-color="white" outlined v-model="item.status" :options="itemStatus" option-label="name" option-value="id" emit-value map-options label="Statut" clearable :rules="[v => checkFilled(v)]" :disable="!edit">
                                <template v-slot:option="scope">
                                    <q-item v-bind="scope.itemProps">
                                        <q-item-section side>
                                            <q-badge :color="scope.opt.color" rounded class="q-mr-sm" />
                                        </q-item-section>
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
                                <q-checkbox v-model="item.writtenresponse" val="true" color="blue" :disable="!edit" />
                            </q-item-section>
                            <q-item-section>
                                <q-item-label>Réponse écrite</q-item-label>
                                <q-item-label caption>Demande nécessite une réponse écrite</q-item-label>
                            </q-item-section>
                        </q-item>

                        <!-- ORAL RESPONSE CHECKBOX FIELD -->
                        <q-item tag="label" v-ripple :disable="!edit">
                            <q-item-section avatar>
                                <q-checkbox v-model="item.oralresponse" val="true" color="blue" :disable="!edit" />
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

                    <!-- EVENTS TABLE -->
                    <!-- <EventsTable v-model="item.events" :edit="edit"></EventsTable> -->

                </template>
            </FormSection>

            <!-- DOCUMENTS SECTION -->
            <FormSection title="Documents">
                <template v-slot:content>

                    <!-- DOCUMENTS TABLE -->
                    <!-- <DocumentsTable v-model="item.documents" :type="item.type" :edit="edit"></DocumentsTable> -->

                </template>
            </FormSection>

        </template>

    </Form>

    <!-- ADD NEW ENTITY DIALOG -->
    <q-dialog v-model="dialog.newEntity">
        <NewEntityDialog @addNewEntity="addNewEntity"></NewEntityDialog>
    </q-dialog>
</template>

<script>
import { store } from '../store/store.js'
import { checkFilled } from '../store/shared.js'
// import itemTypes from '../assets/data/item-types.json'
// import itemStatus from '../assets/data/item-status.json'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"
import EventsTable from "../components/EventsTable.vue"
import DocumentsTable from "../components/DocumentsTable.vue"
import NewEntityDialog from "../views/NewEntityDialog.vue"

const subset = ["Parlementaire", "Groupe parlementaire", "Autre"]

export default {
    name: 'EntityForm',
    components: { Form, FormSection, NewEntityDialog, EventsTable, DocumentsTable },
    props: { 'edit': Boolean, 'modelValue': Object },
    emits: ['update:modelValue'],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            dialog: { newEntity: false, newEvent: false, newDocument: false },
            itemTypes: null, // itemTypes,
            itemStatus: [], // itemStatus,
            authorOptions: [], // store.entities.filter(e => subset.includes(e.type)),
            serviceOptions: [], // store.entities.filter((e) => (e.type === "Service de l'état")),
            addEntityDialog: false
        }
    },
    computed: {
        item: {
            get() {
                return this.modelValue
            },
            set(item) {
                // this.$emit('update:modelValue', item)
            }
        }
    },
    beforeCreate() {
        store.getItemTypes()
    },
    async created() {
        // console.log(`router id: ${this.$route.params.id}`)
        // this.itemTypes = await this.getItemTypes()
        // this.itemStatus = await this.getItemStatus()
        this.serviceOptions = await this.searchEntity("", 1)
        this.authorOptions = await this.searchEntity("", 2)
        this.itemStatus = await this.store.getItemStatus()
    },
    mounted() {

    },
    methods: {
        checkFilled,
        addEntity() {
            console.log('ItemForm.vue | Add new entity')
            this.dialog.newEntity = true
        },
        async init() {

            this.serviceOptions = await this.searchEntity("", 1)
            this.authorOptions = await this.searchEntity("", 2)
        },
        async searchEntity(searchString = "", type = []) {

            // TODO: REPLACE WITH GET CALL TO API 

            // await sleep(Math.random() * 1300)
            let str = searchString.toLowerCase()
            let result = ""

            if (str.length >= 3) {
                // this.store.getEntities(str, 1, this.pagination.rowsPerPage)
                result = await this.store.searchEntities(str, type, 1, 5)
                // this.rows = this.store.entities.filter((x) => (x.name.toLowerCase().includes(str)))
            } else {
                // this.store.getEntities("", 1, this.pagination.rowsPerPage)
                result = await this.store.searchEntities("", type, 1, 20)
            }

            return result

        },
        async addNewEntity(val) {

            console.log('Item.vue | addNewEntity()')
            console.log(val)

            let newOption = {
                "id": val.id, // uuidv4(),
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

                // DEV: ADD NEW ENTITY TO LOCAL JSON
                // store.entities.push(newOption)

                // PRODUCTION: POST NEW ENTITY TO DATABASE
                store.addEntity(newOption)

                // this.authorOptions.push(val)
                this.item.author = newOption

                console.log('authorOptions')
                console.log(this.authorOptions)
            }

        },
        filterFn(val, update, abort) {
            update(async () => {
                // TODO - GET RECORDS FROM DATABASE
                const str = val.toLowerCase()
                // this.authorOptions = entities.filter((v) => v.name.toLowerCase().indexOf(needle) > -1)
                // this.authorOptions = store.entities.filter((e) => subset.includes(e.type)).filter((v) => v.name.toLowerCase().indexOf(str) > -1)
                this.authorOptions = await this.searchEntity(str, [2, 3])
            })
        }
    }
}
</script>

<style scoped></style>
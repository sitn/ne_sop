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
                            <q-select bg-color="white" outlined v-model="item.type" :options="itemTypes" option-label="name" option-value="id" emit-value map-options label="Type" clearable :rules="[v => checkFilled(v)]" :disable="!edit">
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

                            <!--  <q-select bg-color="white" outlined v-model="item.author" :options="authorOptions" option-label="name" option-value="id" emit-value map-options label="Auteur" clearable :rules="[v => checkFilled(v)]" :disable="!edit"> -->

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

                    <!-- DESCRIPTION TEXT AREA FIELD -->
                    <div class="row q-col-gutter-lg q-py-md">
                        <div class="col">
                            <q-input bg-color="white" outlined v-model="item.description" label="Description" type="textarea" :disable="!edit" />
                        </div>
                    </div>

                    <!-- TODO REMOVE/DEV DISPLAY JSON-->
                    <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                        <div>item</div>
                        <div>{{ item }}</div>
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
                            <q-select bg-color="white" outlined v-model="item.support" :options="serviceOptions" option-label="name" option-value="id" emit-value map-options label="Service(s) en appui" multiple clearable @clear="reset()" :disable="!edit">
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
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-item tag="label" v-ripple :disable="!edit">
                                <q-item-section avatar>
                                    <q-checkbox v-model="item.urgent" val="true" color="blue" :disable="!edit" />
                                </q-item-section>
                                <q-item-section>
                                    <q-item-label>Urgent</q-item-label>
                                    <q-item-label caption>Demande nécessite un traitement prioritaire</q-item-label>
                                </q-item-section>
                            </q-item>
                        </div>

                        <!-- WRITTEN RESPONSE CHECKBOX FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-item tag="label" v-ripple :disable="!edit">
                                <q-item-section avatar>
                                    <q-checkbox v-model="item.writtenresponse" val="true" color="blue" :disable="!edit" />
                                </q-item-section>
                                <q-item-section>
                                    <q-item-label>Réponse écrite</q-item-label>
                                    <q-item-label caption>Demande nécessite une réponse écrite</q-item-label>
                                </q-item-section>
                            </q-item>
                        </div>

                        <!-- ORAL RESPONSE CHECKBOX FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
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

                        <!-- AUTOMATIC NOTIFICATIONS CHECKBOX FIELD -->
                        <q-item tag="label" v-ripple :disable="!edit">
                            <q-item-section avatar>
                                <q-checkbox v-model="item.autonotify" val="true" color="blue" :disable="!edit" />
                            </q-item-section>
                            <q-item-section>
                                <q-item-label>Notification automatique</q-item-label>
                                <q-item-label caption>Notifier le(s) service(s) à chaque changement</q-item-label>
                            </q-item-section>
                        </q-item>


                    </div>

                    <div class="row q-py-md">
                        <!-- ADD NEW EVENT BUTTON -->
                        <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6">
                            <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_mail" label="Notifier" :href="mailtostring" @click="" :disable="!edit">
                                <q-tooltip class="bg-black">Envoyer une notification au(x) service(s)</q-tooltip>
                            </q-btn>
                        </div>
                    </div>

                </template>
            </FormSection>

            <!-- EVENTS SECTION -->
            <FormSection title="Calendrier">
                <template v-slot:content>

                    <!-- EVENTS TABLE -->
                    <EventsTable v-model="item.events" :edit="edit"></EventsTable>

                </template>
            </FormSection>

            <!-- DOCUMENTS SECTION -->
            <FormSection title="Documents">
                <template v-slot:content>

                    <!-- DOCUMENTS TABLE -->
                    <DocumentsTable v-model="item.documents" :type="item.type" :edit="edit"></DocumentsTable>

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

// const subset = ["Parlementaire", "Groupe parlementaire", "Autre"]

export default {
    name: 'EntityForm',
    components: { Form, FormSection, NewEntityDialog, EventsTable, DocumentsTable },
    props: { 'edit': Boolean, 'modelValue': Object, 'mode': String },
    emits: ['update:modelValue'],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            dialog: { newEntity: false, newEvent: false, newDocument: false },
            itemTypes: [],
            itemStatus: [],
            authorOptions: [],
            serviceOptions: [],
            events: [],
            documents: [],
        }
    },
    computed: {
        item: {
            get() {
                return this.modelValue
            },
            set(item) {
                this.$emit('update:modelValue', item)
            }
        },
        mailtostring() {
            return `mailto:sitn@ne.ch&subject=Objet parlementaire ${this.item.number} - ${this.item.type.name}&body=Bonjour,%0D%0A%0D%0Al'objet parlementaire ${this.item.number} a été modifié.%0D%0A%0D%0AConsulter les modifications: https://sop.ne.ch/items/${this.item.id}`
        }
    },
    beforeCreate() {
    },
    async created() {
        // console.log(`router id: ${this.$route.params.id}`)
        let data1 = await store.getEntities("", 1, 1, 20, "name", "false")
        this.serviceOptions = data1.results
        console.log('this.serviceOptions')
        console.log(this.serviceOptions)

        let data2 = await store.getEntities("", [2, 3], 1, 20, "name", "false")
        this.authorOptions = data2.results
        console.log("this.authorOptions")
        console.log(this.authorOptions)

        this.itemStatus = await store.getItemStatus()
        this.itemTypes = await store.getItemTypes()
        // this.events = await store.getEvents("", this.item.id, 1, 20) // search = "", item = "", page = 1, size = 10

    },
    async mounted() {

    },
    methods: {
        checkFilled,
        reset() {
            this.item.support = []
        },
        addEntity() {
            console.log('ItemForm.vue | Add new entity')
            this.dialog.newEntity = true
        },
        async searchEntity(searchString = "", type = []) {

            // TODO: REPLACE WITH GET CALL TO API 

            // await sleep(Math.random() * 1300)
            let str = searchString.toLowerCase()
            let data = ""

            if (str.length >= 3) {
                // this.store.getEntities(str, 1, this.pagination.rowsPerPage)
                // this.rows = this.store.entities.filter((x) => (x.name.toLowerCase().includes(str)))
                data = await store.getEntities(str, type, 1, 5, "name", "false")
            } else {
                // this.store.getEntities("", 1, this.pagination.rowsPerPage)
                data = await store.getEntities("", type, 1, 20, "name", "false")
            }

            return data.results

        },
        async addNewEntity(val) {

            console.log(`${this.$options.name} | addNewEntity()`)

            let newEntity = await store.addEntity(val)
            // this.authorOptions = await store.getEntities("", [2, 3], 1, 50)
            this.authorOptions = [await store.getEntity(newEntity.id)]

            // this.authorOptions = [newEntity]
            // this.authorOptions = this.authorOptions.unshift(newEntity)
            console.log(this.authorOptions)

            this.item.author = await newEntity.id

        },
        filterFn(val, update, abort) {
            update(async () => {
                console.log('filterFn')
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
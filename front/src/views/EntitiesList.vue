<template>
    <div class="">

        <div class="q-pa-sm q-gutter-sm">

            <!-- BREADCRUMBS NAVIGATION -->
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Personnes et groupes" to="/entities" />
            </q-breadcrumbs>

            <!-- SEARCH AND FILTER SECTION -->
            <div class="row q-col-gutter-md q-px-sm q-mt-xs items-center">

                <!-- SEARCH RECORDS FIELD -->
                <div class="col-xs-12 col-sm-8 col-md-6 col-lg-6">
                    <q-input bg-color="white" v-model="searchString" outlined dense placeholder="Rechercher" @update:model-value="query()">
                        <template v-slot:prepend>
                            <q-icon name="sym_o_search" />
                        </template>
                        <template v-slot:append>
                            <q-spinner color="blue-grey" :thickness="3" v-if="loading" />
                            <!-- FILTER BUTTON -->
                            <q-btn unelevated icon="sym_o_filter_alt" padding="xs" @click="console.log('filter')"> <!-- color="orange-1" text-color="black" -->
                                <q-tooltip class="bg-black">Filtrer</q-tooltip>
                            </q-btn>
                        </template>
                    </q-input>
                </div>

                <!-- ADD NEW RECORD BUTTON -->
                <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6">
                    <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" class="q-py-none q-my-none" @click="" to="/entities/new">
                        <q-tooltip class="bg-black">Ajouter une nouvelle entité</q-tooltip>
                    </q-btn>
                </div>

            </div>

            <!-- ENTITIES TABLE -->
            <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" :filter="filter" @request="onRequest" binary-state-sort class="q-my-lg">

                <!-- TABLE BODY -->
                <template v-slot:body="props">
                    <q-tr :props="props">

                        <!-- NAME COLUMN -->
                        <q-td key="type" :props="props">

                            <router-link :to="{
                                name: 'Entity',
                                params: {
                                    id: props.row.id
                                }
                            }">
                                {{ props.row.name }}
                            </router-link>

                        </q-td>

                        <!-- TYPE COLUMN -->
                        <q-td key="type" :props="props">
                            {{ props.row.type }}
                        </q-td>

                        <!-- ACTIONS COLUMN -->
                        <q-td key="actions" :props="props">
                            <div class="float-right">
                                <q-btn dense round flat color="grey" name="email" @click="console.log(props.row.email)" icon="sym_o_mail" :href="`mailto:${props.row.email}`" v-if="props.row.email !== ''">
                                    <q-tooltip class="bg-black" v-if="props.row.email">Envoyer un email: {{ props.row.email }}</q-tooltip>
                                </q-btn>
                                <q-btn dense round flat color="grey" name="phone" @click="console.log(props.row.telephone)" icon="sym_o_call" :href="`tel:${props.row.telephone}`" v-if="props.row.telephone !== ''">
                                    <q-tooltip class="bg-black" v-if="props.row.telephone">Appeler: {{ props.row.telephone }}</q-tooltip>
                                </q-btn>
                                <q-btn dense round flat color="red" name="delete" @click="handleDeletion(props.row.id)" icon="sym_o_delete">
                                    <q-tooltip class="bg-black">Supprimer</q-tooltip>
                                </q-btn>
                            </div>
                        </q-td>

                    </q-tr>
                </template>
                <template v-slot:no-data>
                    Aucune objet
                </template>
            </q-table>

            <!-- TODO REMOVE/DEV DISPLAY JSON-->
            <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                <div>store.entities</div>
                <div>{{ store.entities }}</div>
            </div>

        </div>

        <!-- DELETE DIALOG -->
        <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

    </div>
</template>

<script>
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import DeleteDialog from '../components/DeleteDialog.vue'

export default {
    name: 'EntitiesList',
    components: { DeleteDialog },
    props: { 'title': String, 'model': Object },
    emits: [],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            selected: null,
            searchString: null,
            filter: "",
            dialog: { deletion: false },
            data: null,
            rows: [],
            loading: false,
            pagination: {
                rowsNumber: 0,
                sortBy: "type",
                descending: false,
                page: 1,
                rowsPerPage: 25,
            },
            columns: [
                {
                    name: "name",
                    align: "left",
                    label: "Nom",
                    field: "name",
                    sortable: true,
                },
                {
                    name: "type",
                    align: "left",
                    label: "Type",
                    field: "type",
                    sortable: true,
                },
                {
                    name: "actions",
                    align: "center",
                    label: "",
                    field: "",
                    sortable: false,
                },
            ],
        }
    },
    computed: {
    },
    async beforeCreate() {
    },
    async created() {
        this.loading = true
        this.data = await store.getEntities("", "", this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
        this.rows = this.data.results // await store.getEntities("", "", this.pagination.page, this.pagination.rowsPerPage) // .then(console.log(this.rows))
        this.pagination.rowsNumber = this.data.nrows
        this.loading = false
    },
    mounted() {
    },
    methods: {
        async onRequest(props) {

            this.loading = true

            console.log('onRequest')
            console.log(props.pagination)
            let { page, rowsPerPage, sortBy, descending } = props.pagination
            // let filter = props.filter

            console.log(`page: ${page}, rowsPerPage: ${rowsPerPage}, sortBy: ${sortBy}, descending: ${descending}`)

            rowsPerPage = rowsPerPage === 0 ? this.pagination.rowsNumber : rowsPerPage // rowsPerPage

            this.data = await store.getEntities("", "", page, rowsPerPage, sortBy, descending)
            this.rows = this.data.results

            // update pagination object
            this.pagination = props.pagination

            /*
            this.pagination.rowsNumber = this.data.nrows
            this.pagination.page = page
            this.pagination.rowsPerPage = rowsPerPage
            this.pagination.sortBy = sortBy
            this.pagination.descending = descending
            */

            this.loading = false

        },
        async query() {

            // TODO: REPLACE WITH GET CALL TO API 
            console.log(`search: ${this.searchString}`)
            this.loading = true

            // await sleep(Math.random() * 1300)

            if (this.searchString.length >= 3) {
                //this.store.getEntities(str, 1, this.pagination.rowsPerPage)
                //this.rows = this.store.entities
                this.data = await store.getEntities(this.searchString, "", this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending) // .then(console.log(this.rows))

                // this.rows = this.store.entities.filter((x) => (x.name.toLowerCase().includes(str)))
            } else {
                this.data = await store.getEntities("", "", this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)

                // this.store.getEntities("", 1, this.pagination.rowsPerPage)
                // this.rows = this.store.entities
            }
            this.rows = this.data.results
            this.loading = false
        },
        handleDeletion(val) {
            this.selected = val
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: REPLACE WITH GET CALL TO API 

            // store.entities = store.entities.filter((x) => (x.id !== this.selected))
            // this.rows = store.entities
            console.log(`delete ${this.selected}`)
            let message = await store.deleteEntity(this.selected)
            if (message) {
                this.data = await store.getEntities(this.searchString, "", this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
                this.rows = this.data.results
                // this.rows = this.rows.filter((x) => (x.id !== this.selected))
            }
            console.log(message)

        }
    }
}
</script>

<style scoped></style>
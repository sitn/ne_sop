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
            <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" :filter="filter" @request="" class="q-my-lg">

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
            rows: [],
            loading: false,
            pagination: {
                rowsNumber: 17, // TODO: REPLACE BY QUERY TO DATABASE
                sortBy: "desc",
                descending: false,
                page: 1,
                rowsPerPage: 20,
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
        // store.getEntities("", 1, 20)
        // this.rows = await store.searchEntities("", [], this.pagination.page, this.pagination.rowsPerPage)
    },
    async created() {
        this.loading = true
        this.rows = await store.searchEntities("", "", this.pagination.page, this.pagination.rowsPerPage) // .then(console.log(this.rows))
        // this.loading = await this.rows.length == 0 ? true : false
        this.loading = false

    },
    mounted() {

    },
    methods: {
        didi() {
            console.log('didi')
        },
        async onRequest(props) {
            const { page, rowsPerPage, sortBy, descending } = props.pagination
            const filter = props.filter

            loading.value = true

            // emulate server
            setTimeout(() => {
                // update rowsCount with appropriate value
                pagination.value.rowsNumber = getRowsNumberCount(filter)

                // get all rows if "All" (0) is selected
                const fetchCount = rowsPerPage === 0 ? pagination.value.rowsNumber : rowsPerPage

                // calculate starting row of data
                const startRow = (page - 1) * rowsPerPage

                // fetch data from "server"
                const returnedData = fetchFromServer(startRow, fetchCount, filter, sortBy, descending)

                // clear out existing data and add new
                rows.value.splice(0, rows.value.length, ...returnedData)

                // don't forget to update local pagination object
                this.pagination.page = page
                this.rowsPerPage = rowsPerPage
                this.sortBy = 'desc' // sortBy
                this.descending = false // descending

                // ...and turn of loading indicator
                this.loading = false
            }, 1500)
        },
        async query() {

            // TODO: REPLACE WITH GET CALL TO API 
            console.log(`search: ${this.searchString}`)
            this.loading = true

            // await sleep(Math.random() * 1300)
            let str = this.searchString.toLowerCase()

            if (this.searchString.length >= 3) {
                //this.store.getEntities(str, 1, this.pagination.rowsPerPage)
                //this.rows = this.store.entities
                this.rows = await store.searchEntities(str, "", this.pagination.page, this.pagination.rowsPerPage) // .then(console.log(this.rows))
                // this.rows = this.store.entities.filter((x) => (x.name.toLowerCase().includes(str)))
            } else {
                this.rows = await store.searchEntities(str, "", this.pagination.page, this.pagination.rowsPerPage)
                // this.store.getEntities("", 1, this.pagination.rowsPerPage)
                // this.rows = this.store.entities
            }
            this.loading = false
        },
        handleDeletion(val) {
            this.selected = val
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: REPLACE WITH GET CALL TO API 

            // store.entities = store.entities.filter((x) => (x.id !== this.selected))
            console.log(`delete ${this.selected}`)
            this.store.deleteEntity(this.selected)

            this.rows = store.entities
        }
    }
}
</script>

<style scoped></style>
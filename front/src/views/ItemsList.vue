<template>
    <div class="">

        <div class="q-pa-sm q-gutter-sm">

            <!-- BREADCRUMBS NAVIGATION -->
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Objets parlementaires" to="/items" />
            </q-breadcrumbs>

            <div class="row q-col-gutter-md q-px-sm q-mt-xs items-center">

                <!-- SEARCH ITEMS FIELD -->
                <div class="col-xs-12 col-sm-8 col-md-6 col-lg-6">
                    <q-input bg-color="white" v-model="searchString" outlined dense placeholder="Rechercher" @update:model-value="query()">
                        <template v-slot:prepend>
                            <q-icon name="sym_o_search" />
                        </template>
                        <template v-slot:append>
                            <q-spinner color="blue-grey" :thickness="3" v-if="loading" />
                            <q-btn unelevated icon="sym_o_filter_alt" padding="xs" @click="console.log('filter')"> <!-- color="orange-1" text-color="black" -->
                                <q-tooltip class="bg-black">Filtrer</q-tooltip>
                            </q-btn>
                        </template>

                    </q-input>
                </div>

                <!-- ADD NEW ITEM BUTTON -->
                <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6">
                    <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" class="q-py-none q-my-none" to="/items/new">
                        <q-tooltip class="bg-black">Ajouter un nouvel objet parlementaire</q-tooltip>
                    </q-btn>
                </div>

            </div>

            <!-- ITEMS TABLE -->
            <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" @request="onRequest" binary-state-sort class="q-my-lg"> <!-- :filter="filter" -->

                <!-- TABLE BODY -->
                <template v-slot:body="props">
                    <q-tr :props="props">

                        <!-- STATUS COLUMN -->
                        <q-td key="status" :props="props">

                            <div>
                                <q-badge color="red" class="q-my-sm" v-if="props.row.urgent">Urgent</q-badge>
                            </div>
                            <div class="row items-center">
                                <q-badge :color="props.row.status.color" rounded class="q-mr-sm" />
                                <div>{{ props.row.status.name }}</div>
                            </div>

                        </q-td>

                        <!-- NUMBER COLUMN -->
                        <q-td key="number" :props="props">
                            {{ props.row.number }}
                        </q-td>
                        <!-- TYPE COLUMN -->
                        <q-td key="type" :props="props">
                            {{ props.row.type.name }}
                        </q-td>
                        <!-- TITLE COLUMN -->
                        <q-td key="title" :props="props">

                            <router-link :to="{
                                name: 'Item',
                                params: {
                                    id: props.row.id
                                }
                            }">
                                {{ props.row.title }}
                            </router-link>
                            <!-- <q-badge color="red" class="q-mx-sm" v-if="props.row.urgent">Urgent</q-badge> -->

                        </q-td>
                        <!-- DEPOSIT DATE COLUMN -->
                        <q-td key="deposit" :props="props">
                            <!-- {{ props.row.events.find((e) => e.eventType === "Dépôt").date }} -->
                            {{ getDate(props.row.events, "Dépôt") }}
                        </q-td>
                        <!-- DELAY DATE COLUMN -->
                        <q-td key="delay" :props="props">
                            <!-- {{ props.row.events.find((e) => e.eventType === "Délai").date }} -->
                            {{ getDate(props.row.events, "Délai") }}
                        </q-td>
                        <!-- ACTIONS COLUMN -->
                        <q-td key="actions" :props="props">
                            <div class="float-right">
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
                <div>store.items</div>
                <div>{{ store.items }}</div>
            </div>

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

        </div>

    </div>
</template>

<script>
import { store } from '../store/store.js'
// import { sleep } from '../store/shared.js'
import itemStatus from '../assets/data/item-status.json'
import DeleteDialog from '../components/DeleteDialog.vue'

export default {
    name: 'ItemsList',
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
            // itemStatus: itemStatus,
            selected: null,
            searchString: null,
            filter: "",
            dialog: { deletion: false },
            data: null,
            rows: [],
            loading: false,
            pagination: {
                rowsNumber: 0,
                sortBy: "number",
                descending: false,
                page: 1,
                rowsPerPage: 25,
            },
            columns: [
                {
                    name: "status",
                    align: "left",
                    label: "Statut",
                    field: "status",
                    sortable: true,
                },
                {
                    name: "number",
                    align: "left",
                    label: "N°",
                    field: "number",
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
                    name: "title",
                    align: "left",
                    label: "Titre",
                    field: "title",
                    sortable: true,
                },
                {
                    name: "deposit",
                    align: "left",
                    label: "Dépôt",
                    field: "events",
                    sortable: true,
                },
                {
                    name: "delay",
                    align: "left",
                    label: "Délai",
                    field: "events",
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
    beforeCreate() {
    },
    async created() {

        this.loading = true
        this.data = await store.getItems("", this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
        this.rows = this.data.results // await store.getEntities("", "", this.pagination.page, this.pagination.rowsPerPage) // .then(console.log(this.rows))
        this.pagination.rowsNumber = this.data.nrows
        this.loading = false

    },
    mounted() {

    },
    methods: {
        async onRequest(props) {

            console.log('onRequest')
            this.loading = true

            let { page, rowsPerPage, sortBy, descending } = props.pagination
            // let filter = props.filter

            console.log(`page: ${page}, rowsPerPage: ${rowsPerPage}, sortBy: ${sortBy}, descending: ${descending}`)

            rowsPerPage = rowsPerPage === 0 ? this.pagination.rowsNumber : rowsPerPage // rowsPerPage

            this.data = await store.getItems("", page, rowsPerPage, sortBy, descending)
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
            // TODO: REPLACE WITH GET CALL TO DATABASE 
            this.loading = true
            // await sleep(Math.random() * 1300)
            if (this.searchString.length >= 3) {
                this.data = await store.getItems(this.searchString, this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
            } else {
                this.data = await store.getItems("", this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
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
            // store.items = store.items.filter((x) => (x.id !== this.selected))
            // this.rows = store.items
            console.log(`delete ${this.selected}`)
            let message = await store.deleteItem(this.selected)
            if (message) {
                this.data = await store.getItems(this.searchString, this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
                this.rows = this.data.results
                // this.rows = this.rows.filter((x) => (x.id !== this.selected))
            }
            console.log(message)

        },
        addItem() {
            // this.addDialog = true
        },
        getDate(events, type) {
            let res = events.find((e) => e.eventType === type)
            if (res) {
                return res.date
            } else {
                return ""
            }
        },
    }

}
</script>

<style scoped></style>
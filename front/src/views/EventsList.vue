<template>
    <div class="q-pa-sm q-gutter-sm">

        <!-- BREADCRUMBS NAVIGATION -->
        <q-breadcrumbs style="font-size: 16px">
            <q-breadcrumbs-el label="Calendrier" to="/events" />
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
                        <!-- 
                            <q-btn unelevated icon="sym_o_filter_alt" padding="xs" @click="console.log('filter')">
                                <q-tooltip class="bg-black">Filtrer</q-tooltip>
                            </q-btn>
                            -->
                    </template>
                </q-input>
            </div>

            <!-- ADD NEW RECORD BUTTON -->
            <!-- 
                <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6">
                    <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" class="q-py-none q-my-none" @click="" to="/events/new">
                        <q-tooltip class="bg-black">Ajouter un nouvel événement</q-tooltip>
                    </q-btn>
                </div>
                -->

        </div>

        <!-- EVENTS TABLE -->
        <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" :filter="filter" @request="onRequest" binary-state-sort class="q-my-lg">
            <!-- TABLE BODY -->
            <template v-slot:body="props">
                <q-tr :props="props">

                    <!-- DATE COLUMN -->
                    <q-td key="date" :props="props">

                        <router-link :to="{
                            name: 'Event',
                            params: {
                                id: props.row.id
                            }
                        }">
                            {{ props.row.date }}
                        </router-link>

                    </q-td>

                    <!-- EVEN TYPE COLUMN -->
                    <q-td key="type" :props="props">
                        {{ props.row.type.name }}
                    </q-td>

                    <!-- ITEM COLUMN -->
                    <q-td key="item" :props="props">


                        <router-link :to="{
                            name: 'Item',
                            params: {
                                id: props.row.item.id
                            }
                        }">
                            <div>{{ props.row.item.number }} - {{ props.row.item.type.name }}</div>

                        </router-link>

                        <div>{{ props.row.item.title }}</div>


                    </q-td>

                    <!-- ACTIONS COLUMN -->
                    <q-td key="actions" :props="props">
                        <div class="float-right">
                            <q-btn dense round flat color="grey" name="calendar" @click="downloadICS(props.row)" icon="sym_o_calendar_add_on">
                                <q-tooltip class="bg-black">Ajouter au calendrier</q-tooltip>
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
            <div>store.events</div>
            <div>{{ store.events }}</div>
        </div>

        <!-- DELETE DIALOG -->
        <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

    </div>
</template>

<script>
import { store } from '../store/store.js'
import { downloadICS } from '../store/shared.js'
import DeleteDialog from '../components/DeleteDialog.vue'


export default {
    name: 'EventsList',
    components: { DeleteDialog },
    props: { 'title': String },
    emits: [],
    data() {
        return {
            store,
            selected: null,
            searchString: "",
            filter: "",
            dialog: { deletion: false },
            data: null,
            rows: [],
            loading: false,
            pagination: {
                sortBy: "date",
                descending: true,
                page: 1,
                rowsPerPage: 20,
            },
            columns: [
                {
                    name: "date",
                    align: "left",
                    label: "Date",
                    field: "date",
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
                    name: "item",
                    align: "left",
                    label: "Objet",
                    field: "item",
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
    async created() {

        this.loading = true
        this.data = await store.getEvents("", "", this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
        this.rows = this.data.results
        this.pagination.rowsNumber = this.data.nrows
        this.loading = false

    },
    methods: {
        downloadICS,
        async onRequest(props) {

            this.loading = true
            let { page, rowsPerPage, sortBy, descending } = props.pagination
            // let filter = props.filter
            rowsPerPage = rowsPerPage === 0 ? this.pagination.rowsNumber : rowsPerPage // rowsPerPage
            this.data = await store.getEvents("", "", page, rowsPerPage, sortBy, descending)
            this.rows = this.data.results

            // update pagination object
            this.pagination = props.pagination
            this.loading = false

        },
        async query() {

            this.loading = true
            if (this.searchString.length >= 3) {
                this.data = await store.getEvents(this.searchString, "", this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
            } else {
                this.data = await store.getEvents("", "", this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
            }
            this.rows = this.data.results
            this.loading = false
        },
        handleDeletion(val) {
            this.selected = val
            this.dialog.deletion = true
        },
        async remove() {

            // console.log(`delete ${this.selected}`)
            this.loading = true
            let message = await store.deleteEvent(this.selected)
            if (message) {
                this.data = await store.getEvents(this.searchString, "", this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
                this.rows = this.data.results
            }
            this.loading = false

        }
    }
}
</script>
<style scoped></style>
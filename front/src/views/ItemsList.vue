<template>
    <div class="q-pa-sm q-gutter-sm">

        <!-- BREADCRUMBS NAVIGATION -->
        <q-breadcrumbs style="font-size: 16px">
            <q-breadcrumbs-el label="Objets parlementaires" to="/items" />
        </q-breadcrumbs>

        <div class="row q-col-gutter-md q-px-sm q-mt-xs items-center">

            <!-- SEARCH ITEMS FIELD -->
            <div class="col-xs-12 col-sm-8 col-md-6 col-lg-6">

                <q-input class="q-pa-none q-ma-none" bg-color="white" v-model="filter.search" outlined dense placeholder="Rechercher (n° ou titre)"> <!-- @update:model-value="query()"-->
                    <template v-slot:prepend>
                        <q-icon name="sym_o_search" />
                    </template>

                    <template v-slot:append>
                        <q-spinner color="blue-grey" :thickness="3" v-if="loading" />

                        <q-btn unelevated no-caps icon="sym_o_filter_alt" dense padding="xs" label="Filtres" @click="handleFilter()">
                            <q-tooltip class="bg-black">Filtrer</q-tooltip>
                        </q-btn>

                        <q-btn unelevated dense icon="close" @click="reset">
                            <q-tooltip class="bg-black">Réinitialiser</q-tooltip>
                        </q-btn>
                    </template>

                </q-input>
            </div>

            <!-- BUTTONS -->
            <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6" v-if="store.user.is_manager">
                <div class="q-gutter-x-md">

                    <!-- ADD NEW ITEM BUTTON -->
                    <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" to="/items/new">
                        <q-tooltip class="bg-black">Ajouter un nouvel objet parlementaire</q-tooltip>
                    </q-btn>

                    <!-- DOWNLOAD ITEM LIST BUTTON -->
                    <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_download" label="Télécharger" :href="`${store.host}/api/item/download/`">
                        <!-- <q-btn round padding="sm" unelevated no-caps color="blue-grey-8" icon="download" :href="`${store.host}/api/item/download/`">-->
                        <q-tooltip class="bg-black">Télécharger la liste Excel de tous les objets parlementaires</q-tooltip>
                    </q-btn>

                </div>
            </div>
        </div>

        <!-- ITEMS TABLE -->
        <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" @request="onRequest" binary-state-sort class="q-my-lg"> <!-- :filter="filter" -->

            <!-- TABLE BODY -->
            <template v-slot:body="props">
                <q-tr :props="props">

                    <!-- STATUS COLUMN -->
                    <q-td key="status" :props="props">

                        <!--
                    <q-avatar rounded size="58px" v-if="props.row.islate">
                        <img src="img/kermit-panicking.gif">
                    </q-avatar>
                    -->

                        <!-- <q-badge floating color="yellow" text-color="black">retard</q-badge> -->


                        <div class="q-gutter-xs">
                            <q-badge color="red" class="q-my-sm" v-if="props.row.urgent">Urgent</q-badge>
                            <q-badge color="yellow" text-color="black" class="q-my-sm blink" v-if="props.row.late"> Retard</q-badge>
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

                        <div>Auteur: {{ props.row.author }}</div>
                        <div>Lead: {{ props.row.lead }}</div>
                        <div>Support: {{ props.row.support.join(", ") }}</div>

                    </q-td>
                    <!-- START DATE (DEPOSIT) DATE COLUMN -->
                    <q-td key="startdate" :props="props">
                        {{ props.row.startdate }}
                    </q-td>
                    <!-- END DATE (DELAY) DATE COLUMN -->
                    <q-td key="enddate" :props="props">
                        {{ props.row.enddate }}
                    </q-td>
                    <!-- ACTIONS COLUMN -->
                    <q-td key="actions" :props="props">
                        <div class="float-right">
                            <q-btn dense round flat color="red" name="delete" @click="handleDeletion(props.row.id)" icon="sym_o_delete" v-if="store.user.is_manager">
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

        <!-- DELETE DIALOG -->
        <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

        <!-- FILTER DIALOG -->
        <ItemFilterDialog ref="didi" v-model:show="dialog.filter" v-model:filter="filter"></ItemFilterDialog>

        <!--
        <q-dialog v-model="dialog.filter">
            <ItemFilterDialog v-model="filter"></ItemFilterDialog>
        </q-dialog>
        -->

    </div>
</template>

<script>
import { store } from '../store/store.js'
import DeleteDialog from '../components/DeleteDialog.vue'
import ItemFilterDialog from './ItemFilterDialog.vue'

export default {
    name: 'ItemsList',
    components: { DeleteDialog, ItemFilterDialog },
    props: { 'title': String },
    emits: [],
    data() {
        return {
            store,
            selected: null,
            enableWatch: false,
            filter: { search: "", number: "", title: "", status: [], type: [] },
            dialog: { deletion: false, filter: false },
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
                    style: 'max-width: 600px; width: 500px;white-space: normal;',
                },
                {
                    name: "startdate",
                    align: "left",
                    label: "Dépôt",
                    field: "events",
                    sortable: true,
                },
                {
                    name: "enddate",
                    align: "left",
                    label: "Délai retour sec. gén.",
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
    watch: {
        filter: {
            handler(newValue, oldValue) {
                // console.log(`${this.$options.name} | filter()`)
                if (this.enableWatch) {
                    this.query()
                }
            },
            deep: true
        },
    },
    async created() {

        // initialize filters
        this.filter.type = (await store.getItemTypes()).map(x => x.id)
        this.filter.status = (await store.getItemStatus()).map(x => x.id)
        this.filter.service = (await store.getEntities({ search: "", type: [], service: "true" }, 1, 20, "name", "false")).results.map(x => x.id)

        this.enableWatch = true;

        // this.query()

    },
    methods: {
        async onRequest(props) {

            // update pagination object
            this.pagination = props.pagination
            this.pagination.rowsPerPage = props.pagination.rowsPerPage === 0 ? this.pagination.rowsNumber : props.pagination.rowsPerPage // rowsPerPage

            // update table rows
            this.query()

        },
        async query() {

            this.loading = true
            this.data = await store.getItems(this.filter, this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
            this.rows = this.data.results
            this.pagination.rowsNumber = this.data.nrows
            this.loading = false

        },
        handleDeletion(val) {

            this.selected = val
            this.dialog.deletion = true

        },
        handleFilter() {

            this.dialog.filter = true

        },
        async remove() {

            // console.log(`delete ${this.selected}`)
            let message = await store.deleteItem(this.selected)
            if (message) {
                this.query()
            }

        },
        reset() {
            this.$refs.didi.resetall()
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
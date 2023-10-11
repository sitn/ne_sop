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
            <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" class="q-my-lg"> <!-- :filter="filter" -->

                <!-- TABLE BODY -->
                <template v-slot:body="props">
                    <q-tr :props="props">

                        <!-- STATUS COLUMN -->
                        <q-td key="status" :props="props">
                            <div>
                                <q-badge color="red" class="q-my-sm" v-if="props.row.urgent">Urgent</q-badge>
                            </div>
                            <div>
                                <q-badge :color="color(props.row.status)" rounded class="q-mr-sm" /> {{ props.row.status }}
                            </div>
                        </q-td>

                        <!-- NUMBER COLUMN -->
                        <q-td key="number" :props="props">
                            {{ props.row.number }}
                        </q-td>
                        <!-- TYPE COLUMN -->
                        <q-td key="type" :props="props">
                            {{ props.row.type }}
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
                        </q-td>
                        <!-- DELAY DATE COLUMN -->
                        <q-td key="delay" :props="props">
                            <!-- {{ props.row.events.find((e) => e.eventType === "Délai").date }} -->
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

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

        </div>

    </div>
</template>

<script>
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import DeleteDialog from '../components/DeleteDialog.vue'

export default {
    name: 'ItemsList',
    components: { DeleteDialog },
    props: { 'title': String, 'model': Object },
    emits: [],
    setup() {
        return {
            // model: ref(null),
        }
    },
    data() {
        return {
            store,
            selected: null,
            searchString: null,
            filter: "",
            dialog: { deletion: false },
            rows: store.items,
            loading: false,
            pagination: {
                sortBy: "desc",
                descending: false,
                page: 1,
                rowsPerPage: 20,
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
    created() {
    },
    mounted() {

    },
    methods: {
        async query() {
            // TODO: REPLACE WITH GET CALL TO DATABASE 
            this.loading = true
            await sleep(Math.random() * 1300)
            let str = this.searchString.toLowerCase()
            if (this.searchString.length >= 3) {
                this.rows = this.store.items.filter((x) => (x.title.toLowerCase().includes(str) || x.number.toLowerCase().includes(str)))
            } else {
                this.rows = this.store.items
            }
            this.loading = false
        },
        handleDeletion(val) {
            this.selected = val
            this.dialog.deletion = true
        },
        async remove() {
            store.items = store.items.filter((x) => (x.id !== this.selected))
            this.rows = store.items
        },
        addItem() {
            // this.addDialog = true
        },
        color(val) {
            switch (val) {
                case 'Pas traité':
                    return 'red'
                case 'En traitement':
                    return 'orange'
                case 'Terminé':
                    return 'green'
                default:
                    return 'grey'
            }
        },
    }

}
</script>

<style scoped></style>
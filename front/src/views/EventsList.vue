<template>
    <div class="">

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
                            <q-btn unelevated icon="sym_o_filter_alt" padding="xs" @click="console.log('filter')"> <!-- color="orange-1" text-color="black" -->
                                <q-tooltip class="bg-black">Filtrer</q-tooltip>
                            </q-btn>
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
            <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" :filter="filter" class="q-my-lg">
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
                            {{ props.row.eventType }}
                        </q-td>

                        <!-- ITEM COLUMN -->
                        <q-td key="item" :props="props">

                            <router-link :to="{
                                name: 'Item',
                                params: {
                                    id: props.row.itemId
                                }
                            }">
                                <div>{{ props.row.itemNumber }} - {{ props.row.itemType }}</div>

                            </router-link>
                            <div>{{ props.row.itemName }}</div>

                        </q-td>

                        <!-- ACTIONS COLUMN -->
                        <q-td key="actions" :props="props">
                            <div class="float-right">
                                <q-btn dense round flat color="grey" name="calendar" @click="downloadICS(props.row)" icon="sym_o_calendar_add_on">
                                    <q-tooltip class="bg-black">Ajouter au calendrier</q-tooltip>
                                </q-btn>
                                <!-- 
                                <q-btn href="data:,I am text file" download="a122.txt" dense round flat color="grey" name="calendar" @click="" icon="sym_o_calendar_add_on">
                                    <q-tooltip class="bg-black">Ajouter au calendrier</q-tooltip>
                                </q-btn>
                                -->
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
import { downloadICS } from '../store/shared.js'
// import items from '../assets/data/items.json'
// import events from '../assets/data/events.json'
// import * as ics from 'ics'
// import { createEvent } from 'ics'
import DeleteDialog from '../components/DeleteDialog.vue'

//console.log(items.map(e => (e.events)).flat())

export default {
    name: 'EventsList',
    components: { DeleteDialog },
    props: { 'title': String }, // 'rows': items
    emits: [],
    setup() {
        return {}
    },
    data() {
        return {
            store,
            selected: null,
            searchString: null,
            filter: "",
            dialog: { deletion: false },
            rows: store.events,
            loading: false,
            pagination: {
                sortBy: "desc",
                descending: false,
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
                    field: "eventType",
                    sortable: true,
                },
                {
                    name: "item",
                    align: "left",
                    label: "Objet",
                    field: "",
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
        // console.log(store.items.map((x) => (x.events)).flat(1))
    },
    methods: {
        downloadICS,
        handleDeletion(val) {
            this.selected = val
            this.dialog.deletion = true
        },
        async remove() {
            store.events = store.events.filter((x) => (x.id !== this.selected))
            this.rows = store.events
        }
    }
}
</script>
<style scoped></style>
<template>
    <div class="">

        <!-- BREADCRUMBS NAVIGATION -->
        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Calendrier" to="/events" />
            </q-breadcrumbs>
        </div>

        <!-- EVENTS TABLE -->
        <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" :filter="filter" dense class="q-my-lg">
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
                            <q-btn dense round flat color="grey" name="calendar" @click="console.log(props.row.date)" icon="sym_o_calendar_add_on">
                                <q-tooltip class="bg-black">Ajouter au calendrier</q-tooltip>
                            </q-btn>
                            <q-btn dense round flat color="red" name="delete" @click="console.log(props.row.id)" icon="sym_o_delete">
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

    </div>
</template>

<script>
// import items from '../assets/data/items.json'
import events from '../assets/data/events.json'

//console.log(items.map(e => (e.events)).flat())

export default {
    name: 'EventsList',
    components: {},
    props: { 'title': String, 'model': Object }, // 'rows': items
    emits: [],
    setup() {
        return {
            // model: ref(null),
        }
    },
    data() {
        return {
            rows: events,
            loading: false,
            filter: "",
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
    mounted() {

    },
    methods: {
    }
}
</script>

<style scoped>
.material-symbols-outlined {
    font-variation-settings:
        'FILL' 1,
        'wght' 400,
        'GRAD' 0,
        'opsz' 24
}
</style>
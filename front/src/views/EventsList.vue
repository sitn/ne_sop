<template>
    <div class="">

        <!-- BREADCRUMBS NAVIGATION -->
        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Calendrier" to="/events" />
            </q-breadcrumbs>
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
import { store } from '../store/store.js'
// import items from '../assets/data/items.json'
import events from '../assets/data/events.json'
// import * as ics from 'ics'
import { createEvent } from 'ics';


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
            store,
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
    created() {
    },
    mounted() {

    },
    methods: {

        async downloadICS(val) {

            console.log('download ICS')
            console.log(val)

            // const extract = date => val.date.toISOString().split(/[^0-9]/).slice(0, -1)
            let date = new Date(val.date)
            console.log(date)

            let dateArray = [date.getFullYear(), date.getMonth() + 1, date.getDate()]
            console.log(dateArray)

            let event = {
                start: dateArray, // Date.parse(val.date), //  [2018, 5, 30, 6, 30],
                duration: { hours: 1, minutes: 0 },
                title: `Objet parlementaire ${val.itemNumber}`,
                description: '',
                location: '',
                /*
                url: 'http://www.bolderboulder.com/',
                geo: { lat: 40.0095, lon: 105.2669 },
                categories: ['10k races', 'Memorial Day Weekend', 'Boulder CO'],
                status: 'CONFIRMED',
                busyStatus: 'BUSY',
                organizer: { name: 'Admin', email: 'Race@BolderBOULDER.com' },
                attendees: [
                    { name: 'Adam Gibbons', email: 'adam@example.com', rsvp: true, partstat: 'ACCEPTED', role: 'REQ-PARTICIPANT' },
                    { name: 'Brittany Seaton', email: 'brittany@example2.org', dir: 'https://linkedin.com/in/brittanyseaton', role: 'OPT-PARTICIPANT' }
                ]
                */
            }

            const filename = 'sop.ics'
            const file = await new Promise((resolve, reject) => {
                createEvent(event, (error, value) => {
                    if (error) {
                        reject(error)
                    }

                    resolve(new File([value], filename, { type: 'text/calendar' }))
                })
            })
            const url = URL.createObjectURL(file);

            // trying to assign the file URL to a window could cause cross-site
            // issues so this is a workaround using HTML5
            const anchor = document.createElement('a');
            anchor.href = url;
            anchor.download = filename;

            document.body.appendChild(anchor);
            anchor.click();
            document.body.removeChild(anchor);

            URL.revokeObjectURL(url);
        },
        /*
        downloadICS(val) {

            console.log(val)

            let event = {
                start: [2018, 5, 30, 6, 30],
                duration: { hours: 6, minutes: 30 },
                title: 'Bolder Boulder',
                description: 'Annual 10-kilometer run in Boulder, Colorado',
                location: 'Folsom Field, University of Colorado (finish line)',
                url: 'http://www.bolderboulder.com/',
                geo: { lat: 40.0095, lon: 105.2669 },
                categories: ['10k races', 'Memorial Day Weekend', 'Boulder CO'],
                status: 'CONFIRMED',
                busyStatus: 'BUSY',
                organizer: { name: 'Admin', email: 'Race@BolderBOULDER.com' },

            }

            ics.createEvent(event, (error, value) => {
                if (error) {
                    console.log(error)
                    return
                }
                window.open("data:text/calendar;charset=utf8," + value);
                console.log(value)
            })

        }
        */

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
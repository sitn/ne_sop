<template>
    <!-- EVENTS TABLE -->
    <q-table :rows="events" :columns="eventsColumns" row-key="date" class="q-my-md">
        <template v-slot:body="props">
            <q-tr :props="props">
                <q-td key="date" :props="props">
                    {{ props.row.date }}
                </q-td>
                <q-td key="time" :props="props">
                    {{ props.row.time }}
                </q-td>
                <q-td key="type" :props="props">
                    {{ props.row.eventType }}
                </q-td>
                <q-td key="actions" :props="props">
                    <q-btn dense round flat color="red" name="delete" @click="console.log(props.row)" icon="sym_o_delete" :disable="!edit">
                        <q-tooltip class="bg-black">Supprimer</q-tooltip>
                    </q-btn>
                </q-td>
            </q-tr>
        </template>
    </q-table>

    <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
        {{ events }}
    </div>
</template>


<script>
import { store } from '../store/store.js'
import NewEventDialog from "../views/NewEventDialog.vue"

const eventsColumns = [
    { name: "date", align: "left", label: "Date", field: "date", sortable: true },
    { name: "time", align: "left", label: "Heure", field: "", sortable: true },
    { name: "type", align: "left", label: "Type", field: "eventType", sortable: true },
    { name: "actions", align: "right", label: "", field: "", sortable: false }
]

export default {
    name: 'EventsTable',
    components: { NewEventDialog },
    props: { 'events': Object, 'edit': Boolean, 'modelValue': Object },
    emits: [],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            dialog: { newEvent: false },
            eventsColumns: eventsColumns,
        }
    },
    computed: {
    },
    created() {
    },
    mounted() {
    },
    methods: {
        addEvent() {
            // this.dialog.newEvent = true
        },
    }
}
</script>

<style scoped></style>
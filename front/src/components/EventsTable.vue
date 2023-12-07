<template>
    <div class="row q-px-none q-my-md items-center">

        <!-- ADD NEW EVENT BUTTON -->
        <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6">
            <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" @click="addEvent()" :disable="!edit">
                <q-tooltip class="bg-black">Ajouter un évenement au calendrier</q-tooltip>
            </q-btn>
        </div>

    </div>

    <!-- EVENTS TABLE -->
    <q-table :rows="events" :columns="columns" row-key="date" class="q-my-md">
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
                    <div class="float-right">
                        <q-btn dense round flat color="grey" name="calendar" @click="downloadICS(props.row)" icon="sym_o_calendar_add_on" :disable="!edit">
                            <q-tooltip class="bg-black">Ajouter au calendrier</q-tooltip>
                        </q-btn>
                        <q-btn dense round flat color="red" name="delete" @click="handleDeletion(props.row.id)" icon="sym_o_delete" :disable="!edit">
                            <q-tooltip class="bg-black">Supprimer</q-tooltip>
                        </q-btn>
                    </div>
                </q-td>
            </q-tr>
        </template>
    </q-table>

    <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
        {{ events }}
    </div>

    <!-- ADD NEW EVENT DIALOG -->
    <q-dialog v-model="dialog.newEvent">
        <NewEventDialog v-model="events"></NewEventDialog>
    </q-dialog>

    <!-- DELETE EVENT DIALOG -->
    <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />
</template>

<script>
import { store } from '../store/store.js'
import { downloadICS } from '../store/shared.js'
import NewEventDialog from "../views/NewEventDialog.vue"
import DeleteDialog from './DeleteDialog.vue'

const columns = [
    { name: "date", align: "left", label: "Date", field: "date", sortable: true },
    { name: "time", align: "left", label: "Heure", field: "", sortable: true },
    { name: "type", align: "left", label: "Type", field: "eventType", sortable: true },
    { name: "actions", align: "right", label: "", field: "", sortable: false }
]

export default {
    name: 'EventsTable',
    components: { NewEventDialog, DeleteDialog },
    props: { 'edit': Boolean, 'modelValue': Object }, //  'events': Object,
    emits: ['update:modelValue'],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            selected: null,
            dialog: { newEvent: false, deletion: false },
            columns: columns,
        }
    },
    computed: {
        events: {
            get() {
                return this.modelValue
            },
            set(events) {
                this.$emit('update:modelValue', events)
            }
        }
    },
    created() {
    },
    mounted() {
    },
    methods: {
        downloadICS,
        addEvent() {
            this.dialog.newEvent = true
        },
        handleDeletion(val) {
            this.selected = val
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: REPLACE WITH GET CALL TO API
            console.log(`delete ${this.selected}`)
            let message = await store.deleteEvent(this.selected)
            if (message) {
                this.events = this.events.filter((x) => (x.id !== this.selected))
            }
            console.log(message)

            // store.events = store.events.filter((x) => (x.id !== this.selected))
            // this.rows = store.events
            // this.events = this.events.filter((x) => (x.id !== this.selected))
        }
    }
}
</script>

<style scoped></style>
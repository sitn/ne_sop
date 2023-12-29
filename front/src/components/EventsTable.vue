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
    <q-table :rows="events" :columns="columns" row-key="date" @request="onRequest" binary-state-sort class="q-my-md" v-if="eventTypes.length > 0">
        <template v-slot:body="props">
            <q-tr :props="props">
                <q-td key="date" :props="props">
                    {{ props.row.date }}
                </q-td>
                <q-td key="time" :props="props">
                    {{ props.row.time }}
                </q-td>
                <q-td key="type" :props="props">
                    {{ getEventTypeName(props.row.type) }}
                </q-td>
                <q-td key="description" :props="props">
                    {{ props.row.description }}
                </q-td>
                <q-td key="actions" :props="props">
                    <div class="float-right">
                        <q-btn dense round flat color="grey" name="calendar" @click="downloadICS(props.row)" icon="sym_o_calendar_add_on" :disable="!edit">
                            <q-tooltip class="bg-black">Ajouter au calendrier</q-tooltip>
                        </q-btn>
                        <q-btn dense round flat color="blue" name="delete" @click="handleEdition(props.row)" icon="sym_o_edit" :disable="!edit">
                            <q-tooltip class="bg-black">Modifier</q-tooltip>
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
    <q-dialog v-model="dialog.add">
        <NewEventDialog v-model="events"></NewEventDialog>
    </q-dialog>

    <!-- EDIT EVENT DIALOG -->
    <q-dialog v-model="dialog.edit">
        <EditEventDialog v-model="selected"></EditEventDialog>
    </q-dialog>

    <!-- DELETE EVENT DIALOG -->
    <DeleteDialog v-model="dialog.delete" @delete-event="remove" />
</template>

<script>
import { store } from '../store/store.js'
import { downloadICS } from '../store/shared.js'
import NewEventDialog from "../views/NewEventDialog.vue"
import EditEventDialog from "../views/EditEventDialog.vue"
import DeleteDialog from './DeleteDialog.vue'

const columns = [
    { name: "date", align: "left", label: "Date", field: "date", sortable: true },
    { name: "time", align: "left", label: "Heure", field: "", sortable: true },
    { name: "type", align: "left", label: "Type", field: "eventType", sortable: true },
    { name: "description", align: "left", label: "Note", field: "description", sortable: false },
    { name: "actions", align: "right", label: "", field: "", sortable: false }
]

export default {
    name: 'EventsTable',
    components: { NewEventDialog, EditEventDialog, DeleteDialog },
    props: { 'item': Number, 'edit': Boolean, 'modelValue': Object },
    emits: ['update:modelValue'],
    data() {
        return {
            store,
            selected: null,
            dialog: { add: false, delete: false, edit: false },
            eventTypes: [],
            data: null,
            rows: [],
            columns: columns,
            loading: true,
            render: false,
            pagination: {
                sortBy: "date",
                descending: false,
                page: 1,
                rowsPerPage: 20,
            },
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
    async created() {

        this.eventTypes = await this.store.getEventTypes()
        this.render = true
        this.loading = true
        this.data = await store.getEvents("", this.item, this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
        this.rows = this.data.results
        this.pagination.rowsNumber = this.data.nrows
        this.loading = false

    },
    methods: {
        downloadICS,
        async onRequest(props) {

            this.loading = true

            // console.log('onRequest')
            // console.log(props.pagination)
            let { page, rowsPerPage, sortBy, descending } = props.pagination
            // let filter = props.filter
            // console.log(`page: ${page}, rowsPerPage: ${rowsPerPage}, sortBy: ${sortBy}, descending: ${descending}`)

            rowsPerPage = rowsPerPage === 0 ? this.pagination.rowsNumber : rowsPerPage

            this.data = await store.getEvents("", this.item, page, rowsPerPage, sortBy, descending)
            this.rows = this.data.results

            // update pagination object
            this.pagination = props.pagination
            this.loading = false

        },
        addEvent() {
            this.dialog.add = true
        },
        handleDeletion(val) {
            this.selected = val
            this.dialog.delete = true
        },
        handleEdition(val) {
            this.selected = val
            this.dialog.edit = true
        },
        async remove() {

            this.events = this.events.filter((x) => (x.id !== this.selected))

            /*
            // Delete event in DB
            console.log(`delete ${this.selected}`)
            let message = await store.deleteEvent(this.selected)
            if (message) {
                this.events = this.events.filter((x) => (x.id !== this.selected))
            }
            console.log(message)
            */

            // store.events = store.events.filter((x) => (x.id !== this.selected))
            // this.rows = store.events

        },
        getEventTypeName(id) {
            return this.eventTypes.find((x) => x.id === id).name
        }
    }
}
</script>

<style scoped></style>
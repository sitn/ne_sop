<template>
    <div class="">

        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Calendrier" to="/events" />
                    <q-breadcrumbs-el :label="event.date" />
                </q-breadcrumbs>
            </div>

            <!-- FORM -->
            <EventForm v-model="event" :edit="edit"></EventForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="false" :wait="wait" :buttons="{ 'save': true, 'deletion': true }" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode"></FloatingButtons>

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />


        </q-layout>
    </div>
</template>

<script>
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import eventTypes from '../assets/data/event-types.json'
import FloatingButtons from "../components/FloatingButtons.vue"
import DeleteDialog from '../components/DeleteDialog.vue'
import EventForm from "../components/EventForm.vue"

export default {
    name: 'Event',
    components: { FloatingButtons, DeleteDialog, EventForm },
    props: {},
    emits: [],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            dialog: { deletion: false },
            edit: false,
            wait: false,
            event: null, // store.events.find(e => e.id === this.$route.params.id),
            items: store.items,
            eventDate: null,
            eventTime: null,
            eventTypes: eventTypes,
            linkedItem: null,
        }
    },
    computed: {
    },
    created() {
        this.event = Object.assign({}, store.events.find(e => e.id === this.$route.params.id))
    },
    mounted() {
    },
    methods: {
        async save() {
            // TODO: POST RECORD TO DATABASE
            console.log(`${this.$options.name}.vue | save()`)
            this.wait = true
            await sleep(Math.random() * 1300)
            // store.items.filter((x) => (x.events.findIndex(y => (y.id) === this.event.id))) = this.event
            // store.items.find((x) => (x.events.findIndex((y) => (y.id === this.event.id))))
            store.items.forEach((x, j) => {
                let k = x.events.findIndex(y => (y.id === this.event.id))
                if (k !== -1) {
                    store.items[j].events[k] = Object.assign({}, this.event)
                    store.updateEvents()
                }
            })
            this.wait = false
        },
        handleDeletion() {
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: DELETE RECORD IN DATABASE
            console.log(`${this.$options.name}.vue | remove()`)
            // store.entities.splice(this.index, 1)
            this.$router.push({ name: 'EventsList' })
        },
        setEditMode(val) {
            console.log(`${this.$options.name}.vue | setEditMode(${val})`)
            this.edit = val
        },
        setLinkedItem() {

        }
    }
}
</script>

<style scoped></style>
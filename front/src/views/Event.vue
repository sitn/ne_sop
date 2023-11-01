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

            <!--  <div>valid: {{ valid }}</div> -->
            <!--  <div>store.valid: {{ store.valid }}</div> -->

            <!-- FORM -->
            <EventForm v-model="event" :edit="edit" @validation-event="handleValidation"></EventForm>
            <!-- <EventForm v-model="event" :edit="edit" @validation-event="handleValidation" ref="EventForm"></EventForm> -->

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode"></FloatingButtons>

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

        </q-layout>
    </div>
</template>

<script>
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
// import eventTypes from '../assets/data/event-types.json'
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
            // actionButtons: { save: 'active', deletion: 'active' },
            edit: false,
            wait: false,
            valid: null,
            event: null, // store.events.find(e => e.id === this.$route.params.id),
            index: store.events.findIndex((e) => (e.id === this.$route.params.id))
        }
    },
    computed: {
        actionButtons() {
            return {
                save: this.event.valid ? 'active' : 'disable',
                deletion: 'none'
            }
        }
    },
    created() {
        this.event = Object.assign({}, store.events.find(e => e.id === this.$route.params.id))
    },
    mounted() {
        store.valid ? this.actionButtons.save = 'active' : this.actionButtons.save = 'disable'
    },

    methods: {
        /*
        validate() {
            console.log('this.$refs.EventForm.validateForm()')
            this.$refs.EventForm.validateForm()
        },
        */
        async save(redirectTo) {

            // TODO: POST RECORD TO DATABASE
            console.log(`${this.$options.name} | save()`)
            this.wait = true
            await sleep(Math.random() * 1300)
            // store.items.filter((x) => (x.events.findIndex(y => (y.id) === this.event.id))) = this.event
            // store.items.find((x) => (x.events.findIndex((y) => (y.id === this.event.id))))
            store.items.forEach((x, j) => {
                let k = x.events.findIndex(y => (y.id === this.event.id))
                if (k !== -1) {
                    store.items[j].events[k] = Object.assign({}, this.event)
                    // store.updateEvents()
                }
            })
            store.events[this.index] = Object.assign({}, this.event)

            this.wait = false

            if (redirectTo !== null) {
                this.$router.push({ path: redirectTo })
            }

        },
        handleValidation(val) {

            this.valid = val
            //this.valid ? this.actionButtons.save = 'active' : this.actionButtons.save = 'disable'

            // store.valid ? this.actionButtons.save = 'active' : this.actionButtons.save = 'disable'
            console.log(`${this.$options.name} | handleValidation()`)
            // this.actionButtons.save = 'disable'
        },
        handleDeletion() {
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: DELETE RECORD IN DATABASE
            console.log(`${this.$options.name} | remove()`)
            store.events.splice(this.index, 1)
            this.$router.push({ name: 'EventsList' })
        },
        setEditMode(val) {
            console.log(`${this.$options.name} | setEditMode(${val})`)
            this.edit = val
            // this.$refs.EventForm.validateForm()
        }
    }
}
</script>

<style scoped></style>
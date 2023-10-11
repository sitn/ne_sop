<template>
    <div class="">

        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Calendrier" to="/events" />
                    <q-breadcrumbs-el label="Nouvel événement" />
                </q-breadcrumbs>
            </div>

            <!--  <div>valid: {{ valid }}</div> -->
            <!--  <div>store.valid: {{ store.valid }}</div> -->

            <!-- FORM -->
            <EventForm v-model="event" :edit="edit" @validation-event="handleValidation"></EventForm>
            <!-- <EventForm v-model="event" :edit="edit" @validation-event="handleValidation" ref="EventForm"></EventForm> -->

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @edit-event="setEditMode"></FloatingButtons>

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

        </q-layout>
    </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
// import eventTypes from '../assets/data/event-types.json'
import FloatingButtons from "../components/FloatingButtons.vue"
import DeleteDialog from '../components/DeleteDialog.vue'
import EventForm from "../components/EventForm.vue"

export default {
    name: 'NewEvent',
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
            // actionButtons: {},
            edit: true,
            wait: false,
            valid: null,
            event: {
                "id": uuidv4(),
                "itemId": "",
                "itemNumber": "",
                "itemName": "",
                "itemType": "",
                "eventType": "",
                "date": "",
                "time": "",
                "status": "",
                "statusGrandConseil": "",
                "description": "",
                "valid": false
            }, // store.events.find(e => e.id === this.$route.params.id),
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
    },
    mounted() {
        // this.valid ? this.actionButtons.save = 'active' : this.actionButtons.save = 'disable'
        // store.valid ? this.actionButtons.save = 'active' : this.actionButtons.save = 'disable'
    },

    methods: {
        async save() {

            // this.$refs.EventForm.validateForm() // VALIDATE FORM

            // TODO: POST RECORD TO DATABASE
            console.log(`${this.$options.name} | save()`)
            // console.log(`${this.$options.name} | this.$refs.EventForm.valid = ${this.$refs.EventForm.valid}`)

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

            store.events.push(Object.assign({}, this.event))
            this.wait = false
            this.$router.push({ name: 'EventsList' })
        },
        handleValidation(val) {
            this.valid = val
            this.valid ? this.actionButtons.save = 'active' : this.actionButtons.save = 'disable'
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
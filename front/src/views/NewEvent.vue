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

            <!-- FORM -->
            <EventForm v-model="event" :edit="edit" @validation-event="handleValidation" ref="EventForm"></EventForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="floatingButtons" @save-event="save" @edit-event="setEditMode"></FloatingButtons>

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
            floatingButtons: { save: 'active', deletion: 'none' },
            edit: true,
            wait: false,
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
                "description": ""
            }, // store.events.find(e => e.id === this.$route.params.id),
            index: store.events.findIndex((e) => (e.id === this.$route.params.id))
        }
    },
    created() {
        // this.event = Object.assign({}, store.events.find(e => e.id === this.$route.params.id))
    },
    mounted() {
    },
    watch: {
        event: {
            handler(newValue, oldValue) {
                // Note: `newValue` will be equal to `oldValue` here
                // on nested mutations as long as the object itself
                // hasn't been replaced.
                console.log(`${this.$options.name}.vue | event watcher`)
                console.log('this.$refs.EventForm.valid')

                // this.$refs.EventForm.validateForm()
                console.log(this.$refs.EventForm.valid)

            },
            deep: true
        }
    },
    methods: {
        async save() {

            this.$refs.EventForm.validateForm()

            console.log('this.$refs.EventForm.valid')
            console.log(this.$refs.EventForm.valid)

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

            store.events.push(Object.assign({}, this.event))
            this.wait = false
        },
        handleValidation(val) {
            console.log(`${this.$options.name}.vue | handleValidation()`)
            this.floatingButtons.save = 'disable'
        },
        handleDeletion() {
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: DELETE RECORD IN DATABASE
            console.log(`${this.$options.name}.vue | remove()`)
            store.events.splice(this.index, 1)
            this.$router.push({ name: 'EventsList' })
        },
        setEditMode(val) {
            console.log(`${this.$options.name}.vue | setEditMode(${val})`)
            this.edit = val
        }
    }
}
</script>

<style scoped></style>
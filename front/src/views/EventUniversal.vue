<template>
    <div class="" v-if="!store.loading">

        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Calendrier (Universal)" to="/events" />
                    <q-breadcrumbs-el :label="event.date" />
                </q-breadcrumbs>
            </div>

            <!-- FORM -->
            <EventForm v-model="event" :edit="edit"></EventForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode"></FloatingButtons>

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

        </q-layout>
    </div>
</template>

<script>
import { store } from '../store/store.js'
import FloatingButtons from "../components/FloatingButtons.vue"
import DeleteDialog from '../components/DeleteDialog.vue'
import EventForm from "../components/EventForm.vue"

export default {
    name: 'EventUniversal',
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
            loading: true,
            edit: false,
            wait: false,
            valid: null,
            event: {
                "date": "",
                "time": "",
                "item": null,
                "type": "",
                "description": "",
                "valid": false
            },
            // index: store.events.findIndex((e) => (e.id === this.$route.params.id))
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
    async created() {

        console.log(this.$route.params)
        console.log(`this.$route.params.id: ${this.$route.params.id}`)
        if (this.$route.params.hasOwnProperty('id')) {
            this.store.loading = true
            this.event = await store.getEvent(this.$route.params.id)
            this.store.loading = false
        }
        this.store.loading = false

    },
    methods: {
        async save() {

            console.log(`${this.$options.name}.vue | save()`)

            this.wait = true
            if (this.event.id) {
                this.event = await store.updateEvent(this.event.id, this.event)
            } else {
                this.event = await store.addEvent(this.event)
            }
            this.wait = false

        },
        handleValidation(val) {

            this.valid = val
            console.log(`${this.$options.name} | handleValidation()`)

        },
        handleDeletion() {
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: DELETE RECORD IN DATABASE
            console.log(`${this.$options.name} | remove()`)
            // store.events.splice(this.index, 1)
            this.$router.push({ name: 'EventsList' })
        },
        setEditMode(val) {
            console.log(`${this.$options.name} | setEditMode(${val})`)
            this.edit = val
        }
    }
}
</script>

<style scoped></style>
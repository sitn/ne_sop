<template>
    <div class="" v-if="!store.loading">
        <div v-if="event && event.id">

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
                <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode"></FloatingButtons>

                <!-- DELETE DIALOG -->
                <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

            </q-layout>
        </div>

        <div v-else>
            <NotFound></NotFound>
        </div>
    </div>
</template>

<script>
import { store } from '../store/store.js'
import FloatingButtons from "../components/FloatingButtons.vue"
import DeleteDialog from '../components/DeleteDialog.vue'
import EventForm from "../components/EventForm.vue"
import NotFound from '../components/NotFound.vue'


export default {
    name: 'Event',
    components: { FloatingButtons, DeleteDialog, EventForm, NotFound },
    props: {},
    emits: [],
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
    watch: {
        async $route(to, from) {

            if (this.$route.params.hasOwnProperty('id')) {
                this.store.loading = true
                this.event = await store.getEvent(this.$route.params.id)
                this.store.loading = false
            }
            this.store.loading = false

        }
    },
    async created() {

        // console.log(`this.$route.params.id: ${this.$route.params.id}`)
        if (this.$route.params.hasOwnProperty('id')) {
            this.store.loading = true
            this.event = await store.getEvent(this.$route.params.id)
            this.store.loading = false
        }
        this.store.loading = false

    },
    methods: {
        async save(redirectTo) {

            this.wait = true

            let response

            if (this.event.id) {
                // update existing record
                response = await store.updateEvent(this.event.id, this.event)
            } else {
                // create a new record
                response = await store.addEvent(this.event)
            }

            this.wait = false

            // update event
            if (response) {
                this.event = response
                store.event.old = JSON.stringify(this.event)
            }

            // redirection
            if (redirectTo !== null) {
                this.$router.push({ path: redirectTo })
            }

        },
        handleValidation(val) {
            this.valid = val
        },
        handleDeletion() {
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: DELETE RECORD IN DATABASE
            this.$router.push({ name: 'EventsList' })
        },
        setEditMode(val) {
            // console.log(`${this.$options.name} | setEditMode(${val})`)
            this.edit = val
        }
    }
}
</script>

<style scoped></style>
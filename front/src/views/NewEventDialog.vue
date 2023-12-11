<template>
    <q-card style="width: 700px; max-width: 80vw;">
        <q-card-section class="bg-blue-grey text-white">
            <div class="text-h6">Nouvel évenement</div>
        </q-card-section>

        <q-card-section class="row items-center scroll" style="max-height: 70vh">

            <!-- FORM -->
            <EventForm class="col" v-model="event" :edit="edit"></EventForm>
            <!-- <EventForm v-model="event" :edit="edit" @validation-event="handleValidation"></EventForm> -->

        </q-card-section>

        <q-card-actions align="right">
            <q-btn flat label="Annuler" color="primary" v-close-popup />
            <q-btn flat label="Confirmer" color="primary" @click="save()" v-close-popup :disable="!event.valid" />
        </q-card-actions>
    </q-card>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { store } from '../store/store.js'
import EventForm from "../components/EventForm.vue"

export default {
    name: 'NewEventDialog',
    components: { EventForm },
    props: { 'itemId': String, 'modelValue': Object },
    emits: ['addNewEvent'],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            edit: true,
            valid: false,
            event: {
                // "id": uuidv4(),
                // "itemId": "",
                // "itemNumber": "",
                // "itemName": "",
                // "itemType": "",
                // "eventType": "",
                //   "statusGrandConseil": "",
                "date": "",
                "time": "",
                "type": "",
                "status": "",
                "item": null,
                "description": "",
                "valid": false
            }
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
        /*
        item: {
            get() {
                return this.modelValue
            },
            set(item) {
                this.$emit('update:modelValue', item)
            }
        }
        */
    },
    mounted() {

    },
    methods: {
        save() {

            this.events.push(Object.assign({}, this.event))
            // this.item.events.push(Object.assign({}, this.event))
            // store.events.push(Object.assign({}, this.event))
            // store.items[1].events.push(Object.assign({}, this.event))
        },

    }
}
</script>

<style scoped></style>
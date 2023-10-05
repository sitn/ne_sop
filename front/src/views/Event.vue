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

            <Form title="Événement" :edit="false" :toggle="true" @edit-event="setEditMode">

                <template v-slot:body>

                    <!-- IDENTIFICATION SECTION -->
                    <FormSection title="Event">
                        <template v-slot:content>
                            <div class="text-h6">Événement</div>

                            <div class="row q-col-gutter-lg q-py-md">

                                <!-- DATE INPUT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <!--  <q-input type="date" bg-color="white" outlined v-model="eventDate" label="Date" required /> -->
                                    <q-input bg-color="white" outlined v-model="event.date" label="Date" mask="date" :rules="['date']" :disable="!edit">
                                        <template v-slot:append>
                                            <q-icon name="event" class="cursor-pointer">
                                                <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
                                                    <q-date v-model="event.date" color="blue-grey" text-color="white">
                                                        <div class="row justify-end">
                                                            <q-btn v-close-popup label="Close" color="primary" flat />
                                                        </div>
                                                    </q-date>
                                                </q-popup-proxy>
                                            </q-icon>
                                            <!-- 
                                <q-icon name="event" class="cursor-pointer">
                                    <q-popup-proxy>
                                        <q-date v-model="event.date"></q-date>
                                    </q-popup-proxy>
                                </q-icon>
                                -->
                                        </template>
                                    </q-input>
                                </div>

                                <!-- TIME INPUT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <!-- <q-input type="time" bg-color="white" outlined v-model="event.time" label="Heure" /> -->
                                    <q-input bg-color="white" outlined v-model="event.time" label="Heure" mask="time" :rules="['time']" :disable="!edit">
                                        <template v-slot:append>
                                            <q-icon name="access_time" class="cursor-pointer">
                                                <q-popup-proxy transition-show="scale" transition-hide="scale">
                                                    <q-time v-model="event.time" color="blue-grey" text-color="white">
                                                        <div class="row items-center justify-end">
                                                            <q-btn v-close-popup label="Close" color="primary" flat />
                                                        </div>
                                                    </q-time>
                                                </q-popup-proxy>
                                            </q-icon>
                                        </template>
                                    </q-input>
                                </div>

                            </div>

                            <div class="row q-col-gutter-lg">

                                <!-- TYPE SELECT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-select bg-color="white" outlined v-model="event.eventType" :options="eventTypes" label="Type" clearable :disable="!edit">
                                    </q-select>
                                </div>

                                <!-- LINKED ITEM SELECT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <!-- <q-input bg-color="white" outlined v-model="event.itemNumber" label="Objet lié" /> -->
                                    <q-select bg-color="white" outlined v-model="event.itemNumber" :options="this.items" option-label="number" option-value="number" label="Objet lié" @update:model-value="setLinkedItem()" emit-value clearable :disable="!edit">
                                        <template v-slot:option="scope">
                                            <q-item v-bind="scope.itemProps">
                                                <q-item-section>
                                                    <q-item-label>{{ scope.opt.number }} - {{ scope.opt.type }}</q-item-label>
                                                    <q-item-label caption>{{ scope.opt.title }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                        </template>
                                    </q-select>
                                </div>
                            </div>

                            <!-- DESCRIPTION TEXT AREA FIELD -->
                            <div class="row q-col-gutter-lg q-my-sm">
                                <div class="col">
                                    <q-input bg-color="white" outlined v-model="event.description" label="Description" type="textarea" :disable="!edit" />
                                </div>
                            </div>

                            <!-- TODO REMOVE/DEV DISPLAY JSON-->
                            <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                                <div>event</div>
                                <div>{{ event }}</div>
                            </div>

                            <!-- TODO REMOVE/DEV DISPLAY JSON-->
                            <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                                <div>store.event</div>
                                <div>{{ store.events.find(e => e.id === this.$route.params.id) }}</div>
                            </div>

                        </template>
                    </FormSection>

                </template>

            </Form>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="false" :wait="wait" :buttons="{ 'save': true, 'deletion': true }" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode"></FloatingButtons>

        </q-layout>
    </div>
</template>

<script>
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import eventTypes from '../assets/data/event-types.json'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"
import FloatingButtons from "../components/FloatingButtons.vue"

export default {
    name: 'Event',
    components: { Form, FormSection, FloatingButtons },
    props: {},
    emits: [],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
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
<template>
    <Form>

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
                            <q-select bg-color="white" outlined v-model="event.itemNumber" :options="this.store.items" option-label="number" option-value="number" label="Objet lié" @update:model-value="setLinkedItem()" emit-value clearable :disable="!edit">
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
</template>

<script>
import { store } from '../store/store.js'
import eventTypes from '../assets/data/event-types.json'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"

export default {
    name: 'EventForm',
    components: { Form, FormSection },
    props: { 'edit': Boolean, 'modelValue': Object },
    emits: ['update:modelValue'],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            eventTypes: eventTypes
        }
    },
    computed: {
        event: {
            get() {
                return this.modelValue
            },
            set(event) {
                this.$emit('update:modelValue', event)
            }
        }
    },
    created() {
        console.log(`router id: ${this.$route.params.id}`)
    },
    mounted() {
    },
    methods: {
    }
}
</script>

<style scoped></style>
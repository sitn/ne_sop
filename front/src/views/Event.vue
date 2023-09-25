<template>
    <div class="">

        <!-- BREADCRUMBS NAVIGATION -->
        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Événements" to="/events" />
                <q-breadcrumbs-el :label="event.date" />
            </q-breadcrumbs>
        </div>


        <Form title="Événement" :edit="false" @editEvent="toggleEdit">

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

                        <div class="bg-light-blue-1 q-my-md q-pa-md">
                            {{ event }}
                        </div>
                    </template>
                </FormSection>

            </template>

        </Form>

    </div>
</template>

<script>
import events from '../assets/data/events.json'
import items from '../assets/data/items.json'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"


export default {
    name: 'Event',
    components: { Form, FormSection },
    props: { 'model': Object },
    emits: [],
    setup() {
        return {

            // model: ref(null),
        }
    },
    data() {
        return {
            edit: false,
            event: events.find(e => e.id === this.$route.params.id),
            items: items,
            eventDate: null,
            eventTime: null,
            eventTypes: [
                'Dépôt', 'Demande département', 'Délai', 'Clôture'
            ],
            linkedItem: null,
        }
    },
    computed: {
    },
    mounted() {

    },
    methods: {
        toggleEdit(val) {
            this.edit = val
        },
        setLinkedItem() {


        }
    }
}
</script>

<style scoped></style>
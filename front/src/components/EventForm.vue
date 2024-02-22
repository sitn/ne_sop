<template>
    <Form :model="event" :edit="edit" :changewatch="changewatch" @validation-event="validation">

        <template v-slot:body>

            <!-- IDENTIFICATION SECTION -->
            <FormSection title="Événement">
                <template v-slot:content>

                    <div class="row q-col-gutter-lg q-py-md" v-if="item">
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <div class="text-weight-medium">{{ item.number }} - {{ item.type.name }}</div>
                            <router-link :to="{
                                name: 'Item',
                                params: {
                                    id: item.id
                                }
                            }">
                                <div>{{ item.title }}</div>

                            </router-link>
                        </div>
                    </div>

                    <div class="row q-col-gutter-lg q-py-md">

                        <!-- DATE INPUT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <!-- <q-input type="date" pattern="\d{2}.\d{2}.\d{4}" bg-color="white" outlined v-model="event.date" label="Date (jj.mm.aaaa)" required> -->
                            <q-input bg-color="white" outlined v-model="event.date" label="Date (jj.mm.aaaa)" mask="##.##.####" :rules="[val => checkDate(val)]" :disable="!edit">
                                <template v-slot:append>
                                    <q-icon name="event" class="cursor-pointer">
                                        <q-popup-proxy ref="qDateProxy" transition-show="scale" transition-hide="scale">
                                            <q-date v-model="event.date" mask="DD.MM.YYYY" today-btn color="blue-grey" text-color="white">
                                                <div class="row justify-end">
                                                    <q-btn v-close-popup label="Fermer" color="primary" flat />
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
                            <!-- <q-input type="time" bg-color="white" outlined v-model="event.time" label="Heure" :rules="['time']" /> -->
                            <q-input bg-color="white" outlined v-model="event.time" label="Heure (hh:mm)" mask="##:##" :rules="[val => checkTime(val, true)]" clearable :disable="!edit">
                                <template v-slot:append>
                                    <q-icon name="access_time" class="cursor-pointer">
                                        <q-popup-proxy transition-show="scale" transition-hide="scale">
                                            <q-time v-model="event.time" color="blue-grey" text-color="white">
                                                <div class="row items-center justify-end">
                                                    <q-btn v-close-popup label="Fermer" color="primary" flat />
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
                            <q-select bg-color="white" outlined v-model="event.type" :options="eventTypes" option-label="name" option-value="id" emit-value map-options label="Type" :rules="[val => checkFilled(val)]" clearable :disable="!edit">
                            </q-select>
                        </div>

                        <!-- LINKED ITEM SELECT FIELD -->
                        <!-- 
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-select bg-color="white" outlined v-model="linkedItem" :options="this.store.items" option-label="number" label="Objet lié" @update:model-value="setLinkedItem(val)" :rules="[val => checkFilled(val)]" clearable :disable="!edit">
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
                        -->

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

                </template>
            </FormSection>

        </template>

    </Form>
</template>

<script>
// import { date } from 'quasar'
import { store } from '../store/store.js'
import { checkFilled, checkDate, checkTime } from '../store/shared.js'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"

export default {
    name: 'EventForm',
    components: { Form, FormSection },
    props: { 'edit': Boolean, 'modelValue': Object, 'mode': String, 'changewatch': { type: Boolean, default: true } },
    emits: ['update:modelValue', 'validationEvent'],
    data() {
        return {
            store,
            valid: null,
            eventTypes: [],
            item: null,
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
    async created() {

        this.eventTypes = await this.store.getEventTypes()
        if (this.event.item) {
            this.item = await this.store.getItem(this.event.item, true)
        }
        // console.log(`${this.$options.name} | router id: ${this.$route.params.id}`)
    },
    async mounted() {
        store.event.old = JSON.stringify(this.modelValue)
    },
    watch: {
        modelValue: {
            handler(newValue, oldValue) {
                // console.log(`${this.$options.name} | watch: modelValue`)

                if (newValue.time === "") {
                    newValue.time = null
                }

                // store.event.new = Object.assign({}, this.modelValue)
                store.event.new = JSON.stringify(this.modelValue)

                if (this.changewatch) {
                    store.updateWarning(store.event)
                }

            },
            deep: true
        }
    },

    methods: {
        checkFilled,
        checkDate,
        checkTime,
        validation(val) {
            // console.log(`${this.$options.name} | validation: ${val}`)
            this.valid = val
            this.$emit('validationEvent', this.valid)
        },
    }
}
</script>

<style scoped></style>
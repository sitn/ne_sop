<template>
    <div class="">
        <q-layout>

            <!-- Breadcrumbs navigation -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Personnes et groupes" to="/entities" />
                    <q-breadcrumbs-el :label="entity.name" />
                </q-breadcrumbs>
            </div>

            <Form title="Informations générales" :edit="false" :toggle="true" @editEvent="toggleEdit">

                <template v-slot:body>

                    <!-- IDENTIFICATION SECTION -->
                    <FormSection title="Identification">
                        <template v-slot:content>
                            <div class="text-h6">Identification</div>

                            <div class="row q-col-gutter-lg q-py-md">
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input bg-color="white" outlined v-model="entity.name" label="Nom" :disable="!edit" />
                                </div>
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <!-- TYPE SELECT FIELD -->
                                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                        <q-select bg-color="white" outlined v-model="entity.type" :options="entityTypes" label="Type" :disable="!edit">
                                        </q-select>
                                    </div>
                                </div>
                            </div>

                            <div class="row q-col-gutter-lg q-py-md">
                                <div class="col">
                                    <q-input bg-color="white" outlined v-model="entity.description" label="Description" type="textarea" :disable="!edit" />
                                </div>
                            </div>

                            <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                                {{ entity }}
                            </div>
                        </template>
                    </FormSection>

                    <!-- ADDRESS SECTION -->
                    <FormSection title="Addresse">
                        <template v-slot:content>
                            <div class="text-h6">Addresse</div>

                            <div class="row q-col-gutter-lg q-py-md">
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input bg-color="white" outlined v-model="entity.street" label="Rue" :disable="!edit" />
                                </div>
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input bg-color="white" outlined v-model="entity.postalCode" label="Code postal" :disable="!edit" />
                                </div>
                            </div>

                            <div class="row q-col-gutter-lg q-py-md">
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input bg-color="white" outlined v-model="entity.city" label="Localité" :disable="!edit" />
                                </div>
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input bg-color="white" outlined v-model="entity.region" label="Canton / Région" :disable="!edit" />
                                </div>
                            </div>
                            <div class="row q-col-gutter-lg q-py-md">
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input bg-color="white" outlined v-model="entity.country" label="Pays" :disable="!edit" />
                                </div>

                            </div>

                        </template>
                    </FormSection>

                    <!-- CONTACT SECTION -->
                    <FormSection title="Contact">
                        <template v-slot:content>
                            <div class="text-h6">Contact</div>

                            <div class="row q-col-gutter-lg q-py-md">
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input type="email" bg-color="white" outlined v-model="entity.email" label="Email" :rules="[val => checkEmail(val)]" :disable="!edit" />
                                </div>
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input type="tel" bg-color="white" outlined v-model="entity.telephone" label="Téléphone (format international)" @update:model-value="checkPhoneNumber(this.entity.telephone)" @blur="formatPhoneNumber(this.entity.telephone)" :rules="[val => checkPhoneNumber(val)]" :disable="!edit" />
                                </div>
                            </div>

                            <div class="row">
                                <div class="col">
                                    <q-input type="text" bg-color="white" outlined v-model="entity.website" label="Site Internet" :rules="[val => checkWebsite(val)]" :disable="!edit" />
                                </div>
                            </div>

                        </template>
                    </FormSection>

                </template>

            </Form>

            <!-- FLOATING SAVE BUTTON -->
            <q-page-sticky position="bottom-right" :offset="[18, 18]" v-if="edit">
                <q-btn :loading="false" fab icon="sym_o_save" color="amber-14" @click="save()">
                    <q-tooltip class="bg-black">Enregistrer</q-tooltip>
                </q-btn>
            </q-page-sticky>

        </q-layout>

    </div>
</template>

<script>
import { store } from '../store/store.js'
import parsePhoneNumber from 'libphonenumber-js'
import entityTypes from '../assets/data/entity-types.json'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"

export default {
    store,
    name: 'Entity',
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
            store,
            edit: false,
            entity: store.entities.find(e => e.id === this.$route.params.id),
            entityTypes: entityTypes,
        }
    },
    computed: {
    },
    created() {

    },
    mounted() {

        // TEST
        /*
        const phoneNumber = parsePhoneNumber('+41 32 889 47 72') // , 'CH')
        console.log(phoneNumber)
        console.log(phoneNumber.isPossible())
        console.log(phoneNumber.isValid())
        console.log(phoneNumber.number)
        console.log(phoneNumber.country)
        console.log(phoneNumber.formatInternational())
        console.log(phoneNumber.formatNational())
        console.log(phoneNumber.getURI())
        */

    },
    methods: {
        async load() {
            // TODO: GET ENTITY FROM DATABASE
            console.log('Entity.vue | load()')
        },
        async save() {
            // TODO: POST ENTITY TO DATABASE
            console.log('Entity.vue | save()')
        },
        toggleEdit(val) {
            this.edit = val
        },
        checkPhoneNumber(val) {

            let phoneNumber = parsePhoneNumber(val)
            if (phoneNumber) {
                val = '+41255555555'
                console.log('this.entity.phoneNumber')
                console.log(this.entity.phoneNumber)
                return phoneNumber.isPossible() & phoneNumber.isValid()
            } else {
                return 'Format non-valable'
            }

        },
        formatPhoneNumber(val) {
            // this.entity.telephone = '+41255555555'
            console.log('formatPhoneNumber')
            console.log(val)
        },
        checkEmail(val) {

            let reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
            let isValid = reg.test(val)

            if (isValid) {
                return true
            } else {
                return 'Format non-valable'
            }

        },
        checkWebsite(val) {

            let reg = /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi
            let isValid = reg.test(val)

            if (isValid) {
                return true
            } else {
                return 'Format non-valable'
            }

        },

    }
}
</script>

<style scoped></style>
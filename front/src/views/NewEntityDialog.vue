<template>
    <q-card style="width: 700px; max-width: 80vw;">
        <q-card-section class="bg-blue-grey text-white">
            <div class="text-h6">Nouvelle personne ou groupe</div>
        </q-card-section>

        <q-card-section class="row items-center scroll" style="max-height: 70vh">

            <div class="col">

                <!-- Identification -->
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

                        <div class="bg-light-blue-1 q-my-md q-pa-md">
                            {{ entity }}
                        </div>
                    </template>
                </FormSection>

                <!-- Address -->
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

            </div>

        </q-card-section>

        <q-card-actions align="right">
            <q-btn flat label="Annuler" color="primary" v-close-popup />
            <q-btn flat label="Sauvegarder" color="primary" @click="save()" v-close-popup />
        </q-card-actions>
    </q-card>
</template>

<script>
import { store } from '../store/store.js'
import parsePhoneNumber from 'libphonenumber-js'
import entityTypes from '../assets/data/entity-types.json'
import FormSection from "../components/FormSection.vue"

export default {
    name: 'NewEntityDialog',
    components: { FormSection },
    props: { 'model': Object },
    emits: ['addNewEntity'],
    setup() {
        return {

            // model: ref(null),
        }
    },
    data() {
        return {
            store,
            edit: true,
            entity: {},
            entityTypes: entityTypes,
        }
    },
    computed: {
    },
    mounted() {

    },
    methods: {
        save(val) {

            console.log('save:')
            console.log(this.entity)
            this.$emit('addNewEntity', this.entity)

            // this.store.entities.push(this.entity)

            // POST NEW VALUE TO DATABASE

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
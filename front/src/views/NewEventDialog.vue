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
import FormSection from "../components/FormSection.vue"

export default {
    name: 'NewEventDialog',
    components: { FormSection },
    props: { 'model': Object },
    emits: ['addNewEvent'],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            edit: true,
            event: {}
        }
    },
    computed: {
    },
    mounted() {

    },
    methods: {
        save(val) {


        },

    }
}
</script>

<style scoped></style>
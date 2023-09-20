<template>
    <div class="">

        <!-- Breadcrumbs navigation -->
        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Personnes et groupes" to="/entities" />
                <q-breadcrumbs-el :label="entity.name" />
            </q-breadcrumbs>
        </div>

        <!-- Identification -->
        <FormSection title="Identification">
            <template v-slot:content>
                <div class="text-h6">Identification</div>

                <div class="row q-col-gutter-lg q-py-md">
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-input bg-color="white" outlined v-model="entity.name" label="Nom" />
                    </div>
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-input bg-color="white" outlined v-model="entity.type" label="Type" />

                    </div>
                </div>

                <div class="row q-col-gutter-lg q-py-md">
                    <div class="col">
                        <q-input bg-color="white" outlined v-model="entity.description" label="Description" type="textarea" />
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
                        <q-input bg-color="white" outlined v-model="entity.street" label="Rue" />
                        <!-- <q-select bg-color="white" outlined v-model="" :options="" label="Principal" /> -->
                    </div>
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-input bg-color="white" outlined v-model="entity.postalCode" label="Code postal" />
                        <!-- <q-select bg-color="white" outlined v-model="" :options="" label="Appui" /> -->
                    </div>
                </div>

                <div class="row q-col-gutter-lg q-py-md">
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-input bg-color="white" outlined v-model="entity.city" label="Localité" />
                        <!-- <q-select bg-color="white" outlined v-model="" :options="" label="Principal" /> -->
                    </div>
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-input bg-color="white" outlined v-model="entity.region" label="Canton / Région" />
                        <!-- <q-select bg-color="white" outlined v-model="" :options="" label="Appui" /> -->
                    </div>
                </div>
                <div class="row q-col-gutter-lg q-py-md">
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-input bg-color="white" outlined v-model="entity.country" label="Pays" />
                        <!-- <q-select bg-color="white" outlined v-model="" :options="" label="Principal" /> -->
                    </div>

                </div>

            </template>
        </FormSection>

        <FormSection title="Contact">
            <template v-slot:content>
                <div class="text-h6">Contact</div>

                <div class="row q-col-gutter-lg q-py-md">
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-input type="email" bg-color="white" outlined v-model="entity.email" label="Email" />
                    </div>
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-input type="tel" bg-color="white" outlined v-model="entity.telephone" label="Téléphone (format international)" @update:model-value="checkPhoneNumber(this.entity.telephone)" @blur="formatPhoneNumber(this.entity.telephone)" :rules="[val => checkPhoneNumber(val)]" />
                    </div>
                </div>

                <div class="row">
                    <div class="col">
                        <q-input type="text" bg-color="white" outlined v-model="entity.website" label="Site Internet" />
                    </div>
                </div>

            </template>
        </FormSection>

    </div>
</template>

<script>
import parsePhoneNumber from 'libphonenumber-js'
import entities from '../assets/data/entities.json'
import FormSection from "../components/FormSection.vue"


export default {
    name: 'Entity',
    components: { FormSection },
    props: { 'model': Object },
    emits: [],
    setup() {
        return {

            // model: ref(null),
        }
    },
    data() {
        return {
            entity: entities.find(e => e.id === this.$route.params.id)
        }
    },
    computed: {
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
        checkEmail() {

        },
        checkWebsite() {

        },

    }
}
</script>

<style scoped></style>
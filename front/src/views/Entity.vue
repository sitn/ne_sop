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
                        <q-input bg-color="white" outlined v-model="entity.description" label="Description"
                            type="textarea" />
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
                        <q-input bg-color="white" outlined v-model="entity.email" label="Email" />
                    </div>
                    <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                        <q-input bg-color="white" outlined v-model="entity.telephone" label="Téléphone" />

                    </div>
                </div>

                <div class="row q-col-gutter-lg q-py-md">
                    <div class="col">
                        <q-input bg-color="white" outlined v-model="entity.website" label="Site Internet" />
                    </div>
                </div>

            </template>
        </FormSection>

    </div>
</template>

<script>
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

    },
    methods: {
    }
}
</script>

<style scoped></style>
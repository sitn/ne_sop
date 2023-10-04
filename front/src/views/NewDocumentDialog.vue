<template>
    <q-card style="width: 1000px; max-width: 80vw;">
        <q-card-section class="bg-blue-grey text-white">
            <div class="text-h6">Nouveau document</div>
        </q-card-section>

        <q-card-section class="row items-center scroll" style="max-height: 70vh">

            <div class="col">

                <!-- SUMMARY SECTION -->
                <FormSection title="Type">
                    <template v-slot:content>
                        <div class="text-h6">Résumé</div>

                        <div class="row q-col-gutter-lg q-py-md">

                            <!-- TITLE TEXT INPUT FIELD -->
                            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                <q-input bg-color="white" outlined v-model="document.title" label="Titre" :disable="!edit" />
                            </div>

                            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                <!-- TYPE SELECT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-select bg-color="white" outlined v-model="document.type" :options="documentTypes" option-label="name" option-value="name" emit-value label="Type" :disable="!edit">

                                        <template v-slot:option="scope">
                                            <q-item v-bind="scope.itemProps">
                                                <q-item-section>
                                                    <q-item-label>{{ scope.opt.name }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                        </template>

                                    </q-select>
                                </div>
                            </div>

                        </div>

                    </template>
                </FormSection>

                <!-- CONTENT SECTION -->
                <FormSection title="Contenu">
                    <template v-slot:content>
                        <div class="text-h6">Contenu</div>


                        <div class="row q-col-gutter-lg q-py-md">
                            <div class="col">
                                <q-editor v-model="document.content" min-height="15rem" />
                            </div>
                        </div>

                        <div class="bg-light-blue-1 q-my-md q-pa-md">
                            {{ document }}
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
import fs from 'fs'
// import HTMLtoDOCX from '../dist/html-to-docx.esm'
import { store } from '../store/store.js'
import templates from '../assets/data/templates.json'
import FormSection from "../components/FormSection.vue"

export default {
    name: 'NewDocumentDialog',
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
            store,
            edit: true,
            document: { "title": "", "version": null, "type": null, "author": store.session.user, "note": null, "content": "" },
            documentTypes: templates,
        }
    },
    computed: {
    },
    mounted() {

    },
    methods: {
        async save() {

            // TODO: POST RECORD TO DATABASE
            console.log('NewDocumentDialog.vue | save()')
            let ind = store.items.findIndex((e) => (e.id === this.$route.params.id))
            store.items[ind].documents.push(this.document)

        },

    }
}
</script>

<style scoped></style>
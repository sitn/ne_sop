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

                        <!-- NOTE TEXT AREA FIELD -->
                        <div class="row q-col-gutter-lg q-my-sm">
                            <div class="col">
                                <q-input bg-color="white" outlined v-model="document.note" label="Notes" type="textarea" :disable="!edit" />
                            </div>
                        </div>

                    </template>
                </FormSection>


            </div>

        </q-card-section>

        <q-card-actions align="right">
            <q-btn flat label="Annuler" color="primary" v-close-popup />
            <q-btn flat label="Confirmer" color="primary" @click="save()" v-close-popup />
        </q-card-actions>
    </q-card>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { date } from 'quasar'
import { store } from '../store/store.js'
import templates from '../assets/data/templates.json'
import FormSection from "../components/FormSection.vue"

export default {
    name: 'NewDocumentDialog',
    components: { FormSection },
    props: { 'modelValue': Object },
    emits: [],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            edit: true,
            document: {
                "id": uuidv4(),
                "filename": "",
                "filesize": "",
                "format": "",
                "title": "",
                "version": null,
                "type": null,
                "date": new Date(),
                "timestamp": Date.now(),
                "author": store.session.user,
                "note": null,
                "content": ""
            },
            documentTypes: templates,
        }
    },
    computed: {
        documents: {
            get() {
                return this.modelValue
            },
            set(documents) {
                this.$emit('update:modelValue', documents)
            }
        }
    },
    mounted() {

    },
    methods: {
        async save() {

            this.documents.push(Object.assign({}, this.document))
            // console.log('NewDocumentDialog.vue | save()')
            // let ind = store.items.findIndex((e) => (e.id === this.$route.params.id))
            // store.items[ind].documents.push(this.document)

        },

    }
}
</script>

<style scoped></style>
<template>
    <Form :model="document" :edit="edit" :changewatch="changewatch">

        <template v-slot:body>

            <!-- FILE SECTION -->
            <FormSection title="Informations générales" class="q-mt-none">
                <template v-slot:content>
                    <!-- <div class="text-h6">Document</div> -->

                    <div class="row q-col-gutter-lg q-py-md">

                        <!-- REFERENCE TEXT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input bg-color="white" outlined v-model="document.reference" label="N° référence" :disable="!edit" />
                        </div>

                        <!-- TITLE TEXT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input bg-color="white" outlined v-model="document.title" label="Titre" :rules="[v => checkFilled(v)]" :disable="!edit" />
                        </div>

                    </div>

                    <div class="row q-col-gutter-lg q-py-md">

                        <!-- FILE SELECTOR FIELD -->
                        <!--
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-file bg-color="white" outlined v-model="document.file" label="Sélectionner un fichier" counter max-files="1" :rules="[v => checkFile(v)]" clearable @update:model-value="getFileAttributes">
                                <template v-slot:prepend>
                                    <q-icon name="sym_o_attach_file" />
                                </template>
</q-file>
</div>
-->

                        <!-- TYPE SELECT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-select bg-color="white" outlined v-model="document.type" :options="documentTypes" option-label="name" emit-value label="Type" :rules="[v => checkFilled(v)]" clearable :disable="!edit">

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

                    <!-- NOTE TEXT AREA FIELD -->
                    <div class="row q-col-gutter-lg">
                        <div class="col">
                            <q-input bg-color="white" outlined v-model="document.note" label="Notes" type="textarea" :disable="!edit" counter maxlength="500" />
                        </div>
                    </div>

                    <!-- TODO REMOVE/DEV DISPLAY JSON-->
                    <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                        <div>document</div>
                        <div>{{ document }}</div>
                    </div>

                </template>
            </FormSection>

        </template>

    </Form>
</template>

<script>
import { store } from '../store/store.js'
import { checkFilled, checkFile } from '../store/shared.js'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"

export default {
    name: 'DocumentForm',
    components: { Form, FormSection },
    props: { 'item_type': Number, 'edit': Boolean, 'modelValue': Object, 'changewatch': { type: Boolean, default: true } },
    emits: ['update:modelValue'],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            documentTypes: [],
            valid: null,
        }
    },
    computed: {
        document: {
            get() {
                return this.modelValue
            },
            set(document) {
                this.$emit('update:modelValue', document)
            }
        }
    },
    async created() {
        this.documentTypes = await this.store.getDocumentTypes()
        // this.getDocumentTypes()
    },
    methods: {
        checkFilled,
        checkFile,
        validation(val) {
            // console.log(`${this.$options.name} | validation: ${val}`)
            this.valid = val
            // this.$emit('validationEvent', this.valid)
        },
        getFileAttributes() {
            if (this.document.file) {
                this.document.filename = this.document.file.name
                this.document.size = this.document.file.size
            }
        }
        /*
        async getDocumentTypes() {
            this.documentTypes = await store.getTemplatesByItemType(this.item_type)
        }
        */
    }
}
</script>

<style scoped></style>
<template>
    <Form :model="document" :edit="edit" :changewatch="changewatch">

        <template v-slot:body>

            <!-- FILE SECTION -->
            <FormSection title="" class="q-mt-none">
                <template v-slot:content>


                    <!-- FILE SELECTOR FIELD -->
                    <div class="col q-my-md" v-if="!document.file">
                        <!-- counter max-files="1" -->
                        <q-file bg-color="white" outlined v-model="newFile" label="Sélectionner un fichier" :rules="[v => checkFile(v)]" clearable @update:model-value="getFileAttributes">
                            <template v-slot:prepend>
                                <q-icon name="sym_o_attach_file" />
                            </template>
                        </q-file>
                    </div>

                    <!-- ATTACHED FILE CARD -->
                    <q-card class="col q-my-md" flat bordered v-if="document.file">

                        <q-item>
                            <q-item-section avatar>
                                <q-avatar color="blue" text-color="white" icon="sym_o_file_present" />
                            </q-item-section>

                            <q-item-section>
                                <q-item-label class="text-weight-medium"><a :href="fileDownloadUrl">{{ document.filename }}</a></q-item-label>
                                <q-item-label caption>{{ formatBytes(document.size) }}</q-item-label>
                            </q-item-section>

                            <q-item-section avatar>
                                <q-btn dense round flat color="red" name="delete" @click="showDeleteDialog(document)" icon="sym_o_delete">
                                    <q-tooltip class="bg-black">Supprimer</q-tooltip>
                                </q-btn>
                            </q-item-section>
                        </q-item>

                    </q-card>


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

                        <!-- TYPE SELECT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <!-- v-model="entity.type" :options="entityTypes" option-label="name" option-value="id" emit-value map-options label="Type"  -->
                            <q-select bg-color="white" outlined v-model="document.type" :options="documentTypes" option-label="name" option-value="id" emit-value map-options label="Type" :rules="[v => checkFilled(v)]" clearable :disable="!edit">
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

                    <div class="row q-col-gutter-lg q-py-md">
                        <div class="col">
                            <q-list dense bordered padding class="rounded-borders">
                                <q-item clickable v-for="item in document.items">
                                    <q-item-section>
                                        {{ item }}
                                    </q-item-section>
                                </q-item>
                            </q-list>
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

    <!-- DELETE DIALOG -->
    <DeleteDialog v-model="dialog.deletion" @delete-event="handleDelete" :content="dialog_content" />

</template>

<script>
import { store } from '../store/store.js'
import { checkFilled, checkFile, formatBytes } from '../store/shared.js'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"
import DeleteDialog from './DeleteDialog.vue'

export default {
    name: 'DocumentForm',
    components: { Form, FormSection, DeleteDialog },
    props: { 'item_type': Number, 'edit': Boolean, 'modelValue': Object, 'changewatch': { type: Boolean, default: true } },
    emits: ['update:modelValue'],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            dialog: { deletion: false },
            dialog_content: undefined,
            documentTypes: [],
            newFile: null,
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
        },
        fileDownloadUrl() {
            return `${this.store.host}/api/document/${this.document.uuid}/download/`;
        }

    },
    async created() {
        this.documentTypes = await this.store.getDocumentTypes()
        // this.getDocumentTypes()
    },
    methods: {
        formatBytes,
        checkFilled,
        checkFile,
        validation(val) {
            // console.log(`${this.$options.name} | validation: ${val}`)
            this.valid = val
            // this.$emit('validationEvent', this.valid)
        },
        getFileAttributes() {
            if (this.newFile) {
                this.document.file = this.newFile
                this.document.filename = this.newFile.name
                this.document.size = this.newFile.size
                // this.document.type = 1 // TODO rmeove this
            }
        },
        showDeleteDialog(val) {
            this.dialog_content = `Supprimer définitivement le document '${val.filename}' ?`
            this.dialog.deletion = true
        },
        handleDelete() {
            this.document.file = null
            this.newFile = null
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
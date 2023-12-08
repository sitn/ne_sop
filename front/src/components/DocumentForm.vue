<template>
    <Form :model="document" :edit="edit">

        <template v-slot:body>

            <!-- FILE SECTION -->
            <FormSection>
                <template v-slot:content>
                    <div class="text-h6">Fichier</div>

                    <div class="row q-col-gutter-lg q-py-md">

                        <!-- FILE SELECTOR FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-file bg-color="white" outlined v-model="document.file" label="Sélectionner un fichier" counter max-files="1" :rules="[v => checkFile(v)]" clearable @update:model-value="getFileAttributes">
                                <template v-slot:prepend>
                                    <q-icon name="sym_o_attach_file" />
                                </template>
                            </q-file>
                        </div>

                        <!-- TYPE SELECT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-select bg-color="white" outlined v-model="document.type" :options="documentTypes" option-label="name" option-value="name" emit-value label="Type" :rules="[v => checkFilled(v)]" clearable :disable="!edit">

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
                            <q-input bg-color="white" outlined v-model="document.note" label="Notes" type="textarea" :disable="!edit" />
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
    props: { 'type': String, 'edit': Boolean, 'modelValue': Object },
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
    created() {
        console.log(`${this.$options.name} | router id: ${this.$route.params.id}`)
        this.getTemplatesByItemType(this.type);
        
        
    },
    mounted() {
    },
    updated() {
    },
    methods: {
        checkFilled,
        checkFile,
        validation(val) {
            console.log(`${this.$options.name} | validation: ${val}`)
            this.valid = val
            // this.$emit('validationEvent', this.valid)
        },
        getFileAttributes() {
            if (this.document.file) {
                console.log(this.document.file.size)
                this.document.filename = this.document.file.name
                this.document.filesize = this.document.file.size
                console.log(this.document.filesize)
            }
        },

        async getTemplatesByItemType(type) {
            try {

                console.log("this.type =", type)
                const response = await fetch('http://127.0.0.1:8000/api/template-types?itemtype=' + type, {
                    method: 'GET',
                    redirect: 'follow'
                })
                this.documentTypes = await response.json()
                
            } catch (error) {
                console.error(error)
            }
        },
    }
}
</script>

<style scoped></style>
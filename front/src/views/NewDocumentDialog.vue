<template>
    <q-card style="width: 700px; max-width: 80vw;">
        <q-card-section class="bg-blue-grey text-white">
            <div class="text-h6">Nouveau document</div>
        </q-card-section>

        <q-card-section class="row items-center scroll" style="max-height: 70vh">

            <!-- FORM -->
            <DocumentForm class="col" v-model="document" :type="type" :edit="edit"></DocumentForm>

        </q-card-section>

        <q-card-actions align="right">
            <q-btn flat label="Annuler" color="primary" v-close-popup />
            <q-btn flat label="Confirmer" color="primary" @click="save()" v-close-popup :disable="!document.valid" />
        </q-card-actions>
    </q-card>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { date } from 'quasar'
import { store } from '../store/store.js'
import DocumentForm from "../components/DocumentForm.vue"

export default {
    name: 'NewDocumentDialog',
    components: { DocumentForm },
    props: { 'type': String, 'modelValue': Object },
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
                "file": null,
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
                "content": "",
                "valid": false
            }
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
        }
    }
}
</script>

<style scoped></style>
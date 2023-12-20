<template>
    <q-card style="width: 700px; max-width: 80vw;">
        <q-card-section class="bg-blue-grey text-white">
            <div class="text-h6">Nouveau document</div>
        </q-card-section>

        <q-card-section class="row items-center scroll" style="max-height: 70vh">

            <!-- FORM -->
            <DocumentForm class="col" v-model="document" :item_type="item_type" :edit="edit"></DocumentForm>

        </q-card-section>

        <q-card-actions align="right">
            <q-btn flat label="Annuler" color="primary" v-close-popup />
            <q-btn flat label="Confirmer" color="primary" @click="save()" v-close-popup :disable="!document.valid" />
        </q-card-actions>
    </q-card>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { store } from '../store/store.js'
import DocumentForm from "../components/DocumentForm.vue"

export default {
    name: 'NewDocumentDialog',
    components: { DocumentForm },
    props: { 'item_type': Number, 'modelValue': Object },
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
                // "author": store.session.user,
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

            this.documents.unshift({
                'file': this.document.file,
                'filename': this.document.filename,
                'created': new Date().toLocaleString(),
                // 'item_id': this.$route.params.id,
                'template': this.document.type.name,
                'template_id': this.document.type.id,
                'size': this.document.size,
                'note': this.document.note,
                'author_id': 1 // /!\ METTRE A JOUR AVEC LA VALEUR DE L'AUTEUR DU DOCUMENT !
            })
        }
    }
}
</script>

<style scoped></style>
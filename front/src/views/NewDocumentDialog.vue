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
            
            let formData = new FormData()
            formData.append('file', this.document.file)
            formData.append('item_id', this.$route.params.id)


            try {
                console.log("I'm in the try to send the request containing a binary file")
    
                const response = await fetch('http://127.0.0.1:8000/api/fileupload/' + this.document.filename, {
                    method: 'PUT',
                    body: formData,
                    redirect: 'follow'
                })
                await response
                
            } catch (error) {
                console.error(error)
            }
            
        }
    }
}
</script>

<style scoped></style>
<template>
    <q-card style="width: 700px; max-width: 80vw;">
        <q-card-section class="bg-blue-grey text-white">
            <div class="text-h6">Modifier le document</div>
        </q-card-section>

        <q-card-section class="row items-center scroll" style="max-height: 70vh">

            <!-- FORM -->
            <DocumentForm class="col" :item_type="item_type" v-model="document" :edit="edit" :changewatch="false"></DocumentForm>

        </q-card-section>

        <q-card-actions align="right">
            <q-btn flat label="Annuler" color="primary" v-close-popup />
            <q-btn flat label="Confirmer" color="primary" @click="save()" v-close-popup :disable="!document.valid" />
        </q-card-actions>
    </q-card>
</template>

<script>
import { store } from '../store/store.js'
import DocumentForm from "../components/DocumentForm.vue"

export default {
    name: 'EditDocumentDialog',
    components: { DocumentForm },
    props: { 'item_type': Number, 'modelValue': Object },
    emits: ['update:modelValue'],
    data() {
        return {
            store,
            document: null,
            edit: true,
            valid: false,
        }
    },
    created() {
        this.document = Object.assign({}, this.modelValue)
    },
    methods: {
        save() {
            Object.assign(this.modelValue, this.document)
            this.$emit('update:modelValue', this.modelValue)
        },

    }
}
</script>

<style scoped></style>
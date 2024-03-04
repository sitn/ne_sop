<template>
    <q-card style="width: 700px; max-width: 80vw;">
        <q-card-section class="bg-blue-grey text-white">
            <div class="text-h6">Nouvelle personne ou groupe</div>
        </q-card-section>

        <q-card-section class="row items-center scroll" style="max-height: 70vh">

            <!-- FORM -->
            <EntityForm class="col" v-model="entity" :edit="edit" :changewatch="false"></EntityForm>

        </q-card-section>

        <q-card-actions align="right">
            <q-btn flat label="Annuler" color="primary" v-close-popup />
            <q-btn flat label="Confirmer" color="primary" @click="save()" v-close-popup :disable="!entity.valid" />
        </q-card-actions>
    </q-card>
</template>

<script>
import { store } from '../store/store.js'
import EntityForm from "../components/EntityForm.vue"

export default {
    name: 'NewEntityDialog',
    components: { EntityForm },
    props: {},
    emits: ['addNewEntity'],
    data() {
        return {
            store,
            edit: true,
            entity: {
                "name": "",
                "type": "",
                "description": "",
                "street": "",
                "city": "",
                "postalcode": "",
                "region": "",
                "country": "",
                "website": "",
                "email": "",
                "telephone": "",
                "valid": false,
                "active": true
            },
        }
    },
    methods: {
        save() {

            // console.log(`${this.$options.name} | save()`)
            this.$emit('addNewEntity', this.entity)

        }
    }
}
</script>

<style scoped></style>
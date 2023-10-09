<template>
    <q-card style="width: 700px; max-width: 80vw;">
        <q-card-section class="bg-blue-grey text-white">
            <div class="text-h6">Nouvelle personne ou groupe</div>
        </q-card-section>

        <q-card-section class="row items-center scroll" style="max-height: 70vh">

            <!-- <div class="col"> -->

            <!-- FORM -->
            <EntityForm v-model="entity" :edit="edit"></EntityForm>

            <!-- </div> -->

        </q-card-section>

        <q-card-actions align="right">
            <q-btn flat label="Annuler" color="primary" v-close-popup />
            <q-btn flat label="Sauvegarder" color="primary" @click="save()" v-close-popup />
        </q-card-actions>
    </q-card>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { store } from '../store/store.js'
import entityTypes from '../assets/data/entity-types.json'
import EntityForm from "../components/EntityForm.vue"

export default {
    name: 'NewEntityDialog',
    components: { EntityForm },
    props: { 'model': Object },
    emits: ['addNewEntity'],
    setup() {
        return {}
    },
    data() {
        return {
            store,
            edit: true,
            entity: {
                "id": uuidv4(),
                "name": "",
                "type": "",
                "description": "",
                "street": "",
                "city": "",
                "postalCode": "",
                "region": "",
                "country": "",
                "website": "",
                "email": "",
                "telephone": ""
            },
            entityTypes: entityTypes,
        }
    },
    computed: {
    },
    mounted() {
    },
    methods: {
        save(val) {

            console.log('save:')
            console.log(this.entity)
            this.$emit('addNewEntity', this.entity)
            // this.store.entities.push(this.entity)
            // POST NEW VALUE TO DATABASE

        }
    }
}
</script>

<style scoped></style>
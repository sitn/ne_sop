<template>
    <div class="">

        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Personnes et groupes" to="/entities" />
                    <q-breadcrumbs-el label="Nouvelle entité" />
                </q-breadcrumbs>
            </div>

            <!-- FORM -->
            <EntityForm v-model="entity" :edit="edit"></EntityForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="{ 'save': true, 'deletion': false }" @save-event="save" @edit-event="setEditMode"></FloatingButtons>

        </q-layout>

    </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import entityTypes from '../assets/data/entity-types.json'
import FloatingButtons from "../components/FloatingButtons.vue"
import EntityForm from "../components/EntityForm.vue"

export default {
    name: 'NewEntity',
    components: { FloatingButtons, EntityForm },
    props: {},
    emits: [],
    setup() {
        return {}
    },
    data() {
        return {
            store,
            edit: true,
            wait: false,
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
        async save() {
            // TODO - POST NEW RECORD TO DATABASE
            console.log(`${this.$options.name}.vue | save()`)
            this.wait = true
            await sleep(Math.random() * 1300)
            if (!this.store.entities.map((x) => (x.name)).includes(this.entity.name)) {
                this.store.entities.push(this.entity)
            }
            this.wait = false
        },
        setEditMode(val) {
            console.log(`${this.$options.name}.vue | setEditMode(${val})`)
            this.edit = val
        }
    }
}
</script>

<style scoped></style>
<template>
    <div class="" v-if="loaded">
        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Personnes et groupes" to="/entities" />
                    <q-breadcrumbs-el :label="entity.name" />
                </q-breadcrumbs>
            </div>

            <!-- FORM -->
            <EntityForm v-model="entity" :edit="edit"></EntityForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode"></FloatingButtons>

            <!-- <FloatingButtons :edit="false" :wait="wait" :buttons="{ 'save': true, 'deletion': true }" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode"></FloatingButtons> -->
            <!-- <FloatingActionButtons :edit="false" :wait="wait" :buttons="{ 'save': true, 'deletion': true }" @save-event="save" @edit-event="setEditMode"></FloatingActionButtons> -->

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

        </q-layout>

    </div>
</template>

<script>
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import FloatingButtons from "../components/FloatingButtons.vue"
import DeleteDialog from '../components/DeleteDialog.vue'
import EntityForm from "../components/EntityForm.vue"

export default {
    store,
    name: 'Entity',
    components: { FloatingButtons, DeleteDialog, EntityForm },
    props: {},
    emits: [],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            loaded: false,
            dialog: { deletion: false },
            // actionButtons: { save: 'active', deletion: 'active' },
            edit: false,
            wait: false,
            entity: null, // store.entities.find(e => e.id === this.$route.params.id),
            index: store.entities.findIndex((e) => (e.id === this.$route.params.id))
        }
    },
    computed: {

        actionButtons() {
            return {
                save: this.entity.valid ? 'active' : 'disable',
                deletion: 'none'
            }
        }

    },
    beforeCreate() {

    },
    async created() {

        

        try {

            const id = this.$route.params.id
            const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}`, {
                method: 'GET',
                redirect: 'follow'
            })
            this.entity = await response.json()
            this.loaded = true
            console.log(this.entity)

        } catch (error) {
            console.error(error)
        }

        // store.getEntity(this.$route.params.id)
        // store.saveButton = true
        // this.entity = Object.assign({}, store.entities.find((e) => (e.id === this.$route.params.id)))
        //store.getEntity(this.$route.params.id)
        // this.entity = await store.entity
        //console.log(store.entities.find((e) => (e.id === this.$route.params.id)))
        // this.load(this.$route.params.id)

    },
    mounted() {
        //store.getEntity(this.$route.params.id)
        //this.entity = store.entity

    },
    methods: {
        async load(id) {
            // TODO: GET RECORD FROM DATABASE
            console.log('Entity.vue | load()')
            try {

                const response = await fetch(`http://127.0.0.1:8000/api/entity/${id}`, {
                    method: 'GET',
                    redirect: 'follow'
                })
                this.entity = await response.json()
                console.log(this.entity)

            } catch (error) {
                console.error(error)
            }
        },
        async save(redirectTo) {
            // TODO: POST RECORD TO DATABASE
            console.log(`${this.$options.name}.vue | save()`)
            this.wait = true
            await sleep(Math.random() * 1300)
            // let ind = store.entities.findIndex((e) => (e.id === this.$route.params.id))
            store.entities[this.index] = Object.assign({}, this.entity)
            this.wait = false

            if (redirectTo !== null) {
                this.$router.push({ path: redirectTo })
            }

        },
        handleDeletion() {
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: DELETE RECORD IN DATABASE
            console.log(`${this.$options.name}.vue | remove()`)
            store.entities.splice(this.index, 1)
            this.$router.push({ name: 'EntitiesList' })
        },
        setEditMode(val) {
            console.log(`${this.$options.name}.vue | setEditMode(${val})`)
            this.edit = val
        }
    },

}
</script>

<style scoped></style>
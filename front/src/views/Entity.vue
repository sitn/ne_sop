<template>
    <div class="" v-if="!store.loading">
        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Parlementaires" to="/entities" />
                    <q-breadcrumbs-el :label="entity.name" />
                </q-breadcrumbs>
            </div>

            <!-- FORM -->
            <EntityForm v-model="entity" :edit="edit"></EntityForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode" v-if="store.user.is_manager"></FloatingButtons>

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

        </q-layout>

    </div>
</template>

<script>
import { store } from '../store/store.js'
import FloatingButtons from "../components/FloatingButtons.vue"
import DeleteDialog from '../components/DeleteDialog.vue'
import EntityForm from "../components/EntityForm.vue"

export default {
    store,
    name: 'Entity',
    components: { FloatingButtons, DeleteDialog, EntityForm },
    props: {},
    emits: [],
    data() {
        return {
            store,
            loaded: false,
            dialog: { deletion: false },
            edit: false,
            wait: false,
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
                "valid": false
            },
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
    async created() {

        // console.log(`this.$route.params.id: ${this.$route.params.id}`)
        if (this.$route.params.hasOwnProperty('id')) {
            this.store.loading = true
            this.entity = await store.getEntity(this.$route.params.id)
            this.store.loading = false
        }
        this.store.loading = false

    },
    methods: {
        async save() {

            // console.log(`${this.$options.name}.vue | save()`)
            this.wait = true
            if (this.entity.id) {
                this.entity = await store.updateEntity(this.entity.id, this.entity)
            } else {
                this.entity = await store.addEntity(this.entity)
            }
            this.wait = false

        },
        handleDeletion() {
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: DELETE RECORD IN DATABASE
            // console.log(`${this.$options.name}.vue | remove()`)
            this.$router.push({ name: 'EntitiesList' })
        },
        setEditMode(val) {
            // console.log(`${this.$options.name}.vue | setEditMode(${val})`)
            this.edit = val
        }
    },

}
</script>

<style scoped></style>
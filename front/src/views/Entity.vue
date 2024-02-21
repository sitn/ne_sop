<template>
    <div class="" v-if="!store.loading">
        <div v-if="(entity && entity.id) || this.$route.name === 'NewEntity'">
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

        <div v-else>
            <NotFound></NotFound>
        </div>
    </div>
</template>

<script>
import { store } from '../store/store.js'
import FloatingButtons from "../components/FloatingButtons.vue"
import DeleteDialog from '../components/DeleteDialog.vue'
import EntityForm from "../components/EntityForm.vue"
import NotFound from '../components/NotFound.vue'


export default {
    name: 'Entity',
    components: { FloatingButtons, DeleteDialog, EntityForm, NotFound },
    props: {},
    emits: [],
    data() {
        return {
            store,
            loaded: false,
            dialog: { deletion: false },
            edit: false,
            wait: false,
            entity: {},
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
    watch: {
        async $route(to, from) {

            if (to.name === "NewEntity" && from.href !== to.href) {
                this.initialize_entity()
                this.edit = true
                this.$router.push({ name: 'NewEntity' })
            }

            if (this.$route.params.hasOwnProperty('id')) {
                this.store.loading = true
                this.entity = await store.getEntity(this.$route.params.id)
                this.store.loading = false
            }
            this.store.loading = false

        }
    },
    async created() {
        this.initialize_entity()

        if (this.$route.name === "NewEntity") {
            this.edit = true
        }

        // console.log(`this.$route.params.id: ${this.$route.params.id}`)
        if (this.$route.params.hasOwnProperty('id')) {
            this.store.loading = true
            this.entity = await store.getEntity(this.$route.params.id)
            this.store.loading = false
        }
        this.store.loading = false

    },
    methods: {
        initialize_entity() {
            this.entity = {
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
            }
        },
        async save(redirectTo) {

            // console.log(`${this.$options.name}.vue | save()`)
            this.wait = true
            if (this.entity.id) {
                this.entity = await store.updateEntity(this.entity.id, this.entity)
            } else {
                this.entity = await store.addEntity(this.entity)
            }
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
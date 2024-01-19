<template>
    <q-layout view="hHh LpR fFf" class="shadow-2">

        <Header></Header>
        <Sidebar></Sidebar>

        <q-page-container>
            <q-page class="q-pa-md">

                <div class="" v-if="!store.loading">
                    <div v-if="entity && entity.id">
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
                            <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode" v-if="store.user.is_manager"></FloatingButtons>

                            <!-- DELETE DIALOG -->
                            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

                        </q-layout>
                    </div>

                    <div v-else>
                        <NotFound></NotFound>
                    </div>
                </div>
            </q-page>
        </q-page-container>

    </q-layout>
</template>

<script>
import { store } from '../store/store.js'
import FloatingButtons from "../components/FloatingButtons.vue"
import DeleteDialog from '../components/DeleteDialog.vue'
import EntityForm from "../components/EntityForm.vue"
import Header from '../components/Header.vue'
import Sidebar from '../components/Sidebar.vue'
import NotFound from '../components/NotFound.vue'


export default {
    name: 'Entity',
    components: { Header, Sidebar, FloatingButtons, DeleteDialog, EntityForm, NotFound },
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
    watch: {
        async $route(to, from) {

            if (this.$route.params.hasOwnProperty('id')) {
                this.store.loading = true
                this.entity = await store.getEntity(this.$route.params.id)
                this.store.loading = false
            }
            this.store.loading = false

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
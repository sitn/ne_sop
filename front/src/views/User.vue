<template>
    <div class="">

        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Administration" to="/admin" />
                    <q-breadcrumbs-el :label="user.name" />
                </q-breadcrumbs>
            </div>

            <!-- FORM -->
            <UserForm v-model="user" :edit="edit"></UserForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @delete-event="handleDeletion" @edit-event="setEditMode"></FloatingButtons>

            <!-- DELETE DIALOG -->
            <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />

        </q-layout>
    </div>
</template>

<script>
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"
import FloatingButtons from "../components/FloatingButtons.vue"
import DeleteDialog from '../components/DeleteDialog.vue'
import UserForm from "../components/UserForm.vue"

export default {
    name: 'User',
    components: { Form, FormSection, FloatingButtons, DeleteDialog, UserForm },
    props: {},
    emits: [],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            dialog: { deletion: false },
            edit: false,
            wait: false,
            user: null,
            index: store.users.findIndex((e) => (e.id === this.$route.params.id)),
            groupOptions: store.entities.filter((x) => (x.type === "Service de l'état"))
        }
    },
    computed: {
        actionButtons() {
            return {
                save: this.user.valid ? 'active' : 'disable',
                deletion: 'none'
            }
        }
    },
    created() {
        console.log(`router id: ${this.$route.params.id}`)
        this.user = Object.assign({}, store.users.find(e => e.id === this.$route.params.id))
    },
    mounted() {
    },
    methods: {
        async load() {
            // TODO: GET RECORD FROM DATABASE
            console.log(`${this.$options.name}.vue | load()`)
        },
        async save() {
            // TODO: POST RECORD TO DATABASE
            console.log(`${this.$options.name}.vue | save()`)
            this.wait = true
            await sleep(Math.random() * 1300)
            // let ind = store.users.findIndex((e) => (e.id === this.$route.params.id))
            store.users[this.index] = Object.assign({}, this.user)
            this.wait = false
        },
        handleDeletion() {
            this.dialog.deletion = true
        },
        async remove() {
            // TODO: DELETE RECORD IN DATABASE
            console.log(`${this.$options.name}.vue | remove()`)
            store.users.splice(this.index, 1)
            this.$router.push({ name: 'Admin' })
        },
        setEditMode(val) {
            console.log(`${this.$options.name}.vue | setEditMode(${val})`)
            this.edit = val
        }
    }
}
</script>

<style scoped></style>
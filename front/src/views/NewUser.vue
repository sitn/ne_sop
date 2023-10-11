<template>
    <div class="">

        <q-layout>

            <!-- BREADCRUMBS NAVIGATION -->
            <div class="q-pa-sm q-gutter-sm">
                <q-breadcrumbs style="font-size: 16px">
                    <q-breadcrumbs-el label="Administration" to="/admin" />
                    <q-breadcrumbs-el label="Nouvel utilisateur" />
                </q-breadcrumbs>
            </div>

            <!-- FORM -->
            <UserForm v-model="user" :edit="edit"></UserForm>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="edit" :wait="wait" :buttons="actionButtons" @save-event="save" @edit-event="setEditMode"></FloatingButtons>

        </q-layout>
    </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import FloatingButtons from "../components/FloatingButtons.vue"
import UserForm from "../components/UserForm.vue"

export default {
    name: 'NewUser',
    components: { FloatingButtons, UserForm },
    props: {},
    emits: [],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            // actionButtons: { save: 'active', deletion: 'none' },
            edit: true,
            wait: false,
            user: {
                "id": uuidv4(),
                "name": "",
                "email": "",
                "admin": false,
                "active": true,
                "groups": []
            },
            index: store.users.findIndex((e) => (e.id === this.$route.params.id)),
            groupOptions: store.entities.filter((x) => (x.type === "Service de l'état"))
        }
    },
    computed: {
    },
    created() {
        console.log(`router id: ${this.$route.params.id}`)
        // this.user = Object.assign({}, store.users.find(e => e.id === this.$route.params.id))
        this.user = {
            "id": uuidv4(),
            "name": "",
            "email": "",
            "admin": false,
            "active": true,
            "groups": [],
            "valid": false
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
            store.users.push(Object.assign({}, this.user))
            this.wait = false

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
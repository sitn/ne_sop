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

            <Form title="Utilisateur" :edit="false" :toggle="true" @editEvent="setEditMode">

                <template v-slot:body>

                    <!-- USER SECTION -->
                    <FormSection title="User">
                        <template v-slot:content>
                            <div class="text-h6">Utilisateur</div>

                            <div class="row q-col-gutter-lg q-py-md">

                                <!-- NAME TEXT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input bg-color="white" outlined v-model="user.name" label="Nom" :disable="!edit" />
                                </div>

                                <!-- EMAIL TEXT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-input bg-color="white" outlined v-model="user.email" label="Email" :disable="!edit" />
                                </div>
                            </div>

                            <div class="row q-py-md">

                                <!-- ADMIN CHECKBOX FIELD -->
                                <q-item tag="label" v-ripple :disable="!edit">
                                    <q-item-section avatar>
                                        <q-checkbox v-model="user.admin" val="true" color="blue" :disable="!edit" />
                                    </q-item-section>
                                    <q-item-section>
                                        <q-item-label>Administrateur</q-item-label>
                                        <q-item-label caption>Accès administrateur</q-item-label>
                                    </q-item-section>
                                </q-item>


                                <!-- ACTIVE CHECKBOX FIELD -->
                                <q-item tag="label" v-ripple :disable="!edit">
                                    <q-item-section avatar>
                                        <q-checkbox v-model="user.active" val="true" color="blue" :disable="!edit" />
                                    </q-item-section>
                                    <q-item-section>
                                        <q-item-label>Actif</q-item-label>
                                        <q-item-label caption>Compte utilisateur actif</q-item-label>
                                    </q-item-section>
                                </q-item>

                            </div>

                            <div class="row q-col-gutter-lg q-py-md">

                                <!-- GROUPS SELECT FIELD -->
                                <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                                    <q-select bg-color="white" outlined v-model="user.groups" multiple :options="groupOptions" option-label="name" option-value="name" label="Groupe(s)" emit-value clearable :disable="!edit">

                                        <template v-slot:option="scope">
                                            <q-item v-bind="scope.itemProps">
                                                <q-item-section>
                                                    <q-item-label>{{ scope.opt.name }}</q-item-label>
                                                    <q-item-label caption>{{ scope.opt.type }}</q-item-label>
                                                </q-item-section>
                                            </q-item>
                                        </template>

                                    </q-select>
                                </div>

                            </div>

                            <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                                <div>user</div>
                                <div>{{ user }}</div>
                            </div>

                            <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                                <div>store.users</div>
                                <div>{{ store.users.find(e => e.id === this.$route.params.id) }}</div>
                            </div>

                        </template>
                    </FormSection>

                    <!-- GROUPS SECTION -->
                    <FormSection title="User">
                        <template v-slot:content>
                            <div class="text-h6">Groupes</div>


                        </template>
                    </FormSection>

                </template>

            </Form>

            <!-- FLOATING ACTION BUTTONS -->
            <FloatingButtons :edit="false" :wait="wait" @save-event="save" @edit-event="setEditMode"></FloatingButtons>

        </q-layout>
    </div>
</template>

<script>
import { store } from '../store/store.js'
import { sleep } from '../store/shared.js'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"
import FloatingButtons from "../components/FloatingButtons.vue"

export default {
    name: 'User',
    components: { Form, FormSection, FloatingButtons },
    props: {},
    emits: [],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            edit: false,
            wait: false,
            user: null,
            groupOptions: store.entities.filter((x) => (x.type === "Service de l'état"))
        }
    },
    computed: {
    },
    created() {
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
            let ind = store.users.findIndex((e) => (e.id === this.$route.params.id))
            store.users[ind] = Object.assign({}, this.user)
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
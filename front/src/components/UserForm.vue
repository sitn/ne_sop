<!-- 
    https://vuejs.org/guide/components/v-model.html
-->
<template>
    <Form :model="user" :edit="edit">

        <template v-slot:body>

            <!-- USER SECTION -->
            <FormSection title="Utilisateur">
                <template v-slot:content>

                    <div class="row q-col-gutter-lg q-py-md">

                        <!-- NAME TEXT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input bg-color="white" outlined v-model="user.name" label="Nom" :rules="[v => checkFilled(v)]" :disable="!edit" />
                        </div>

                        <!-- EMAIL TEXT FIELD -->
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input bg-color="white" outlined v-model="user.email" label="Email" :rules="[v => checkEmail(v, false)]" :disable="!edit" />
                        </div>
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



                    <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                        <div>edit</div>
                        <div>{{ edit }}</div>
                    </div>

                    <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                        <div>user</div>
                        <div>{{ user }}</div>
                    </div>

                    <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                        <div>store.users</div>
                        <div>{{ store.users.find(e => e.id === this.user.id) }}</div>
                    </div>

                </template>
            </FormSection>

            <!-- GROUPS SECTION -->
            <!-- 
            <FormSection title="User">
                <template v-slot:content>
                    <div class="text-h6">Groupes</div>

                </template>
            </FormSection>
            -->

        </template>

    </Form>
</template>

<script>
import { store } from '../store/store.js'
import { checkFilled, checkEmail } from '../store/shared.js'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"

export default {
    name: 'UserForm',
    components: { Form, FormSection },
    props: { 'edit': Boolean, 'modelValue': Object },
    emits: ['update:modelValue'],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            groupOptions: store.entities.filter((x) => (x.type === "Service de l'état"))
        }
    },
    computed: {
        user: {
            get() {
                return this.modelValue
            },
            set(user) {
                this.$emit('update:modelValue', user)
            }
        }
    },
    created() {
        console.log(`${this.$options.name} | router id: ${this.$route.params.id}`)
    },
    mounted() {
    },
    methods: {
        checkFilled,
        checkEmail
    }
}
</script>

<style scoped></style>
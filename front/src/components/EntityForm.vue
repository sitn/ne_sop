<template>
    <Form :model="entity" :edit="edit" :changewatch="changewatch">
        <!-- @validation-event="validation" -->

        <template v-slot:body>

            <!-- IDENTIFICATION SECTION -->
            <FormSection title="Identification">
                <template v-slot:content>

                    <div class="row q-col-gutter-lg q-py-md">

                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <!-- NAME TEXT FIELD -->
                            <q-input bg-color="white" outlined v-model="entity.name" label="Nom" :rules="[v => checkFilled(v)]" :disable="!edit" />
                        </div>

                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <!-- TYPE SELECT FIELD -->
                            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">

                                <q-select bg-color="white" outlined v-model="entity.type" :options="entityTypes" option-label="name" option-value="id" emit-value map-options label="Type" clearable :rules="[v => checkFilled(v)]" :disable="!edit">
                                    <template v-slot:option="scope">
                                        <q-item v-bind="scope.itemProps">
                                            <q-item-section>
                                                <q-item-label>{{ scope.opt.name }}</q-item-label>
                                            </q-item-section>
                                        </q-item>
                                    </template>
                                </q-select>

                            </div>

                        </div>

                    </div>

                    <!-- DESCRIPTION FIELD -->
                    <div class="row q-col-gutter-lg q-py-md">
                        <div class="col">
                            <q-input bg-color="white" outlined v-model="entity.description" label="Description" type="textarea" :disable="!edit" />
                        </div>
                    </div>

                    <!-- TODO REMOVE/DEV DISPLAY JSON-->
                    <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
                        <div>entity</div>
                        <div>{{ entity }}</div>
                    </div>

                </template>
            </FormSection>

            <!-- ADDRESS SECTION -->
            <FormSection title="Addresse">
                <template v-slot:content>

                    <div class="row q-col-gutter-lg q-py-md">
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input bg-color="white" outlined v-model="entity.street" label="Rue" :disable="!edit" />
                        </div>
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input bg-color="white" outlined v-model="entity.postalcode" label="Code postal" :disable="!edit" />
                        </div>
                    </div>

                    <div class="row q-col-gutter-lg q-py-md">
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input bg-color="white" outlined v-model="entity.city" label="Localité" :disable="!edit" />
                        </div>
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input bg-color="white" outlined v-model="entity.region" label="Canton / Région" :disable="!edit" />
                        </div>
                    </div>
                    <div class="row q-col-gutter-lg q-py-md">
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input bg-color="white" outlined v-model="entity.country" label="Pays" :disable="!edit" />
                        </div>

                    </div>

                </template>
            </FormSection>

            <!-- CONTACT SECTION -->
            <FormSection title="Contact">
                <template v-slot:content>

                    <div class="row q-col-gutter-lg q-py-md">
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input type="email" bg-color="white" outlined v-model="entity.email" label="Email" :rules="[v => checkEmail(v, true)]" :disable="!edit" />
                            <!-- <q-input type="email" bg-color="white" outlined v-model="entity.email" label="Email" :rules="[val => checkEmail(val)]" :disable="!edit" /> -->
                        </div>
                        <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6">
                            <q-input type="tel" bg-color="white" outlined v-model="entity.telephone" label="Téléphone (format international)" :rules="[v => checkPhoneNumber(v, true)]" :disable="!edit" />
                            <!--    <q-input type="tel" bg-color="white" outlined v-model="entity.telephone" label="Téléphone (format international)" @update:model-value="checkPhoneNumber(this.entity.telephone)" @blur="formatPhoneNumber(this.entity.telephone)" :rules="[val => checkPhoneNumber(val)]" :disable="!edit" />
                         -->
                        </div>
                    </div>

                    <div class="row">
                        <div class="col">
                            <q-input type="text" bg-color="white" outlined v-model="entity.website" label="Site Internet" :rules="[v => checkWebsite(v, true)]" :disable="!edit" />
                            <!-- <q-input type="text" bg-color="white" outlined v-model="entity.website" label="Site Internet" :rules="[val => checkWebsite(val)]" :disable="!edit" /> -->

                        </div>
                    </div>

                </template>
            </FormSection>

        </template>

    </Form>
</template>

<script>
import { store } from '../store/store.js'
import { checkFilled, checkPhoneNumber, formatPhoneNumber, checkEmail, checkWebsite } from '../store/shared.js'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"

export default {
    name: 'EntityForm',
    components: { Form, FormSection },
    props: { 'edit': Boolean, 'modelValue': Object, 'changewatch': { type: Boolean, default: true } },
    emits: ['update:modelValue'],
    setup() {
        return {
        }
    },
    data() {
        return {
            store,
            entityTypes: [],
        }
    },
    computed: {
        entity: {
            get() {
                return this.modelValue
            },
            set(entity) {
                this.$emit('update:modelValue', entity)
            }
        }
    },
    watch: {
        modelValue: {
            handler(newValue, oldValue) {

                store.entity.new = JSON.stringify(this.modelValue)

                if (this.changewatch) {
                    store.updateWarning(store.entity)
                }

            },
            deep: true
        },
    },
    mounted() {
        store.entity.old = JSON.stringify(this.entity)
    },
    async created() {
        this.entityTypes = await this.store.getEntityTypes()
        // console.log(`${this.$options.name} | router id: ${this.$route.params.id}`)
    },
    methods: {
        checkFilled,
        checkPhoneNumber,
        formatPhoneNumber,
        checkEmail,
        checkWebsite
    }
}
</script>

<style scoped></style>
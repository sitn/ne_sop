<template>
    <div class="">

        <!-- BREADCRUMBS NAVIGATION -->
        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Administration" to="/admin" />
            </q-breadcrumbs>
        </div>

        <Form title="Objets parlementaires" :edit="false" :toggle="false">

            <template v-slot:body>

                <!-- USERS LIST TABLE -->
                <FormSection title="Utilisateurs">
                    <template v-slot:content>
                        <div class="text-h6">Utilisateurs</div>

                        <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" :filter="filter" class="q-my-lg">
                            <!-- TABLE BODY -->
                            <template v-slot:body="props">
                                <q-tr :props="props">

                                    <!-- NAME COLUMN -->
                                    <q-td key="name" :props="props">

                                        <router-link :to="{
                                            name: 'User',
                                            params: {
                                                id: props.row.id
                                            }
                                        }">
                                            {{ props.row.name }}
                                        </router-link>

                                    </q-td>

                                    <!-- ACTIVE COLUMN -->
                                    <q-td key="active" :props="props">

                                        {{ props.row.active }}

                                    </q-td>

                                    <!-- ACTIONS COLUMN -->
                                    <q-td key="actions" :props="props">
                                        <div class="float-right">
                                            <q-btn dense round flat color="red" name="delete" @click="console.log(props.row.id)" icon="sym_o_delete">
                                                <q-tooltip class="bg-black">Supprimer</q-tooltip>
                                            </q-btn>
                                        </div>
                                    </q-td>
                                </q-tr>
                            </template>
                            <template v-slot:no-data>
                                Aucun objet
                            </template>
                        </q-table>

                    </template>
                </FormSection>

            </template>

        </Form>

    </div>
</template>

<script>
import { store } from '../store/store.js'
import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"

export default {
    name: 'Admin',
    components: { Form, FormSection },
    props: { 'model': Object },
    emits: [],
    setup() {
        return {

            // model: ref(null),
        }
    },
    data() {
        return {
            store,
            rows: store.users,
            loading: false,
            filter: "",
            pagination: {
                sortBy: "desc",
                descending: false,
                page: 1,
                rowsPerPage: 20,
            },
            columns: [
                {
                    name: "name",
                    align: "left",
                    label: "Nom",
                    field: "name",
                    sortable: true,
                },
                {
                    name: "active",
                    align: "center",
                    label: "Actif",
                    field: "active",
                    sortable: true,
                },
                {
                    name: "actions",
                    align: "center",
                    label: "",
                    field: "",
                    sortable: false,
                },
            ],
        }
    },
    computed: {
    },
    mounted() {

    },
    methods: {

    }
}
</script>

<style scoped></style>
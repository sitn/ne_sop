<template>
    <div class="">

        <!-- BREADCRUMBS NAVIGATION -->
        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Utilisateurs" to="/users" />
            </q-breadcrumbs>
        </div>

        <!-- USERS TABLE -->
        <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" :filter="filter" class="q-my-lg">
            <!-- TABLE BODY -->
            <template v-slot:body="props">
                <q-tr :props="props">

                    <!-- NAME COLUMN -->
                    <q-td key="user" :props="props">

                        <router-link :to="{
                            name: 'User',
                            params: {
                                id: props.row.id
                            }
                        }">
                        </router-link>
                        <div>{{ props.row.name }}</div>

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

    </div>
</template>

<script>
import { store } from '../store/store.js'

export default {
    name: 'UsersList',
    components: {},
    props: { 'title': String, 'model': Object },
    emits: [],
    setup() {
        return {
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
                    field: "",
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
    created() {
    },
    mounted() {

    },
    methods: {

    }
}
</script>

<style scoped></style>
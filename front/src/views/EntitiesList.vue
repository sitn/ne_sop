<template>
    <div class="">

        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Personnes et groupes" to="/entities" />
            </q-breadcrumbs>
        </div>

        <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading"
            :filter="filter" dense class="q-my-lg">
            <!-- TABLE BODY -->
            <template v-slot:body="props">
                <q-tr :props="props">
                    <!-- name  column -->
                    <q-td key="type" :props="props">

                        <router-link :to="{
                            name: 'Entity',
                            params: {
                                id: props.row.id
                            }
                        }">
                            {{ props.row.name }}
                        </router-link>

                    </q-td>

                    <!-- type column -->
                    <q-td key="type" :props="props">
                        {{ props.row.type }}
                    </q-td>
                    <!-- title column -->

                    <!-- actions column -->
                    <q-td key="actions" :props="props">
                        <q-btn dense round flat color="grey" name="email" @click="console.log(props.row.email)"
                            icon="email"></q-btn>
                        <q-btn dense round flat color="grey" name="phone" @click="console.log(props.row.telephone)"
                            icon="phone"></q-btn>
                        <q-btn dense round flat color="grey" name="delete" @click="console.log(props.row.id)"
                            icon="delete"></q-btn>
                    </q-td>
                </q-tr>
            </template>
            <template v-slot:no-data>
                Aucune objet
            </template>
        </q-table>

    </div>
</template>


<script>
import items from '../assets/data/items.json'
import entities from '../assets/data/entities.json'

export default {
    name: 'EntitiesList',
    components: {},
    props: { 'title': String, 'model': Object }, // 'rows': items
    emits: [],
    setup() {
        return {
            // model: ref(null),
        }
    },
    data() {
        return {
            rows: entities,
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
                    name: "type",
                    align: "left",
                    label: "Type",
                    field: "type",
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
<template>
    <div class="">

        <div class="q-pa-sm q-gutter-sm">

            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Objets parlementaires" to="/items" />
            </q-breadcrumbs>

            <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination"
                :loading="loading" :filter="filter" dense class="q-my-lg">
                <!-- TABLE BODY -->
                <template v-slot:body="props">
                    <q-tr :props="props">
                        <!-- number column -->
                        <q-td key="number" :props="props">
                            {{ props.row.number }}
                        </q-td>
                        <!-- type column -->
                        <q-td key="type" :props="props">
                            {{ props.row.type }}
                        </q-td>
                        <!-- title column -->
                        <q-td key="title" :props="props">

                            <router-link :to="{
                                name: 'Item',
                                params: {
                                    id: props.row.id
                                }
                            }">
                                {{ props.row.title }}
                            </router-link>

                        </q-td>
                        <!-- deposit date column -->
                        <q-td key="deposit" :props="props">
                            {{ props.row.events.find((e) => e.name === "Dépôt").date }}
                        </q-td>
                        <!-- delay date column -->
                        <q-td key="delay" :props="props">
                            {{ props.row.events.find((e) => e.name === "Délai").date }}
                        </q-td>
                        <!-- actions column -->
                        <q-td key="actions" :props="props">
                            <q-btn dense round flat color="grey" name="delete" @click="console.log(props.row)" icon="sym_o_delete"></q-btn>
                        </q-td>
                    </q-tr>
                </template>
                <template v-slot:no-data>
                    Aucune objet
                </template>
            </q-table>

        </div>

    </div>
</template>

<script>
import items from '../assets/data/items.json'

export default {
    name: 'ItemsList',
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
            rows: items,
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
                    name: "number",
                    align: "left",
                    label: "N°",
                    field: "number",
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
                    name: "title",
                    align: "left",
                    label: "Titre",
                    field: "title",
                    sortable: true,
                },
                {
                    name: "deposit",
                    align: "left",
                    label: "Dépôt",
                    field: "events",
                    sortable: true,
                },
                {
                    name: "delay",
                    align: "left",
                    label: "Délai",
                    field: "events",
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
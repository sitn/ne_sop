<template>
    <div class="">

        <!-- BREADCRUMBS NAVIGATION -->
        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Personnes et groupes" to="/entities" />
            </q-breadcrumbs>
        </div>

        <!-- ENTITIES TABLE -->
        <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" :filter="filter" dense class="q-my-lg">
            <!-- TABLE BODY -->
            <template v-slot:body="props">
                <q-tr :props="props">

                    <!-- NAME COLUMN -->
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

                    <!-- TYPE COLUMN -->
                    <q-td key="type" :props="props">
                        {{ props.row.type }}
                    </q-td>

                    <!-- ACTIONS COLUMN -->
                    <q-td key="actions" :props="props">
                        <div class="float-right">
                            <q-btn dense round flat color="grey" :name="email" @click="console.log(props.row.email)" icon="sym_o_mail" :href="`mailto:${props.row.email}`" v-if="props.row.email !== ''">
                                <q-tooltip class="bg-black" v-if="props.row.email !== ''">Envoyer un email: {{ props.row.email }}</q-tooltip>
                            </q-btn>
                            <q-btn dense round flat color="grey" name="phone" @click="console.log(props.row.telephone)" icon="sym_o_call" :href="`tel:${props.row.telephone}`" v-if="props.row.telephone !== ''">
                                <q-tooltip class="bg-black" v-if="props.row.telephone !== ''">Appeler: {{ props.row.telephone }}</q-tooltip>
                            </q-btn>
                            <q-btn dense round flat color="red" name="delete" @click="console.log(props.row.id)" icon="sym_o_delete">
                                <q-tooltip class="bg-black">Supprimer</q-tooltip>
                            </q-btn>
                        </div>
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
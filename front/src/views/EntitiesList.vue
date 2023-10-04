<template>
    <div class="">

        <div class="q-pa-sm q-gutter-sm">
            <!-- BREADCRUMBS NAVIGATION -->

            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Personnes et groupes" to="/entities" />
            </q-breadcrumbs>


            <div class="row q-col-gutter-md q-px-sm q-mt-xs items-center">

                <!-- SEARCH ITEMS FIELD -->
                <div class="col-xs-12 col-sm-8 col-md-6 col-lg-6">
                    <q-input bg-color="white" v-model="searchString" outlined dense placeholder="Rechercher" @update:model-value="query()">
                        <template v-slot:prepend>
                            <q-icon name="sym_o_search" />
                        </template>
                        <template v-slot:append>
                            <q-spinner color="blue-grey" :thickness="3" v-if="loading" />
                            <q-btn unelevated icon="sym_o_filter_alt" padding="xs" @click="console.log('filter')"> <!-- color="orange-1" text-color="black" -->
                                <q-tooltip class="bg-black">Filtrer</q-tooltip>
                            </q-btn>
                        </template>

                    </q-input>
                </div>

                <!-- ADD NEW ITEM BUTTON -->
                <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6">
                    <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" class="q-py-none q-my-none" @click="" to="/entities/new">
                        <q-tooltip class="bg-black">Ajouter une nouvelle entité</q-tooltip>
                    </q-btn>
                </div>

            </div>

            <!-- ENTITIES TABLE -->
            <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" :filter="filter" class="q-my-lg">
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
                                <q-btn dense round flat color="grey" name="email" @click="console.log(props.row.email)" icon="sym_o_mail" :href="`mailto:${props.row.email}`" v-if="props.row.email !== ''">
                                    <q-tooltip class="bg-black" v-if="props.row.email">Envoyer un email: {{ props.row.email }}</q-tooltip>
                                </q-btn>
                                <q-btn dense round flat color="grey" name="phone" @click="console.log(props.row.telephone)" icon="sym_o_call" :href="`tel:${props.row.telephone}`" v-if="props.row.telephone !== ''">
                                    <q-tooltip class="bg-black" v-if="props.row.telephone">Appeler: {{ props.row.telephone }}</q-tooltip>
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

    </div>
</template>

<script>
import { store } from '../store/store.js'
// import entities from '../assets/data/entities.json'

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms))

export default {
    name: 'EntitiesList',
    components: {},
    props: { 'title': String, 'model': Object },
    emits: [],
    setup() {
        return {
            // model: ref(null),
        }
    },
    data() {
        return {
            store,
            searchString: null,
            rows: store.entities,
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
    created() {
    },
    mounted() {

    },
    methods: {
        async query() {

            // TODO: REPLACE WITH GET CALL TO DATABASE 
            console.log(`search: ${this.searchString}`)
            this.loading = true
            await sleep(Math.random() * 1300)

            let str = this.searchString.toLowerCase()
            if (this.searchString.length >= 3) {

                this.rows = this.store.entities.filter((x) => (x.name.toLowerCase().includes(str)))
                console.log(this.rows)

            } else {

                this.rows = this.store.entities

            }
            this.loading = false

        },
    }
}
</script>

<style scoped></style>
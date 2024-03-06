<template>
    <div class="q-pa-sm q-gutter-sm">

        <!-- BREADCRUMBS NAVIGATION -->
        <q-breadcrumbs style="font-size: 16px">
            <q-breadcrumbs-el label="Parlementaires" to="/entities" />
        </q-breadcrumbs>

        <!-- SEARCH AND FILTER SECTION -->
        <div class="row q-col-gutter-md q-px-sm q-mt-xs items-center">

            <!-- SEARCH RECORDS FIELD -->
            <div class="col-xs-12 col-sm-8 col-md-6 col-lg-6">
                <q-input bg-color="white" v-model="filter.search" outlined dense placeholder="Rechercher"> <!-- @update:model-value="query()" -->
                    <template v-slot:prepend>
                        <q-icon name="sym_o_search" />
                    </template>

                    <template v-slot:append>
                        <q-spinner color="blue-grey" :thickness="3" v-if="loading" />
                        <!-- FILTER BUTTON -->
                        <!--
                            <q-btn unelevated icon="sym_o_filter_alt" padding="xs" @click="console.log('filter')">
                                <q-tooltip class="bg-black">Filtrer</q-tooltip>
                            </q-btn>
                            -->
                    </template>
                </q-input>
            </div>

            <!-- ADD NEW RECORD BUTTON -->
            <div class="col-xs-12 col-sm-4 col-md-6 col-lg-6" v-if="store.user.is_manager">
                <q-btn padding="sm md" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" class="q-py-none q-my-none" @click="" to="/entities/new">
                    <q-tooltip class="bg-black">Ajouter une nouvelle entité</q-tooltip>
                </q-btn>
            </div>

        </div>

        <!-- ENTITIES TABLE -->
        <q-table title="" :rows="rows" :columns="columns" row-key="id" v-model:pagination="pagination" :loading="loading" @request="onRequest" binary-state-sort class="q-my-lg">

            <!-- TABLE BODY -->
            <template v-slot:body="props">
                <q-tr :props="props" :class="{ inactive: !props.row.active }">

                    <!-- NAME COLUMN -->
                    <q-td key="type" :props="props">

                        <router-link :to="{
                            name: 'Entity',
                            params: {
                                id: props.row.id
                            }
                        }">
                            {{ props.row.name }}
                            <span v-if="!props.row.active"> (désactivé)</span>
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
                            <q-toggle dense round flat name="deactivate" v-model="props.row.active" @update:model-value="deactivate(props.row)" checked-icon="check" color="green" unchecked-icon="clear" v-if="store.user.is_manager">
                                <q-tooltip class="bg-black">{{ props.row.active ? "Désactiver" : "Activer" }}</q-tooltip>
                            </q-toggle>
                            <!-- 
                            <q-btn dense round flat color="red" name="delete" @click="handleDeletion(props.row.id)" icon="sym_o_delete" v-if="store.user.is_manager">
                                <q-tooltip class="bg-black">Supprimer</q-tooltip>
                            </q-btn>
                            -->
                        </div>
                    </q-td>

                </q-tr>
            </template>

            <template v-slot:no-data>
                Aucune objet
            </template>
        </q-table>

    </div>

    <!-- DELETE DIALOG -->
    <!--
    <DeleteDialog v-model="dialog.deletion" @delete-event="remove" />
    -->
</template>

<script>
import { store } from '../store/store.js'
// import DeleteDialog from '../components/DeleteDialog.vue'

export default {
    name: 'EntitiesList',
    components: {}, // DeleteDialog
    props: { 'title': String },
    emits: [],
    data() {
        return {
            store,
            selected: null,
            filter: { search: "", service: "false", type: [] },
            dialog: { deletion: false },
            data: null,
            rows: [],
            loading: false,
            pagination: {
                rowsNumber: 0,
                sortBy: "type",
                descending: false,
                page: 1,
                rowsPerPage: 25,
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
    watch: {
        filter: {
            handler(newValue, oldValue) {
                // console.log(`${this.$options.name} | filter()`)
                this.query()
            },
            deep: true
        },
    },
    async created() {

        this.query()
    },
    methods: {
        async onRequest(props) {

            // update pagination object
            this.pagination = props.pagination
            this.pagination.rowsPerPage = props.pagination.rowsPerPage === 0 ? this.pagination.rowsNumber : props.pagination.rowsPerPage // rowsPerPage

            // update table rows
            this.query()

        },
        async query() {

            // console.log(`search: ${this.filter.search}`)
            this.loading = true
            this.data = await store.getEntities(this.filter, this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
            this.rows = this.data.results
            this.pagination.rowsNumber = this.data.nrows
            this.loading = false
        },
        /*
        handleDeletion(val) {
            this.selected = val
            this.dialog.deletion = true
        },
        */
        async deactivate(val) {
            this.selected = val
            let message = await store.updateEntity(val.id, { active: val.active })

            if (message) {
                this.query()
            }

        },
        async remove() {

            // console.log(`delete ${this.selected}`)
            // let message = await store.deleteEntity(this.selected)
            let message = await store.deactivateEntity(data.id)
            this.data = await store.getEntities(this.filter, this.pagination.page, this.pagination.rowsPerPage, this.pagination.sortBy, this.pagination.descending)
            this.rows = this.data.results

            if (message) {
                this.query()
            }


        }
    }
}
</script>

<style scoped>
.inactive {
    font-style: italic;
    color: grey;
}
</style>
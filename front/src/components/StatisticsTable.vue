<template>
    <q-table :rows="rows" :columns="columns" class="q-my-md" v-if="rows.length > 0"></q-table>

    <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
        {{ rows }}
        <br>
        <br>
        {{ columns }}
    </div>
</template>

<script>
import { store } from '../store/store.js'

export default {
    name: 'StatisticsTable',
    components: {},
    props: {},
    emits: [],
    data() {
        return {
            store,
            rows: [],
            loading: true,
            data: [],
            columns: []
        }
    },
    computed: {
    },
    async created() {

        this.loading = true
        this.data = await this.store.getNumberOfItemsPerYear()

        this.rows = this.data
        let n_col = Object.keys(this.data[0]).length

        this.columns = Object.keys(this.data[0]).map(x => {
            return {
                name: x,
                field: x,
                align: "right",
                label: x === "year" ? "Année" : x,
                sortable: true,
                headerStyle: `width: calc(100% / ${n_col})`,
            }
        })

        this.loading = false

    },
    methods: {
    }
}
</script>

<style scoped></style>
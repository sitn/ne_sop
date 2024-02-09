<template>
    <q-table :rows="rows" :columns="columns" class="q-my-md" v-if="rows.length > 0"></q-table>

    <!-- <div class="bg-light-blue-1 q-my-md q-pa-md" v-if="store.dev">
        {{ rows }}
        <br>
        <br>
        {{ columns }}
    </div> -->
</template>

<script>
import { store } from '../store/store.js'

export default {
    name: 'StatisticsTable',
    components: {},
    props: {
        data: { type: Array, default: () => [] }
    },
    emits: [],
    data() {
        return {
            store,
            rows: [],
            loading: true,
            columns: []
        }
    },
    computed: {
    },
    created() {

        this.loading = true

        this.computePercentage()

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
        computePercentage() {
            let row_sum
            this.data.forEach(row => {
                // compute total of objets by year
                row_sum = 0;
                for (const [key, value] of Object.entries(row)) {
                    if (key !== 'year') {
                        row_sum += value
                    }
                }

                // comput percentage
                for (const [key, value] of Object.entries(row)) {
                    if (key !== 'year') {
                        if (row_sum > 0) {
                            row[key] = `${value} (${((value / row_sum) * 100).toFixed(0)}%)`
                        } else {
                            row[key] = `${value} (-%)`
                        }
                    }
                }

            })

        }
    }
}
</script>

<style scoped></style>
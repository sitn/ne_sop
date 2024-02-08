<template>
    <!-- Breadcrumbs navigation -->
    <div class="q-pa-sm q-gutter-sm">
        <q-breadcrumbs style="font-size: 16px">
            <q-breadcrumbs-el label="Statistiques" to="/statistics" />
        </q-breadcrumbs>
    </div>

    <!-- Statistics section -->
    <FormSection title="Année de dépôt">
        <template v-slot:content>
            <StatisticsTable :data="data_deposition" v-if="data_deposition.length > 0"></StatisticsTable>
        </template>
    </FormSection>

    <FormSection title="Année de traitement">
        <template v-slot:content>
            <StatisticsTable :data="data_treatment" v-if="data_treatment.length > 0"></StatisticsTable>
        </template>
    </FormSection>
</template>

<script>
import { store } from '../store/store.js'
import FormSection from "../components/FormSection.vue"
import StatisticsTable from "../components/StatisticsTable.vue"
const host = import.meta.env.VITE_API_URL

export default {
    name: 'Help',
    components: { FormSection, StatisticsTable },
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
            data_deposition: [],
            data_treatment: [],

        }
    },
    async created() {
        this.data_deposition = await this.store.getNumberOfItemsDepositedPerYear()
        this.data_treatment = await this.store.getNumberOfItemsTreatedPerYear()
    },
    computed: {
    },
    watch: {
    },
    mounted() {
    },
    methods: {
    }
}
</script>

<style scoped></style>
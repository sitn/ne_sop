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
    <FormSection title="Année de traitement (retour au secrétériat général)">
        <template v-slot:content>
            <StatisticsTable :data="data_treatment" v-if="data_treatment.length > 0"></StatisticsTable>
        </template>
    </FormSection>

    <FormSection title="Nombre d'objets par service et par année de dépôt">
        <template v-slot:content>
            <StatisticsTable :data="data_services" v-if="data_services.length > 0"></StatisticsTable>
        </template>
    </FormSection>

    <FormSection title="Nombre d'objets par statut et par année de dépôt">
        <template v-slot:content>
            <StatisticsTable :data="data_itemstatus" v-if="data_itemstatus.length > 0"></StatisticsTable>
        </template>
    </FormSection>

    <FormSection title="Réponses urgentes et/ou écrites demandées et par année de dépôt">
        <template v-slot:content>
            <StatisticsTable :data="data_urgentWritten" v-if="data_urgentWritten.length > 0"></StatisticsTable>
        </template>
    </FormSection>
</template>

<script>
import { store } from '../store/store.js'
import FormSection from "../components/FormSection.vue"
import StatisticsTable from "../components/StatisticsTable.vue"

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
            data_services: [],
            data_itemstatus: [],
            data_urgentWritten: [],
        }
    },
    async created() {
        this.data_deposition = await this.store.getNumberOfItemsDepositedPerYear()
        this.data_treatment = await this.store.getNumberOfItemsTreatedPerYear()
        this.data_services = await this.store.getNumberOfServiceItemsPerYear()
        this.data_itemstatus = await this.store.getStatisticItemStatus()
        this.data_urgentWritten = await this.store.getStatisticItemUrgentWritten()
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
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
            <StatisticsTable></StatisticsTable>
        </template>
    </FormSection>
</template>

<script>
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

        }
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
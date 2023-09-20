<template>
    <div class="">

        <!-- Breadcrumbs navigation -->
        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Statistiques" to="/statistics" />
            </q-breadcrumbs>
        </div>

        <!-- Identification -->
        <FormSection title="Identification">
            <template v-slot:content>
                <div class="text-h6">Statistiques</div>

            </template>
        </FormSection>

    </div>
</template>

<script>
import FormSection from "../components/FormSection.vue"


export default {
    name: 'Help',
    components: { FormSection },
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
    mounted() {

    },
    methods: {

    }
}
</script>

<style scoped></style>
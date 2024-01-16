<template>
    <div class="">

        <!-- BREADCRUMBS NAVIGATION -->
        <div class="q-pa-sm q-gutter-sm">
            <q-breadcrumbs style="font-size: 16px">
                <q-breadcrumbs-el label="Aide" to="/help" />
            </q-breadcrumbs>
        </div>

        <!-- HELP -->
        <FormSection title="Question ou remarque ?">
            <template v-slot:content>
                <p>
                    N'hésitez pas à nous contacter: <a :href="mailtostring">{{ email_webmaster }}</a>.
                </p>
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
    data() {
        return {
            email_webmaster: import.meta.env.VITE_WEBMASTER_EMAIL,
        }
    },
    computed: {
        mailtostring() {
            return `mailto:${this.email_webmaster}&subject=SOP - Help`
        }
    },
    mounted() {
    },
    methods: {
    }
}
</script>

<style scoped></style>
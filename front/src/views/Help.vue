<template>
    <!-- BREADCRUMBS NAVIGATION -->
    <div class="q-pa-sm q-gutter-sm">
        <q-breadcrumbs style="font-size: 16px">
            <q-breadcrumbs-el label="Aide" to="/help" />
        </q-breadcrumbs>
    </div>

    <!-- <Form>
        <template v-slot:body> -->

    <!-- HELP -->
    <FormSection title="Question ou remarque ?">
        <template v-slot:content>
            <p>
                N'hésitez pas à nous contacter: <a :href="mailtostring">{{ email_webmaster }}</a>.
            </p>
        </template>
    </FormSection>

    <FormSection title="Enregistrement d'un objet parlementaire">

        <template v-slot:content>
            <p>
                Tous les champs du formulaire des objets parlementaires sont enregistrés lorsque l'utilisateur clique sur le bouton "enregistrer".
                C'est également le cas pour les évènements créés et pour les fichiers enregistrés.
                De même, les évènements supprimés le seront définitivement lorsque l'objet parlementaire est enregistré.
            </p>
            <p>
                <q-icon name="warning" color="warning" size="1.5rem" style="margin-right: 10pt;" /> La suppression de documents est un cas particulier: les documents supprimés sont définitivement supprimés lorsque l'utilisateur confirme leur suppression, même si l'objet parlementaire n'est pas enregistré.
            </p>
        </template>
    </FormSection>

    <FormSection title="Nouvel utilisateur / nouveau service" v-if="store.user.is_manager">

        <template v-slot:content>
            <p>
                Pour créer un nouvel utilisateur ou un nouveau service, envoyer son nom, son prénom et son service à <a :href="`mailto:${email_webmaster}&subject=SOP - Demande d'enregistrement d'un nouvel utilisateur`">{{ email_webmaster }}</a>.
            </p>
            <p style="font-style: italic;">
                La gestion des utilisateurs pourra prochainement être réalisée par les managers de l'application, au travers de l'active directory.
            </p>
        </template>
    </FormSection>

    <!-- </template>
    </Form> -->
</template>

<script>
// import Form from "../components/Form.vue"
import FormSection from "../components/FormSection.vue"
import { store } from "../store/store.js"


export default {
    name: 'Help',
    components: {
        // Form,
        FormSection
    },
    props: { 'model': Object },
    emits: [],
    data() {
        return {
            store,
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

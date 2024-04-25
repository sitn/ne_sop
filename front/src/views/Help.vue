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

    <FormSection title="Ajout d'un nouvel objet parlementaire">

        <template v-slot:content>
            <ol class="instructions">
                <li>Aller sur la page <a href="./items">Objets parlementaires</a></li>
                <li>Cliquer sur le bouton <q-btn size="sm" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" class="q-py-none q-my-none"></q-btn></li>
                <li>Dans la formulaire du nouvel objet parlementaire, remplir les champs obligatoires (en rouge)</li>
                <li>Pour indiquer l'auteur de l'objet, il y a deux options:</li>

                <ul>
                    <li>Choisir un parlementaire existant dans la liste déroulante ou;</li>
                    <li>Créer un nouveau parlementaire en cliquant sur le bouton <q-btn round unelevated size="sm" color="blue-grey-8" icon="sym_o_person_add"></q-btn></li>
                </ul>
                <li>Remplir la section calendrier</li>
                <li>Remplir la section documents</li>
                <li>Cliquer sur le bouton <kbd>Enregister</kbd> <q-btn round unelevated size="sm" color="green-5" icon="sym_o_save"></q-btn> en bas à droite</li>


            </ol>

            <p>
                Tous les champs du formulaire des objets parlementaires sont enregistrés lorsque l'utilisateur clique sur le bouton "enregistrer".
                C'est également le cas pour les évènements créés et pour les fichiers enregistrés.
                De même, les évènements supprimés le seront définitivement lorsque l'objet parlementaire est enregistré.
            </p>
            <p>
                <q-icon name="warning" color="warning" size="1.5rem" style="margin-right: 10pt;" /> La suppression de documents est un cas particulier: les documents supprimés sont définitivement supprimés lorsque l'utilisateur confirme leur suppression, même si l'objet parlementaire n'est pas enregistré.
            </p>

            <video controls width="600">
                <source src="video/2024-04-25 15-33-26.mp4" type="video/mp4" />
            </video>

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

<style scoped>
.instructions li {
    line-height: 2.2em;
    height: auto;
}
</style>

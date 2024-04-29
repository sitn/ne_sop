<template>
    <!-- BREADCRUMBS NAVIGATION -->
    <div class="q-pa-sm q-gutter-sm">
        <q-breadcrumbs style="font-size: 16px">
            <q-breadcrumbs-el label="Aide" to="/help" />
        </q-breadcrumbs>
    </div>

    <div class="q-pa-md example-col-gutter-size">
        <div class="row">

            <!-- Créer et éditer une personne ou un groupe parlementaire -->
            <div>
                <q-card class="my-card">
                    <q-card-section class="bg-blue-grey-5 text-grey-2">
                        <div class="title-format">Créer et éditer une personne ou un groupe parlementaire</div>
                    </q-card-section>

                    <video class="video-format" controls>
                        <source src="video/parlementaire_edition.mp4" type="video/mp4" />
                    </video>


                    <q-list class="rounded-borders">
                        <q-expansion-item
                            expand-separator
                            label="Créer une nouvelle personne ou un nouveau groupe parlementaire">
                            <q-card>
                                <q-card-section>
                                    <ol>
                                        <li>Cliquer sur <b>+ Ajouter</b></li>
                                        <li>Renseigner les champs du formulaire</li>
                                        <li>Cliquer sur <b>enregistrer</b> (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_save" class="icon-class" size="sm" /></span>), puis sur <b>fermer</b> (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_close" class="icon-class" size="sm" /></span>)</li>
                                    </ol>
                                </q-card-section>
                            </q-card>
                        </q-expansion-item>

                        <q-expansion-item
                            expand-separator
                            label="Modifier une personne ou un groupe parlementaire">
                            <q-card>
                                <q-card-section>
                                    <ol>
                                        <li>Cliquer sur l'entité</li>
                                        <li>Dans le formulaire, cliquer sur le bouton <b>modifier</b> (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_edit" class="icon-class" size="sm" /></span>)</li>
                                        <li>Mettre les données de l'entité à jour dans le formulaire</li>
                                        <li>Cliquer sur <b>enregistrer</b> (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_save" class="icon-class" size="sm" /></span>), puis sur <b>fermer</b> (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_close" class="icon-class" size="sm" /></span>)</li>
                                    </ol>
                                </q-card-section>
                            </q-card>
                        </q-expansion-item>

                        <q-expansion-item
                            expand-separator
                            label="Activer / désactiver une personne ou un groupe parlementaire">
                            <q-card>
                                <q-card-section>
                                    <ol>
                                        <li>Cliquer sur le bouton d'état (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_switches" class="icon-class" size="sm" /></span>) dans le tableau des parlementaires</li>
                                    </ol>
                                </q-card-section>
                            </q-card>
                        </q-expansion-item>
                    </q-list>
                </q-card>
            </div>


            <!-- Insert new content here -->

            <!-- <div></div> -->


        </div>

        <div class="row">
            <!-- Créer un nouvel utilisateur ou un nouveau service -->
            <div>
                <q-card class="my-card">
                    <q-card-section class="bg-blue-grey-5 text-grey-2">
                        <div class="title-format">Ajouter un utilisateur ou un service</div>
                    </q-card-section>

                    <q-card-section>
                        <p>
                            Pour créer un nouvel utilisateur ou un nouveau service, envoyer son nom, son prénom et son service à <a :href="`mailto:${email_webmaster}&subject=SOP - Demande d'enregistrement d'un nouvel utilisateur`">{{ email_webmaster }}</a>.
                        </p>
                        <p style="font-style: italic;">
                            La gestion des utilisateurs pourra prochainement être réalisée par les managers de l'application, au travers de l'active directory.
                        </p>
                    </q-card-section>
                </q-card>
            </div>

            <!-- Question ou remarque -->
            <div>
                <q-card class="my-card">
                    <q-card-section class="bg-blue-grey-5 text-grey-2">
                        <div class="title-format">Question ou remarque ?</div>
                    </q-card-section>

                    <q-card-section>
                        N'hésitez pas à nous contacter: <a :href="mailtostring">{{ email_webmaster }}</a>.
                    </q-card-section>
                </q-card>
            </div>
        </div>
    </div>



    <!-- HELP -->
    <!-- <FormSection title="Question ou remarque ?">
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

<FormSection title="Créer et éditer une personne / Groupe parlementaire" v-if="store.user.is_manager">
    <template v-slot:content>
            <br>
            <p>
            <div class="row">
                <div class="block">
                    Créer une nouvelle personne ou un nouveau groupe parlementaire
                    <ol>
                        <li>Cliquer sur <b>+ Ajouter</b></li>
                        <li>Renseigner les champs du formulaire</li>
                        <li>Cliquer sur <b>enregistrer</b> (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_save" class="icon-class" size="sm" /></span>), puis sur <b>fermer</b> (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_close" class="icon-class" size="sm" /></span>)</li>
                    </ol>
                </div>

                <div class="block">
                    Modifier une personne ou un groupe parlementaire
                    <ol>
                        <li>Cliquer sur l'entité</li>
                        <li>Dans le formulaire, cliquer sur le bouton <b>modifier</b> (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_edit" class="icon-class" size="sm" /></span>)</li>
                        <li>Mettre les données de l'entité à jour dans le formulaire</li>
                        <li>Cliquer sur <b>enregistrer</b> (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_save" class="icon-class" size="sm" /></span>), puis sur <b>fermer</b> (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_close" class="icon-class" size="sm" /></span>)</li>
                    </ol>
                </div>

                <div class="block">
                    Activer / désactiver une personne ou un groupe parlementaire
                    <ol>
                        <li>Cliquer sur le bouton d'état (<span class="text-blue q-gutter-md" style="line-height: 1.5em;"><q-icon name="sym_o_switches" class="icon-class" size="sm" /></span>) dans le tableau des parlementaires</li>
                    </ol>
                </div>
            </div>
            </p>

            <video class="video-format" controls>
                <source src="video/parlementaire_edition.mp4" type="video/mp4" />
            </video>
        </template>
</FormSection> -->

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
.video-format {
    width: inherit;
}

.row {
    width: 100%;
    margin: 0 auto;
}

/* .block {
    width: 550px;
    display: inline-block;
} */

.my-card {
    width: 550px;
    margin: 15px;

}

.my-card .icon-class {
    margin-top: 0;
}

.title-format{
    font-size: large;
}
</style>
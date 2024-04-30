<template>
    <!-- BREADCRUMBS NAVIGATION -->
    <div class="q-pa-sm q-gutter-sm">
        <q-breadcrumbs style="font-size: 16px">
            <q-breadcrumbs-el label="Aide" to="/help" />
        </q-breadcrumbs>
    </div>

    <div>
        <q-splitter v-model="splitterModel">

            <template v-slot:before>
                <div class="q-pa-md">
                    <q-tree :nodes="simple" node-key="label" selected-color="primary" v-model:selected="selected" default-expand-all />
                </div>
            </template>

            <template v-slot:after>
                <q-tab-panels v-model="selected" animated transition-prev="jump-up" transition-next="jump-up">

                    <!-- RESUME DU PROCESSUS -->
                    <q-tab-panel name="Résumé du processus">
                        <div class="text-h5 q-mb-md">Résumé du processus</div>
                        <p><a href="documents/SDTE_2023_TraitementObjetsDDTE.pdf" download>Télécharger (PDF)</a></p>
                        <img src="documents/SDTE_2023_TraitementObjetsDDTE.svg" alt="Résumé du processus" />
                    </q-tab-panel>

                    <!-- CREER UN NOUVEL OBJET -->
                    <q-tab-panel name="Créer un nouvel objet">

                        <div class="video-container">
                            <video controls autoplay>
                                <source src="video/edition_objet_parlementaire_1080p_titre5s.mp4#t=0,68" type="video/mp4" />
                            </video>
                        </div>

                        <div class="text-h5 q-my-md">Créer un nouvel objet</div>
                        <ol class="instructions">
                            <li>Aller sur la page <a href="./items">Objets parlementaires</a></li>
                            <li>Pour ouvrir le formulaire d'un nouvel objet, cliquer sur le bouton <q-btn size="sm" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" class="q-py-none q-my-none"></q-btn></li>
                            <li>Remplir la section <b>Informations générales</b>:</li>

                            <ul>
                                <li>Remplir les champs (obligatoirement le N°, le type et le titre de l'objet)</li>
                                <li>Pour indiquer l'auteur, choisir un parlementaire existant dans la liste déroulante ou
                                    créer un nouveau parlementaire en cliquant sur le bouton <q-btn round unelevated size="sm" color="blue-grey-8" icon="sym_o_person_add"></q-btn></li>
                            </ul>
                            <li>Remplir la section <b>Traitement</b>:</li>
                            <ul>
                                <li>Remplir les champs (obligatoirement le service principal, le statut)</li>
                                <li>Pour activer la notification automatique par email en cas de changement, cocher la case <b>Notification automatique</b></li>
                            </ul>
                            <li>Remplir la section <b>Calendrier</b>:</li>
                            <ul>
                                <li>Cliquer sur le bouton <q-btn size="sm" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" class="q-py-none q-my-none"></q-btn></li>
                                <li>Remplir les champs du menu flottant (obligatoirement la date et le type d'événement)</li>
                                <li>Répéter les points précédents pour chaque événement à ajouter</li>
                                <li>Vous pouvez modifier un événement, en cliquant sur le bouton <b>Modifier</b> <q-btn dense round flat color="blue" name="delete" icon="sym_o_edit"></q-btn> à la ligne correspondante</li>
                                <li>Vous pouvez supprimer définitivement un événement, en cliquant sur le bouton <b>Supprimer</b> <q-btn dense round flat color="red" name="delete" icon="sym_o_delete"></q-btn> à la ligne correspondante</li>
                            </ul>
                            <li>Remplir la section <b>Documents</b></li>
                            <ul>
                                <li>Cliquer sur le bouton <q-btn size="sm" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" class="q-py-none q-my-none"></q-btn></li>
                                <li>Remplir les champs du menu flottant (obligatoirement le fichier et le type de document)</li>
                                <li>Répéter les points précédents pour chaque document à ajouter</li>
                                <li>Vous pouvez supprimer définitivement un document, en cliquant sur le bouton <b>Supprimer</b> <q-btn dense round flat color="red" name="delete" icon="sym_o_delete"></q-btn> à la ligne correspondante</li>
                            </ul>
                            <li>Cliquer sur le bouton <b>Enregister</b> <q-btn round unelevated size="sm" color="green-5" icon="sym_o_save"></q-btn> en bas à droite</li>

                        </ol>

                        <!--
                        <p>
                            Tous les champs du formulaire des objets parlementaires sont enregistrés lorsque l'utilisateur clique sur le bouton "enregistrer".
                            C'est également le cas pour les évènements créés et pour les fichiers enregistrés.
                            De même, les évènements supprimés le seront définitivement lorsque l'objet parlementaire est enregistré.
                        </p>
                        <p>
                            <q-icon name="warning" color="warning" size="1.5rem" style="margin-right: 10pt;" /> La suppression de documents est un cas particulier: les documents supprimés sont définitivement supprimés lorsque l'utilisateur confirme leur suppression, même si l'objet parlementaire n'est pas enregistré.
                        </p>
                        -->


                    </q-tab-panel>

                    <!-- MODIFIER UN OBJET -->
                    <q-tab-panel name="Modifier un objet">

                        <div class="video-container">
                            <video controls autoplay>
                                <source src="video/edition_objet_parlementaire_1080p_titre5s.mp4#t=68,98" type="video/mp4" />
                            </video>
                        </div>

                        <div class="text-h5 q-my-md">Modifier un objet</div>

                        <ol class="instructions">
                            <li>Aller sur la page <a href="./items">Objets parlementaires</a></li>
                            <li>Cliquer sur le titre (lien souligné) de l'objet parlementaire à modifier, pour accéder au formulaire</li>
                            <li>Cliquer sur le bouton <b>Modifier</b> <q-btn round unelevated size="sm" color="blue" icon="sym_o_edit"></q-btn> en bas à droite, pour activer le formulaire</li>
                            <li>Modifier les champs souhaités dans le formulaire</li>
                            <li>Cliquer sur le bouton <b>Enregister</b> <q-btn round unelevated size="sm" color="green-5" icon="sym_o_save"></q-btn> en bas à droite</li>
                        </ol>

                    </q-tab-panel>

                    <!-- CREER UN NOUVEAU PARLEMENTAIRE -->
                    <q-tab-panel name="Supprimer un objet">

                        <div class="video-container">
                            <video controls autoplay>
                                <source src="video/edition_objet_parlementaire_1080p_titre5s.mp4#t=98" type="video/mp4" />
                            </video>
                        </div>

                        <div class="text-h5 q-my-md">Supprimer un objet</div>

                        <q-banner inline-actions class="text-white bg-red">
                            Attention la suppression d'un objet est définitive (aucune possibilité de récupération)
                            <template v-slot:avatar>

                                <q-icon name="front_hand" color="white" class="q-py-sm" />

                            </template>
                        </q-banner>

                        <ol class="instructions">
                            <li>Aller sur la page <a href="./items">Objets parlementaires</a></li>
                            <li>Cliquer sur le bouton <b>Supprimer</b> <q-btn dense round flat color="red" name="delete" icon="sym_o_delete"></q-btn> à la ligne de l'objet concerné</li>
                        </ol>

                    </q-tab-panel>


                    <!-- CREER UN NOUVEAU PARLEMENTAIRE -->
                    <q-tab-panel name="Créer un nouveau parlementaire">

                        <div class="video-container">
                            <video controls autoplay>
                                <source src="video/edition_parlementaire_1080p_titre5s.mp4#t=0,42" type="video/mp4" />
                            </video>
                        </div>

                        <div class="text-h5 q-my-md">Créer un nouveau parlementaire</div>

                        <ol class="instructions">
                            <li>Aller sur la page <a href="./entities">Parlementaires</a></li>
                            <li>Cliquer sur le bouton <q-btn size="sm" unelevated no-caps color="blue-grey-8" text-color="white" icon="sym_o_add_circle" label="Ajouter" class="q-py-none q-my-none"></q-btn></li>
                            <li>Remplir les champs du formulaire (obligatoirement nom et type)</li>
                            <li>Cliquer sur le bouton <b>Enregister</b> <q-btn round unelevated size="sm" color="green-5" icon="sym_o_save"></q-btn> en bas à droite</li>
                        </ol>

                    </q-tab-panel>


                    <!-- MODIFIER UN PARLEMENTAIRE -->
                    <q-tab-panel name="Modifier un parlementaire">

                        <div class="video-container">
                            <video controls autoplay>
                                <source src="video/edition_parlementaire_1080p_titre5s.mp4#t=42,73" type="video/mp4" />
                            </video>
                        </div>

                        <div class="text-h5 q-my-md">Modifier un parlementaire</div>

                        <ol class="instructions">
                            <li>Aller sur la page <a href="./entities">Parlementaires</a></li>
                            <li>Cliquer sur le nom (lien souligné) du parlementaire à modifier, pour accéder au formulaire</li>
                            <li>Cliquer sur le bouton <b>Modifier</b> <q-btn round unelevated size="sm" color="blue" icon="sym_o_edit"></q-btn> en bas à droite, pour activer le formulaire</li>
                            <li>Modifier les champs souhaités dans le formulaire</li>
                            <li>Cliquer sur le bouton <b>Enregister</b> <q-btn round unelevated size="sm" color="green-5" icon="sym_o_save"></q-btn> en bas à droite</li>
                        </ol>

                    </q-tab-panel>

                    <!-- ACTIVER/DESACTVER UN PARLEMENTAIRE -->
                    <q-tab-panel name="Activer/désactiver un parlementaire">

                        <div class="video-container">
                            <video controls autoplay>
                                <source src="video/edition_parlementaire_1080p_titre5s.mp4#t=73" type="video/mp4" />
                            </video>
                        </div>

                        <div class="text-h5 q-mb-md">Activer/désactiver un parlementaire</div>

                        <q-banner inline-actions class="text-white bg-blue">
                            La suppression d'un parlementaire ou d'un groupe parlementaire n'est pas possible, pour préserver l'intégrité référentielle des données
                            <template v-slot:avatar>

                                <q-icon name="info" color="white" class="q-py-sm" />

                            </template>
                        </q-banner>

                        <ol class="instructions">
                            <li>Aller sur la page <a href="./entities">Parlementaires</a></li>
                            <li>Cliquer sur le bouton d'état <q-toggle dense round flat name="deactivate" v-model="fakeToggle" checked-icon="check" color="green" unchecked-icon="clear"></q-toggle> dans le tableau des parlementaires</li>
                        </ol>

                    </q-tab-panel>


                    <!-- GESTION DES UTILISATEURS -->
                    <q-tab-panel name="Gestion des utilisateurs">
                        <div class="text-h5 q-mb-md">Gestion des utilisateurs</div>
                        <p>
                            Pour créer un nouvel utilisateur ou un nouveau service, envoyer son nom, son prénom et son service à <a :href="`mailto:${email_webmaster}&subject=SOP - Demande d'enregistrement d'un nouvel utilisateur`">{{ email_webmaster }}</a>.
                        </p>
                        <p style="font-style: italic;">
                            La gestion des utilisateurs pourra prochainement être réalisée par les managers de l'application, au travers de l'active directory.
                        </p>
                    </q-tab-panel>

                    <!-- SUPPORT -->
                    <q-tab-panel name="Support">
                        <div class="text-h5 q-mb-md">Support</div>
                        <p>N'hésitez pas à nous contacter: <a :href="mailtostring">{{ email_webmaster }}</a></p>
                    </q-tab-panel>

                </q-tab-panels>
            </template>
        </q-splitter>
    </div>

</template>

<script>
import { ref } from 'vue'
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
            fakeToggle: true,
            splitterModel: ref(25),
            selected: ref('Résumé du processus'),
            simple: [
                {
                    label: 'Sommaire',
                    children: [
                        { label: 'Résumé du processus' },
                        {
                            label: 'Objets parlementaires',
                            icon: 'sym_o_list_alt',
                            children: [
                                { label: 'Créer un nouvel objet' },
                                { label: 'Modifier un objet' },
                                { label: 'Supprimer un objet' }
                            ]
                        },
                        {
                            label: 'Parlementaires',
                            icon: 'sym_o_groups',
                            children: [
                                { label: 'Créer un nouveau parlementaire' },
                                { label: 'Modifier un parlementaire' },
                                { label: 'Activer/désactiver un parlementaire' }
                            ]
                        },
                        {
                            label: 'Gestion des utilisateurs',
                            icon: 'sym_o_manage_accounts'
                        },
                        {
                            label: 'Support',
                            icon: 'sym_o_live_help'
                        }
                    ]
                },

            ]
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

.video-container video {
    width: 100%;
    height: 500px;
    object-fit: contain;
}
</style>

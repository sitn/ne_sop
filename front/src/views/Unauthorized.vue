<template>
    <div class="unauthorized">
        <div class="q-pa-md">
            <div style="text-align: center;">
                <h2 class="text-red">Accès non autorisé</h2>
                <q-icon name="do_not_disturb_on" style="font-size: calc(min(30vw, 400pt)); max-width: 100px; color: rgba(255, 0, 0, 0.7);"></q-icon>
                <h4 class="text-red">Vous n'êtes pas autorisé·e à accéder à ce contenu.</h4>
                <p>Contacter le support: <a :href="mailtostring">{{ email_webmaster }}</a></p>
            
            </div>
        </div>
            

    </div>
</template>

<script>

export default {
    name: 'Unauthorized',
    data() {
        return {
            email_webmaster: import.meta.env.VITE_WEBMASTER_EMAIL,
        }
    },
    computed: {
        mailtostring() {
            return `mailto:${this.email_webmaster}&subject=SOP - Access`
        }
    },
}

</script>

<style scoped>
.unauthorized {
    padding-top: 40px;
    max-width: 50%;
    margin: auto;
}
</style>
<template>
    <div class="row justify-center q-my-lg">
        <div class="col-xs-12 col-sm-12 col-md-8">

            <!-- <div class="bg-blue-grey-6 text-white text-h5 q-pa-md q-mx-md">{{ title }}</div> -->
            <div class="bg-grey-2 q-pa-md q-mx-md">


                <!-- <q-form ref="form" greedy> -->

                <slot name="content"></slot>

                <!-- </q-form> -->

            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'FormSection',
    components: {},
    props: { 'title': String },
    emits: [],
    setup() {
        return {

        }
    },
    data() {
        return {
            model: null,
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
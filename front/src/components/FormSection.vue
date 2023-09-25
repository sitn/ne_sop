<template>
    <div class="row justify-center q-mb-lg">
        <!-- <div class="col-xs-12 col-sm-12 col-md-8"> -->

        <div class="col bg-grey-2 q-pa-md">

            <slot name="content"></slot>

        </div>


    </div>
    <!--  </div> -->
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
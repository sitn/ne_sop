<template>
    <div class="row justify-center q-my-lg">

        <div class="col" style="max-width: 880px;"> <!-- -xs-12 col-sm-12 col-md-8 -->

            <div class="row justify-center">
                <div class="col">
                    <q-form ref="form" @validation-success="validationSuccess" @validation-error="validationError" greedy>
                        <slot name="body"></slot>
                    </q-form>
                </div>
            </div>

        </div>

    </div>
</template>

<script>

export default {
    name: 'Form',
    components: {},
    props: { 'title': String, 'edit': Boolean, 'toggle': Boolean },
    emits: ['editEvent', 'validationEvent'],
    setup() {
        return {

        }
    },
    data() {
        return {
            model: null,
            editMode: this.edit,
            valid: null,
        }
    },
    computed: {
    },
    mounted() {
        // this.validateForm()
    },
    updated() {
        this.validateForm()
    },
    methods: {
        /*
        toggleEdit() {
            console.log('toggleEdit')
            this.$emit('editEvent', this.editMode)
        },
        */
        validateForm() {
            if (this.$refs.hasOwnProperty('form')) {
                if (this.$refs.form !== null) {
                    this.$nextTick(() => { this.$refs.form.validate() })
                }
            }
        },
        validationSuccess() {
            console.log('validationSuccess')
            this.valid = true
            this.$emit('validationEvent', this.valid)
        },
        validationError() {
            console.log('validationError')
            this.valid = false
            this.$emit('validationEvent', this.valid)
        },
    }
}
</script>

<style scoped></style>
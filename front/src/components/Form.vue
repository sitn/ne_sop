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

        <!-- FLOATING ACTION BUTTONS -->
        <!-- <FloatingButtons :edit="true" :wait="true" :buttons="{ save: 'active', deletion: 'none' }"></FloatingButtons> -->


    </div>
</template>

<script>
import { store } from '../store/store.js'

export default {
    name: 'Form',
    components: {},
    props: { 'edit': Boolean, 'model': Object }, // { 'title': String, 'edit': Boolean, 'toggle': Boolean },
    emits: ['editEvent', 'validationEvent'],
    setup() {
        return {

        }
    },
    data() {
        return {
            editMode: this.edit,
            valid: null,
        }
    },
    computed: {
    },
    mounted() {
        this.validateForm()
    },
    updated() {
        this.validateForm()
    },
    watch: {
        model: {
            handler(newValue, oldValue) {
                console.log(`${this.$options.name} | watch`)
                this.validateForm()
            },
            deep: true
        },
        edit: {
            handler(newValue, oldValue) {
                console.log(`${this.$options.name} | watch edit`)
                this.validateForm()
            }
        }
    },
    methods: {
        validateForm() {
            this.$nextTick(() => { this.$refs.form.validate() })

            /*
            if (this.$refs.hasOwnProperty('form')) {
                if (this.$refs.form !== null) {
                    this.$nextTick(() => { this.$refs.form.validate() })
                }
            }
            */

        },
        validationSuccess() {
            console.log(`${this.$options.name} | validationSuccess()`)
            this.valid = true
            this.$emit('validationEvent', true)
            store.valid = true
        },
        validationError() {
            console.log(`${this.$options.name} | validationError()`)
            this.valid = false
            this.$emit('validationEvent', false)
            store.valid = false
        },
    }
}
</script>

<style scoped></style>
/*
export default {
    foo: function () { alert("foo!") }
}
*/
import parsePhoneNumber from 'libphonenumber-js'
import { date } from 'quasar'

export const sleep = ms => new Promise(resolve => setTimeout(resolve, ms))

export const checkPhoneNumber = (val, allowEmpty = true) => {

    if (allowEmpty && val === '') {
        return true
    }

    let phoneNumber = parsePhoneNumber(val)
    if (phoneNumber) {
        return phoneNumber.isPossible() & phoneNumber.isValid()
    } else {
        return 'Format non-valable'
    }

}

export const checkEmail = (val, allowEmpty = true) => {

    let reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
    let isValid = reg.test(val) || (allowEmpty && val === '')

    if (isValid) {
        return true
    } else {
        return 'Format non-valable'
    }

}

export const checkWebsite = (val, allowEmpty = true) => {

    let reg = /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi
    let isValid = reg.test(val) || (allowEmpty && val === '')

    if (isValid) {
        return true
    } else {
        return 'Format non-valable'
    }

}

export const formatPhoneNumber = val => {
    // this.entity.telephone = '+41255555555'
    console.log('formatPhoneNumber')
    console.log(val)
}

export const checkDate = val => {
    let mydate = date.extractDate(val, 'DD.MM.YYYY')
    console.log(val)
    console.log(mydate)
    console.log(date.isValid(mydate))
    return date.isValid(val) ? true : 'Format non-valable'
}

export const checkFilled = val => {
    return val ? true : 'Champ obligatoire'
}

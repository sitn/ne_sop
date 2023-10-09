/*
export default {
    foo: function () { alert("foo!") }
}
*/
import parsePhoneNumber from 'libphonenumber-js'

export const sleep = ms => new Promise(resolve => setTimeout(resolve, ms))

export const checkPhoneNumber = val => {

    let phoneNumber = parsePhoneNumber(val)
    if (phoneNumber) {
        val = '+41255555555'
        console.log('this.entity.phoneNumber')
        console.log(this.entity.phoneNumber)
        return phoneNumber.isPossible() & phoneNumber.isValid()
    } else {
        return 'Format non-valable'
    }

}

export const checkEmail = val => {

    let reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
    let isValid = reg.test(val)

    if (isValid) {
        return true
    } else {
        return 'Format non-valable'
    }

}

export const checkWebsite = val => {

    let reg = /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi
    let isValid = reg.test(val)

    if (isValid) {
        return true
    } else {
        return 'Format non-valable'
    }

}

export const checkFilled = val => {
    return val ? true : 'Choix non-valable'
}

/*
checkFilled(val) { 
            
},
*/
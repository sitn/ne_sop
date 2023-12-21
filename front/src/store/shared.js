import parsePhoneNumber from 'libphonenumber-js'
import { createEvent } from 'ics'
import { date } from 'quasar'

export const sleep = ms => new Promise(resolve => setTimeout(resolve, ms))

export const checkPhoneNumber = (val, allowEmpty = true) => {

    if (allowEmpty && (val === '' || val === null)) {
        return true
    }

    let phoneNumber = parsePhoneNumber(val)
    if (phoneNumber) {
        return phoneNumber.isPossible() & phoneNumber.isValid()
    } else {
        return 'Format non-valable'
    }

}

export const formatPhoneNumber = (val) => {
    // TO DO: implement auto-formatting of phone numbers 
}

export const checkEmail = (val, allowEmpty = true) => {

    let reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
    let isValid = reg.test(val) || (allowEmpty && (val === '' || val === null))

    if (isValid) {
        return true
    } else {
        return 'Format non-valable'
    }

}

export const checkWebsite = (val, allowEmpty = true) => {

    let reg = /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/gi
    let isValid = reg.test(val) || (allowEmpty && (val === '' || val === null))

    if (isValid) {
        return true
    } else {
        return 'Format non-valable'
    }

}

export const checkFile = (val) => {
    if (val) {
        return true
    } else {
        return 'Champ obligatoire'
    }
}

export const checkDate = (val) => {

    let reg = /^[0-9]{2}.[0-9]{2}.[0-9]{4}$/
    let isValidMask = reg.test(val)

    let dmy = val.split(".")
    let day = parseInt(dmy[0])
    let month = parseInt(dmy[1] - 1)
    let year = parseInt(dmy[2].padStart(4, 0))

    const eventDate = new Date()
    eventDate.setFullYear(year)
    eventDate.setMonth(month)
    eventDate.setDate(day)

    let isValidDate = parseInt(eventDate.getDate()) === parseInt(day) &&
        parseInt(eventDate.getMonth()) === parseInt(month) &&
        parseInt(eventDate.getFullYear()) === parseInt(year)

    return (isValidDate & isValidMask) ? true : 'Format non-valable'

}

export const checkTime = (val, allowEmpty = true) => {
    let reg = /^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/
    let isValid = reg.test(val) || (allowEmpty && (val === '' || val === null))
    if (isValid) {
        return true
    } else {
        return 'Format non-valable'
    }
}

export const checkFilled = (val) => {
    return val ? true : 'Champ obligatoire'
}

export const downloadICS = async (val) => {

    let eventDate = date.extractDate(val.date, 'DD.MM.YYYY')
    let dateArray = [eventDate.getFullYear(), eventDate.getMonth() + 1, eventDate.getDate()]

    let event = {
        start: dateArray,
        duration: { hours: 1, minutes: 0 },
        title: `Objet parlementaire ${val.itemNumber}`,
        description: '',
        location: '',
    }

    const filename = 'sop.ics'
    const file = await new Promise((resolve, reject) => {
        createEvent(event, (error, value) => {
            if (error) {
                reject(error)
            }

            resolve(new File([value], filename, { type: 'text/calendar' }))
        })
    })
    const url = URL.createObjectURL(file);

    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = filename;

    document.body.appendChild(anchor);
    anchor.click();
    document.body.removeChild(anchor);

    URL.revokeObjectURL(url);
}

export const formatBytes = (bytes, decimals = 2) => {
    if (!+bytes) return '0 Bytes'

    const k = 1024
    const dm = decimals < 0 ? 0 : decimals
    const sizes = ['Bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']

    const i = Math.floor(Math.log(bytes) / Math.log(k))

    return `${parseFloat((bytes / Math.pow(k, i)).toFixed(dm))} ${sizes[i]}`
}
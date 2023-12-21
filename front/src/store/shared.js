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

export const formatPhoneNumber = (val) => {
    // console.log('formatPhoneNumber')
    /// console.log(val)
}

export const checkFile = (val) => {
    //console.log('checkFile')
    //console.log(val)
    if (val) {
        return true
    } else {
        return 'Champ obligatoire'
    }
}

export const checkDate = (val) => {
    // let mydate = date.extractDate(val, 'DD.MM.YYYY')
    // console.log(`val: ${val}`)

    let reg = /^[0-9]{2}.[0-9]{2}.[0-9]{4}$/
    let isValidMask = reg.test(val)

    // console.log(`val: ${val} reg: ${isValidMask}`)

    let dmy = val.split(".")
    let day = parseInt(dmy[0])
    let month = parseInt(dmy[1] - 1)
    let year = parseInt(dmy[2].padStart(4, 0)) // 

    const eventDate = new Date()
    eventDate.setFullYear(year)
    eventDate.setMonth(month)
    eventDate.setDate(day)

    let isValidDate = parseInt(eventDate.getDate()) === parseInt(day) &&
        parseInt(eventDate.getMonth()) === parseInt(month) &&
        parseInt(eventDate.getFullYear()) === parseInt(year)

    /*
    const result = eventDate.toLocaleDateString("fr-CH", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
    })

    console.log(eventDate)
    console.log(result)
    */

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

    console.log('download ICS')
    console.log(val)

    // const extract = date => val.date.toISOString().split(/[^0-9]/).slice(0, -1)
    // let date = new Date(val.date)
    let eventDate = date.extractDate(val.date, 'DD.MM.YYYY')
    console.log(eventDate)

    let dateArray = [eventDate.getFullYear(), eventDate.getMonth() + 1, eventDate.getDate()]
    console.log(dateArray)

    let event = {
        start: dateArray, // Date.parse(val.date), //  [2018, 5, 30, 6, 30],
        duration: { hours: 1, minutes: 0 },
        title: `Objet parlementaire ${val.itemNumber}`,
        description: '',
        location: '',
        /*
        url: 'http://www.bolderboulder.com/',
        geo: { lat: 40.0095, lon: 105.2669 },
        categories: ['10k races', 'Memorial Day Weekend', 'Boulder CO'],
        status: 'CONFIRMED',
        busyStatus: 'BUSY',
        organizer: { name: 'Admin', email: 'Race@BolderBOULDER.com' },
        attendees: [
            { name: 'Adam Gibbons', email: 'adam@example.com', rsvp: true, partstat: 'ACCEPTED', role: 'REQ-PARTICIPANT' },
            { name: 'Brittany Seaton', email: 'brittany@example2.org', dir: 'https://linkedin.com/in/brittanyseaton', role: 'OPT-PARTICIPANT' }
        ]
        */
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

    // trying to assign the file URL to a window could cause cross-site
    // issues so this is a workaround using HTML5
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = filename;

    document.body.appendChild(anchor);
    anchor.click();
    document.body.removeChild(anchor);

    URL.revokeObjectURL(url);
}

/*
downloadICS(val) {

    console.log(val)

    let event = {
        start: [2018, 5, 30, 6, 30],
        duration: { hours: 6, minutes: 30 },
        title: 'Bolder Boulder',
        description: 'Annual 10-kilometer run in Boulder, Colorado',
        location: 'Folsom Field, University of Colorado (finish line)',
        url: 'http://www.bolderboulder.com/',
        geo: { lat: 40.0095, lon: 105.2669 },
        categories: ['10k races', 'Memorial Day Weekend', 'Boulder CO'],
        status: 'CONFIRMED',
        busyStatus: 'BUSY',
        organizer: { name: 'Admin', email: 'Race@BolderBOULDER.com' },

    }

    ics.createEvent(event, (error, value) => {
        if (error) {
            console.log(error)
            return
        }
        window.open("data:text/calendar;charset=utf8," + value);
        console.log(value)
    })

}

*/

// source: https://stackoverflow.com/questions/15900485/correct-way-to-convert-size-in-bytes-to-kb-mb-gb-in-javascript
export const formatBytes = (bytes, decimals = 2) => {
    if (!+bytes) return '0 Bytes'

    const k = 1024
    const dm = decimals < 0 ? 0 : decimals
    const sizes = ['Bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']

    const i = Math.floor(Math.log(bytes) / Math.log(k))

    return `${parseFloat((bytes / Math.pow(k, i)).toFixed(dm))} ${sizes[i]}`
}
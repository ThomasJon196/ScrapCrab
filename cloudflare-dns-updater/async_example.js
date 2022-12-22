const fs = require('fs')

const A = (filePath, callback) => {
    return fs.readFile(filePath, (error, result) => {
        if (error) {
            return callback(error, null)
        }
        return callback(null, result)
    })
}

const B = () => {
    // a callback function attached
    A('./file.txt', (error, result) => {
        if (result) {
            for (i = 0; i < result.length; i++) {
                console.log(i)
            }
        }
    })
    console.log('Result is not yet back from function A')
}

B()

// With Promise instead of Callback

const C = (filePath) => {
    const promise = new Promise((resolve, reject) => {
        return fs.readFile(filePath, (error, result) => {
            if (error) {
                reject(error)
            }
            resolve(result)
        })
    })
    return promise
}

const D = () => {
    C('./file.txt').then((data) => {
        if (data) {
            for (i = 0; i < data.length; i++) {
                console.log(i)
            }
        }
    }).catch((error) => {
        // handle errors
        console.log(error)
    })
    console.log('Result is not yet back from function A')
}

D()

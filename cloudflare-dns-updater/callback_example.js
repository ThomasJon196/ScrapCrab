const fun = (error, callback) => {
    console.log(`This is an example, with a ${error} passed an an argument`)
    callback()
}

const callback_fun = () => {
    console.log('Again, this is just a simple callback example')
}

fun('callback', callback_fun)
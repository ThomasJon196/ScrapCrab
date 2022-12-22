import fetch from 'node-fetch';

async function fetchMovies() {
    const response:Promise<any> = fetch('https://www.jonas-space.de', {method: 'GET'})

    var text = response.then(
        (value) => {
            console.log(value)
        }
    )

    return text
}

console.log(fetchMovies())



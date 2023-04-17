#!/usr/bin/node

const argv = process.argv;
const request = require('request');
url = `https://swapi-api.hbtn.io/api/films/${argv[2]}`

request(url, function(err, data, body) {
    if (err) throw err;
    else {
        console.log(JSON.parse(body).title);
    }
});
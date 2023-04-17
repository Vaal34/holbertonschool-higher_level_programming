#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films';
request(url, function (err, content, body) {
  let count = 0;
  if (err) {
    console.log(err);
  } else {
    const response = JSON.parse(body);
    for (const i in response.results) {
      const characters = response.results[i].characters;
      for (const j in characters) {
        if (characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});

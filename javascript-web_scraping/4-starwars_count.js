#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films';
request(url, function (err, content, body) {
  let count = 0;
  if (err) {
    console.log(err);
  } else {
    const response = JSON.parse(body);
    for (const dataResults of response.results) {
      for (const dataCharacter of dataResults.characters) {
        if (dataCharacter.includes('18')) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});

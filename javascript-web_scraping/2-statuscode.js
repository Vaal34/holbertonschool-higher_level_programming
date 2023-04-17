#!/usr/bin/node

const argv = process.argv;
const request = require('request');
const url = argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);  // Print the response status code if a response was received
  }
});

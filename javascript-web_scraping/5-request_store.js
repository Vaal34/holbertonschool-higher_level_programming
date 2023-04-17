#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');
const filename = argv[3];
const request = require('request');

request(argv[2], function (err, content, body) {
  if (err) {
    console.log(err);
  } else {
    const loremIpsum = body;
    fs.writeFile(filename, loremIpsum, err => {
      if (err) { console.log(err); }
    });
  }
});

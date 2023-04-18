#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = argv[2];
const dict = {};

request(url, function (err, content, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const maxLength = data.length - 1;
    if (maxLength === -1) {
      return dict;
    } else {
      const allId = data[maxLength];
      for (let i = 1; i <= allId.userId; i++) {
        let count = 0;
        for (const value of data) {
          if (value.userId === i) {
            if (value.completed === true) { count += 1; }
          }
        }
        if (count === 0) {
          // pass
        } else {
          dict[i] = count;
        }
      }
      console.log(dict);
    }
  }
});

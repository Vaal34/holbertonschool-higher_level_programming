#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;
const data = argv[3];

fs.writeFile(argv[2], data, err => {
  if (err) { console.log(err); }
});

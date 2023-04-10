#!/usr/bin/node

const argv = process.argv;
const numbertest = Number(argv[2]);

if (isNaN(numbertest)) { // check if number have Nan in value
  console.log('Not a Number');
} else {
  console.log('My number: ' + Number.parseInt(argv[2])); // Parse and take the first part if is float
}

#!/usr/bin/node

const argv = process.argv;

Number_test = Number(argv[2])

if (isNaN(Number_test)) {
  console.log('Not a Number')}
else if (Number_test % 1 !== 0) {
  console.log('My number: ' + Number.parseInt(argv[2]))
} else {
  console.log('My number: ' + argv[2])
}
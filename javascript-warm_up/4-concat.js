#!/usr/bin/node

const argv = process.argv; // create argv
const args = process.argv.length; // create argc

if (args === 3) {
  console.log(argv[2] + ' is ' + argv[3]);
} else if (args === 2) {
  console.log(argv[2] + ' is ' + argv[3]);
} else {
  console.log(argv[2] + ' is ' + argv[3]); // if arg dont exist but call is undefined no out of range
}

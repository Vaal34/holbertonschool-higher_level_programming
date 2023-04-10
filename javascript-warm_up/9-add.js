#!/usr/bin/node

const argv = process.argv;
const a = Number(argv[2]); // take arg and transform in Number for add
const b = Number(argv[3]);

function add (a, b) { // fonction that add 2 number
  console.log(a + b);
}

add(a, b); // fonction call

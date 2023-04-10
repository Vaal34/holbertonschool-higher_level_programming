#!/usr/bin/node

const argv = process.argv;
let num = Number(argv[2]);

function facto(num) {
  if (num <= 1) {
    return 1;
  }
  return num * facto(num - 1);
}

console.log(facto(num))
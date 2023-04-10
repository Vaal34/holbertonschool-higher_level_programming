#!/usr/bin/node

const argv = process.argv;
const num = Number(argv[2]);

function facto (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num <= 1) {
    return 1;
  } else if (num === undefined) {
    return 1;
  }
  return num * facto(num - 1);
}

console.log(facto(num));

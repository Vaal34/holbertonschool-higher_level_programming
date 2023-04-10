#!/usr/bin/node

const argv = process.argv;

const list = [];

if (argv.length <= 3) { // if 0 or just 1 args
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    list.push(Number(argv[i])); // append the list
  }
  list.sort((lower, upper) => upper - lower); // trier la liste dans l'ordre décroissant
  console.log(list[1]); // return 2nd value
}

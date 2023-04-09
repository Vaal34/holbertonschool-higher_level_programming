#!/usr/bin/node

const argc = process.argv.length; // Récupération du nombre d'arguments passés en ligne de commande

if (argc === 2) { // 2 car normalement prompt = node 2-arguments.js arg1 arg2
  console.log('No argument');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

#!/usr/bin/node

let i = 0; // varibale qui va augmenter a chaque fois que la fonction va être appelé

exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++; // incrémente la variable i chaque fois que la focntion est appelé
};

#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) { // searchElement est l'élement a trouver dans list
  let count = 0;
  for (let i = 0; i < list.length; i++) { // Boucle dans la list
    if (list[i] === searchElement) { // si un element de la liste est egal a searchElement
      count++; // Alors count augmente de 1
    }
  }
  return count; // return le nombre d'élement de la liste égale a searchElement
};

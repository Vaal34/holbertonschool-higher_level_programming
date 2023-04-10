#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  for (let i = list.length - 1; i >= 0; i--) { // Boucle dans la liste en partant de la fin
    newlist.push(list[i]); // Push dans une nouvelle list les element du debut a la fin
  }
  return newlist;
};

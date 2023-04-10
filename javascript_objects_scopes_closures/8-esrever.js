#!/usr/bin/node

exports.esrever = function (list) {
  new_list = [];
  for (let i = list.length - 1; i >= 0; i--) { // Boucle dans la liste en partant de la fin
    new_list.push(list[i]); // Push dans une nouvelle list les element du debut a la fin
  }
  return new_list;
};

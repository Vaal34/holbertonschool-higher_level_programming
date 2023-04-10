#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle { // crée un enfant de la classe Rectangle
  constructor (size) {
    super(size, size);
    // Appelle le constructeur de la classe parent en lui passant la taille du carré pour la longueur et la largeur
  }
}

module.exports = Square;

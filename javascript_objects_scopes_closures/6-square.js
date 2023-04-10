#!/usr/bin/node

const SquareParents = require('./5-square');

class Square extends SquareParents { // crée un enfant de la classe Rectangle
  constructor (size) {
    super(size, size);
    // Appelle le constructeur de la classe parent en lui passant la taille du carré pour la longueur et la largeur
  }

  charPrint (c) {
    if (c === undefined) { // si c est vide alors c vaut 'X'
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) { // boucle hauteur
      for (let j = 0; j < this.width; j++) { // boucle largeur
        process.stdout.write(c); // print X sans sauté de ligne
      }
      console.log();
    }
  }
}
module.exports = Square;

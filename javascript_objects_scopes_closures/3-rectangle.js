#!/usr/bin/node
class Rectangle {
  constructor (w, h) { // Les nouveaux rectangle predrons c'est arguments lors de leur creation
    if (h <= 0 || w <= 0 || h === undefined || w === undefined) { // si un param est < 0 ou n'st pas donné
      return;
    }
    this.height = h;
    this.width = w;
  }

  print () {
    for (let i = 0; i < this.height; i++) { // boucle hauteur
      for (let j = 0; j < this.width; j++) { // boucle largeur
        process.stdout.write('X'); // print X sans sauté de ligne
      }
      console.log();
    }
  }
}
module.exports = Rectangle; // permet de pouvoir utiliser la classe dans d'autres fichiers

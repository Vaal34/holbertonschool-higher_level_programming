#!/usr/bin/node
class Rectangle {
  constructor (w, h) { // Les nouveaux rectangle predrons c'est arguments lors de leur creation
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle; // permet de pouvoir utiliser la classe dans d'autres fichiers

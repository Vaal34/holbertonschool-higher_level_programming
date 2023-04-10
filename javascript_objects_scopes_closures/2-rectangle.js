#!/usr/bin/node
class Rectangle {
  constructor (w, h) { // Les nouveaux rectangle predrons c'est arguments lors de leur creation
    if (h <= 0 || w <= 0 || h === undefined || w === undefined) { // si un param est < 0 ou n'st pas donné
      return;
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle; // permet de pouvoir utiliser la classe dans d'autres fichiers

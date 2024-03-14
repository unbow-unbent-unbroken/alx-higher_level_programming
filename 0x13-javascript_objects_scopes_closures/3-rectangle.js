#!/usr/bin/node

/**
 * Defines a Rectangle
 */

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  printRectangle () {
    for (let i = 0; i < this.height; i++) {
      const row = '';
      for (let j = 0; j < this.width; j++) {
        const row = +'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;

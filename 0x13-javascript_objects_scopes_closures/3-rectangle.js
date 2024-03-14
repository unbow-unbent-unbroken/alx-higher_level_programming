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

  print () {
    for (let i = 0; i < this.height; i++) {
      const row = '';
      let j = 0;
      while (j < this.width) {
        row += 'X';
        j++;
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;

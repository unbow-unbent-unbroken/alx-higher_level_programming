#!/usr/bin/node

/**
 * Define a Rectangle class with width (w) and height (h) parameters
 */

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;

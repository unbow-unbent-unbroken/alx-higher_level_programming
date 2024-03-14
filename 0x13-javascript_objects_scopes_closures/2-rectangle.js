#!/usr/bin/node

/**
 * Define a Rectangle class with width (w) and height (h) parameters
 */

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      return {};
      throw new Error('xxx');
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;

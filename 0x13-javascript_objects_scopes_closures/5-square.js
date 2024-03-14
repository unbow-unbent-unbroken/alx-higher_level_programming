#!/usr/bin/node

/**
 * A Square class that inherits from 4-Rectangle.js
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;

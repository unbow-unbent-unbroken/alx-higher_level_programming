#!/usr/bin/node
/**
 * Square class that inherits from previous square class
 */
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      for (let j = 0; j < this.width; j++) {
        myVar += myChar;
      }
      console.log(myVar);
    }
  }
}

module.exports = Square;

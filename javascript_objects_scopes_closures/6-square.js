#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      let row = '';
      for (let j = 0; j < this.size; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;

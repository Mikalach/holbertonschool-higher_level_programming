#!/usr/bin/node

const Rectangle = require('./rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  toString () {
    return `[Square] ${this.width} x ${this.height}`;
  }
}

module.exports = Square;

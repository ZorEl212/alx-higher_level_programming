#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const th = this.width;
    this.width = this.height;
    this.height = th;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};

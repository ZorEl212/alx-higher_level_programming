#!/usr/bin/node
exports.logMe = function (item) {
  this.calls = (this.calls || 0) + 1;
  console.log(this.calls + ': ' + item);
};

#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    rev[j] = list[i];
  }
  return rev;
};

#!/usr/bin/node
/* add two numbers */

function add (a, b) {
  return a + b;
}
const res = add(Number(process.argv[2]), Number(process.argv[3]));
console.log(res);

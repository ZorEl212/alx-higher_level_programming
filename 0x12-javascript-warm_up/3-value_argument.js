#!/usr/bin/node
/* print values of passed arguments */
function getLength (args) {
  let size = 0;
  while (args[size] !== undefined) {
    size++;
  }
  return size;
}
const args = process.argv;
if (getLength(args) < 3) {
  console.log('No argument');
}
for (let i = 2; i < getLength(args); i++) {
  console.log(args[i]);
}

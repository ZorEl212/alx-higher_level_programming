#!/usr/bin/node
/* convert the first arg in to a  number if possible */
const arg = process.argv[2];
if (Number(arg)) {
  console.log('My number: ' + Number(arg));
} else {
  console.log('Not a number');
}

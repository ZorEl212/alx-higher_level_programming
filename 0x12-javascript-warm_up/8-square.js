#!/usr/bin/node
/* print a square with 'X' */

const sq = 'X';
const count = Number(process.argv[2]);
if (!Number(count)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < count; i++) {
    console.log(sq.repeat(count));
  }
}

#!/usr/bin/node
/* find second largest element of an array */

function secondLargest (arr) {
  let largest = arr[0];
  let second = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > largest) {
      second = largest;
      largest = arr[i];
    } else if (arr[i] > second && arr[i] !== largest) {
      second = arr[i];
    }
  }
  return second;
}

const array = process.argv.slice(2, process.argv.length);
const res = secondLargest(array.map(Number));
console.log(res);

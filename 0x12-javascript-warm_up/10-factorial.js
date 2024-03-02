#!/usr/bin/node
/* calculate a factorial of a number */

function factorial (n) {
  if (n <= 0) {
    return undefined;
  }
  if (n === 1 || !Number(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(Number(process.argv[2])));

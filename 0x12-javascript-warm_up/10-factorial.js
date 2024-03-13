#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }

  return n * factorial(n - 1);
}

const myArg = process.argv[2];

const num = parseInt(myArg);
console.log(factorial(num));

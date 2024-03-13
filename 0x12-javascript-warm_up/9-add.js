#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const firstNum = process.argv[2];
const secondNum = process.argv[3];

const num1 = parseInt(firstNum);
const num2 = parseInt(secondNum);

if (!isNaN(num1) & !isNaN(num2)) {
  console.log(add(num1, num2));
} else {
  console.log('NaN');
}

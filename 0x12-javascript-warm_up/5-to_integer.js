#!/usr/bin/node

const firstArg = process.argv[2];

const num = parseInt(firstArg);

if (!isNaN(num)) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}

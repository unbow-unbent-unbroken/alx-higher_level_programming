#!/usr/bin/node

const myArg = process.argv[2];

const x = parseInt(myArg);

if (!isNaN(x)) {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}

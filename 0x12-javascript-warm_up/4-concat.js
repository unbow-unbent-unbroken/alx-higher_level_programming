#!/usr/bin/node

const firstArg = process.argv[2];
const secondArg = process.argv[3];

if (firstArg === 1 & secondArg === 2) {
  console.log(firstArg, 'is', secondArg);
} else if (firstArg === 1 & secondArg === undefined) {
  console.log(firstArg, 'is', secondArg);
} else {
  console.log(firstArg, 'is', secondArg);
}

#!/usr/bin/node
console.log(parseInt(process.argv[2]) ? `My number: ${parseInt(process.argv[2])}` : 'Not a number');
/*
const firstArg = process.argv[2];

const num = parseInt(firstArg);

if (!isNaN(num))
{
    console.log("My number:", firstArg)
}
else
{
    console.log("Not a number")
}
*/
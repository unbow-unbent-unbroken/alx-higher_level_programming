#!/usr/bin/node

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
#!/usr/bin/node

const myArg = process.argv.slice(2);

if (myArg.length === 0 || myArg.length === 1)
{
    console.log(0);
}
else
{
    const num = myArg.map(myArg => parseInt(myArg)).sort((a, b) => b - a);
    console.log(num[1]);
}
#!/usr/bin/node

// prints My number: <first argument converted in integer>

const argFloat = parseFloat(process.argv[2]);
const argInt = Math.floor(argFloat);
if (Number.isInteger(argInt)) {
  console.log('My number: ' + argInt);
} else {
  console.log('Not a number');
}

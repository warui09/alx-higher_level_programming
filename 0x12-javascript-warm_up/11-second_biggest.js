#!/usr/bin/node

// prints the second biggest integer in the list of arguments

const args = process.argv.slice(2).sort().reverse();
if (args[1]) {
  console.log(args[1]);
}

console.log(0);

#!/usr/bin/node

// prints the second biggest integer in the list of arguments

const args = process.argv.slice(2).sort((a, b) => a - b).reverse();
if (process.argv.length <= 3) {
  console.log(0);
}

if (args[1]) {
  console.log(args[1]);
}

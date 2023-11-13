#!/usr/bin/node

// prints x times “C is fun”

const timesToPrint = process.argv[2];

if (!timesToPrint) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < timesToPrint; i++) {
  console.log('C is fun');
}

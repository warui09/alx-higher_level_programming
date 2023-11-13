#!/usr/bin/node

// prints a square

const size = Number(process.argv[2]);
if (!Number.isInteger(size)) {
  console.log('Missing size');
}

for (let i = 0; i < size; i++) {
  console.log('X'.repeat(size));
}

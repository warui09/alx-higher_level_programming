#!/usr/bin/node

// computes and prints a factorial

function factorial (num) {
  if (num === 0) {
    return 1;
  }

  return num * factorial(num - 1);
}

const number = Number(process.argv[2]);
if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}

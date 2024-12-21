#!/usr/bin/node

function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const args = process.argv.slice(2);

const number = parseInt(args[0], 10);
const result = factorial(isNaN(number) ? 1 : number);

console.log(result);

#!/usr/bin/node

// Function to add two integers
function add (a, b) {
  return a + b;
}

// Get the command-line arguments
const args = process.argv.slice(2);

if (args.length !== 2) {
  console.log('NaN');
  process.exit(1);
}

// Parse the arguments as integers
const a = parseInt(args[0], 10);
const b = parseInt(args[1], 10);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}

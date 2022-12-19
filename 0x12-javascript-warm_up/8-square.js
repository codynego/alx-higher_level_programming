#!/usr/bin/node

const args = process.argv.slice(2);
let square = Number(args[0]);

if (isNaN(Number(args[0]))) {
  console.log('Missing size');
} else {
  while (square > 0) {
    console.log('x'.repeat(Number(args[0])));
    square--;
  }
}

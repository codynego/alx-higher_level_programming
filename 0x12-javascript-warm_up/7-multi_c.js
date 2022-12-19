#!/usr/bin/node

const args = process.argv.slice(2);

if (isNaN(Number(args[0]))) {
  console.log('Missing number of occurrences');
} else {
  while (Number(args[0]) > 0) {
    console.log('C is fun');
    args[0]--;
  }
}

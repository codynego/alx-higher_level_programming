#!/usr/bin/node

const myargs = process.argv.slice(2);

if (isNaN(Number(myargs[0]))) {
  console.log('Not a number');
} else {
  console.log('My number:', myargs[0]);
}

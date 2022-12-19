#!/usr/bin/node

const myargs = process.argv.slice(2);

if (!myargs[0]) {
  console.log('No argument');
} else if (!myargs[1]) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

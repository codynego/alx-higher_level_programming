#!/usr/bin/node

const myargs = process.argv.slice(2);

if (!myargs[0]) {
  console.log('No argument');
} else {
  console.log(myargs[0]);
}

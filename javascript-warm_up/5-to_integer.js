#!/usr/bin/node
const arg = process.argv;

if (isNaN(Number(arg[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(arg[2]));
}

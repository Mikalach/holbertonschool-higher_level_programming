#!/usr/bin/node

if (isNaN(Number(argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(argv[2]));
}

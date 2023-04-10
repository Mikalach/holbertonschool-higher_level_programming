#!/usr/bin/node
const arg = process.argv;

if (arg === undefined) {
  console.log("No argument");
} else {
  console.log(arg);
}

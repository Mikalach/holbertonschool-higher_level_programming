#!/usr/bin/node


const args = process.argv.slice(2);
const numArgs = args.length;

if (numArgs < 2) {
  console.log(0);
} else {
  const nums = args.map(Number);
  const sortedNums = nums.sort((a, b) => b - a);
  console.log(sortedNums[1]);
}
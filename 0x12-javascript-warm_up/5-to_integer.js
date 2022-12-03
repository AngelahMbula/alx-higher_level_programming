#!/usr/bin/node
const args = process.argv;
let s1 = parseInt(args[2]);
if (isNaN(s1)) {
  s1 = 'Not a number';
} else {
  s1 = ('My number: ' + s1);
}
console.log(s1);

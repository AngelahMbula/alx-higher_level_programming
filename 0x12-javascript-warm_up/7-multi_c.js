#!/usr/bin/node
const x = parseInt(process.argv[2]);
let s1;
if (isNaN(x)) {
  s1 = 'Missing number of occurrences';
  console.log(s1);
} else {
  s1 = 'C is fun';
  for (let i = 0; i < x; i++) {
    console.log(s1);
  }
}

#!/usr/bin/node
// script that reads and prints the content of a file

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

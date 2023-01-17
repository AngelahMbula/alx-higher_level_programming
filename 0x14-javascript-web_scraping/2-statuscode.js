#!/usr/bin/node
// script that displays the statuscode of GET request

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});

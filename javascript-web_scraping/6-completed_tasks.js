#!/usr/bin/node

// Module
const request = require('request');
const process = require('process');

// Function
const dict = {};
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  JSON.parse(body).forEach(element => {
    if (element.completed === true) {
      if (dict[element.userId] === undefined) {
        dict[element.userId] = 1;
      } else { dict[element.userId] = dict[element.userId] += 1; }
    }
  });
  console.log(dict);
});

#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const apiUrl = argv[2]
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  for (const todo of todos) {
    if (todo.completed) {
      const userId = todo.userId;
      if (!completedTasks[userId]) {
        completedTasks[userId] = 1;
      } else {
        completedTasks[userId]++;
      }
    }
  }
    console.log(JSON.stringify(completedTasks));
  }
);

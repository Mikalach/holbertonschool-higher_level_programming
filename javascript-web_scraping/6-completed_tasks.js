#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

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

  const keys = Object.keys(completedTasks);
  const numKeys = keys.length;
  let count = 0;
  const keyValuePairs = [];

  for (const userId in completedTasks) {
    const pair = `'${userId}': ${completedTasks[userId]}`;
    keyValuePairs.push(pair);
    count++;

    if (count < numKeys) {
      keyValuePairs.push(',');
    }
  }

  console.log(`{ ${keyValuePairs.join(' ')} }`);
});

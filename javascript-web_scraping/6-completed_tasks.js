#!/usr/bin/node

const request = require('request');
const url = process.argv[2] || 'https://jsonplaceholder.typicode.com/todos';

request(url, (error, response, body) => {
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

  const formattedOutput = Object.keys(completedTasks).map(key => ` '${key}': ${completedTasks[key]}`).join(',\n');

  console.log(`{\n${formattedOutput}\n}`);
});

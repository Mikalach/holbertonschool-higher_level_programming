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

  let output = '';
  Object.entries(completedTasks).forEach(([key, value]) => {
    output += `'${key}': ${value}, `;
  });
  output = '{\n' + output.slice(0, -2) + '\n}';

  console.log(output);
});

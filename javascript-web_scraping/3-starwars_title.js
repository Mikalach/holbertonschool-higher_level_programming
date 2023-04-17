#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${movieId}`, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  
  const movie = JSON.parse(body);
  
  console.log(movie.title);
});

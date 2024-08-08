#!/usr/bin/node
const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL to fetch the movie data from the Star Wars API
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the HTTP GET request to the Star Wars API
request(url, async function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to get data. Status code:', response.statusCode);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;

    for (const characterUrl of characters) {
      await new Promise((resolve, reject) => {
        request(characterUrl, function (charError, charResponse, charBody) {
          if (charError) {
            console.error('Error:', charError);
            reject(charError);
          } else if (charResponse.statusCode !== 200) {
            console.error('Failed to get character data. Status code:', charResponse.statusCode);
            reject(new Error('Failed to get character data'));
          } else {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
            resolve();
          }
        });
      });
    }
  }
});

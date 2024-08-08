#!/usr/bin/node
const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL to fetch the movie data from the Star Wars API
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the HTTP GET request to the Star Wars API
request(url, function (error, response, body) {
  if (error) {
    // Log the error if the request fails
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    // Log the status code if the request is not successful
    console.error('Failed to get data. Status code:', response.statusCode);
  } else {
    // Parse the JSON response to get the movie data
    const data = JSON.parse(body);
    const characters = data.characters;

    // Iterate over the list of characters and make a request for each one
    characters.forEach(characterUrl => {
      request(characterUrl, function (charError, charResponse, charBody) {
        if (charError) {
          // Log the error if the request fails
          console.error('Error:', charError);
        } else if (charResponse.statusCode !== 200) {
          // Log the status code if the request is not successful
          console.error('Failed to get character data. Status code:', charResponse.statusCode);
        } else {
          // Parse the character data and print the character's name
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  }
});

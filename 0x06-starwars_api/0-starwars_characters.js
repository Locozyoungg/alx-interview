// Fetch and print character names in order
characters.forEach(characterUrl => {
    request(characterUrl, function (charError, charResponse, charBody) {
      if (charError) {
        console.error('Error:', charError);
      } else if (charResponse.statusCode !== 200) {
        console.error('Failed to get character data. Status code:', charResponse.statusCode);
      } else {
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      }
    });
  });
  
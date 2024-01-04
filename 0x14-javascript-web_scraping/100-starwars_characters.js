#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (err, res, body) => {
  if (err) {
    console.log(`Error: ${err}`);
    return;
  }
  const characterUrls = JSON.parse(body).characters;
  for (let i = 0; i < characterUrls.length; i++) {
    request(characterUrls[i], (err, res, body) => {
      if (err) {
        console.log(`Error: ${err}`);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  }
}
);

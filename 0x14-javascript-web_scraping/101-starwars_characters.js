#!/usr/bin/node
const request = require('request');
async function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, async (err, res, body) => {
  if (err) {
    console.log(`Error: ${err}`);
    return;
  }
  const characterUrls = JSON.parse(body).characters;
  for (let i = 0; i < characterUrls.length; i++) {
    const characterName = await getCharacterName(characterUrls[i]);
    console.log(characterName);
  }
});

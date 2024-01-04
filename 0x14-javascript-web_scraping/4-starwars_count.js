#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) { console.log(`error: ${err}`); }
  const searchParam = 'https://swapi-api.alx-tools.com/api/people/18/';
  const results = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < results.length; i++) {
    if (results[i].characters.includes(searchParam)) { count++; }
  }
  console.log(count);
}
);

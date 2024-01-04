#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) { console.log(`error: ${err}`); }
  fs.writeFile(process.argv[3], body, (err) => { if (err) console.log(err); });
}
);

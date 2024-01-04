#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(`Error: ${err}`);
    return;
  }
  body = JSON.parse(body);
  const users = {};
  for (let i = 0; i < body.length; i++) {
    if (body[i].completed === true) {
      if (body[i].userId in users) {
        users[body[i].userId] = (users[body[i].userId] ?? 0) + 1;
      } else {
        users[body[i].userId] = 1;
      }
    }
  }
  console.log(users);
});

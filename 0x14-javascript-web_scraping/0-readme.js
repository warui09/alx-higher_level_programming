#!/usr/bin/node
let fs = require('fs')
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
	if (!data)
		console.log(err)
	else
		console.log(data)
}
)

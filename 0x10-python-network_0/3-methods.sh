#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -s -i -X OPTIONS "$1" | grep "Allow:" | tr -d '\r' | awk '{print $2}'

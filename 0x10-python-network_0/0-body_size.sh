#!/bin/bash
# takes in a URL, sends a request and displays the size of the body of the response
echo $(curl -sI "$1" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n')

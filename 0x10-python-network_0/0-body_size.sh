#!/usr/bin/env bash

# Check if a URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL in a variable
url=$1

# Use curl to send a request and measure the size of the response body in bytes
size=$(curl -sI $url | grep -i content-length | awk '{print $2}' | tr -d '\r\n')

# Check if the content-length header is present in the response
if [ -z "$size" ]; then
    echo "Content-Length not found in the response headers."
    exit 1
fi

# Display the size of the response body in bytes
echo "${size}"

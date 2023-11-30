#!/usr/bin/env bash
#Get body of http request

url=$1

curl -sL "$url"

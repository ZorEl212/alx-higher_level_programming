#!/usr/bin/env bash
# Check if a URL is provided
curl -s "$1" | wc -c

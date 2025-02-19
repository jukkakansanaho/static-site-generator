#!/bin/bash

python3 src/main.py
PORT=8888
echo "Starting SSG server at port $PORT"
cd public && python3 -m http.server $PORT

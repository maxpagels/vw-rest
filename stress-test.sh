#!/bin/bash

# wrk -t2 -c10 -d20s -s body.lua http://127.0.0.1:5000/train
# ab -c 10 -n 5000 -s 90 -T application/json -p post.json http://127.0.0.1:5000/train

ab -c 10 -n 5000 -s 90 -T application/json http://127.0.0.1:3000/

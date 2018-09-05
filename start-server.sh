#!/bin/bash
#vw --daemon --progress 1 --port 26542 --foreground --quiet
uwsgi --http 127.0.0.1:5000 --master --processes 2 --disable-logging --module vw-server:app

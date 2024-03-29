#!/bin/sh

sudo mount /dev/sda1 /media/photos -o gid=pi,uid=pi
{ echo "const list_str = \`"; find /media/photos/ -type f; echo "\`"; cat slideshow/without_list.js; } > slideshow/with_list.js

python -m src.main_app.boot &
python -m src.api_server.apiserver

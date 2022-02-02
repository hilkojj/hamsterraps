#!/bin/sh

{ echo "const list_str = \`"; find /media/photos/ -type f; echo "\`"; cat slideshow/without_list.js; } > slideshow/with_list.js


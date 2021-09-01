#!/bin/sh

python -m src.main_app.boot &
python -m src.api_server.apiserver

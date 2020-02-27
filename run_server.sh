#!/usr/bin/env bash
uwsgi --http :5000 --manage-script-name --mount /=src.flask.api:flask_app --workers 4  > web_server_log.log 2>&1 &
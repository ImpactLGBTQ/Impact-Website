#!/bin/sh

# Run the server with uwsgi
exec uwsgi \
    --module ImpactWebsite.wsgi:application \
    --master \
    --max-requests 5000 \
    --socket 0.0.0.0:8000 \
    --mount /backend=ImpactWebsite.wsgi:application \
    --manage-script-name
    



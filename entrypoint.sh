#!/bin/sh

# Entry point for the main django deployment of the Imapact Website


if [ "$DATABASE" = "postgress" ]; then
    echo "Waiting for postgress..."
    
    # Wait for postgress to go up 
    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "DONE"
fi

python manage.py makemigrations 
python manage.py migrate

exec "$@"



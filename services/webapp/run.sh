#!/bin/bash

DATE=$(date)

echo ""
echo "==================================================="
echo "  Starting Server @ $DATE"
echo "==================================================="
echo ""

echo "Loading/sourcing env and settings..."
echo ""

# Load env
source /env.sh

# Stay quiet on Python warnings
export PYTHONWARNINGS=ignore

# To Python3 (unbuffered). P.s. "python -u" does not work..
export PYTHONUNBUFFERED=on

# Move to the code dir
cd /opt/webapp/code
    

if [[ "x$DEV_SERVER" == "xtrue" ]] ; then
    
    # Run the (development) server
    echo "Now starting Flask development server."
    export FLASK_ENV=development
    exec flask run --host=0.0.0.0

else

    # Collect static
    echo "Collecting static files..."
    python manage.py collectstatic

    # Run uWSGI
    echo "Now starting the uWSGI server."

    uwsgi --http :5000 \
          --master --pidfile=/tmp/autograding.pid \
          --workers 4 \
          --threads 2 \
          --socket=127.0.0.1:49152 \
          --static-map /static=/opt/webapp/code/static \
          --disable-logging \
          -w app:app

fi

#!/bin/bash

set -e

function migrate {
    if psql -h db -U postgres -lqt | cut -d \| -f 1 | grep -qw ${POSTGRES_GM_DB}; then
        echo "Database exists. Not creating"
    else
        psql -h db -U postgres -c "CREATE DATABASE ${POSTGRES_GM_DB}"
    fi
    python manage.py migrate
}

function mockdata {
    :
}

function assets {
    python manage.py collectstatic --noinput
}

function prepare {
    :
}

function supervisor {
    exec /usr/bin/supervisord -c /code/docker/Docker.server/supervisord-dev.conf
}

function development {
    migrate
    mockdata
    assets
    supervisor
}

function production {
    prepare
    migrate
    assets
    supervisor
}

function test {
    echo "Running tests with cache (use --cache-clear otherwise)..."
    cd /code/server/
    if [ $# -eq 0 ]; then
        DJANGO_SETTINGS_MODULE=django-react-docker-heroku.settings pytest --pylama tests/
    else
        DJANGO_SETTINGS_MODULE=django-react-docker-heroku.settings pytest --pylama "$@"
    fi
}

# Wait for the postgres container to actually be up and running
until psql -h db -U postgres -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

eval $@

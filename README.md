# django-react-docker-heroku

This is a starter project that has a Django backend, React frontend. It runs inside a Docker container. It is preconfigured to deploy on Heroku too (sans Docker).

The starter code consists of one GraphQL endpoint that is read on the frontend. The frontend is configured to be written in TypeScript. It was generated from CRA. The reader is encouraged to regenerate this in the future.

## Development

### Backend

```
./d build
./d start
```

Peek inside `./d` for more.

### Frontend
```
cd client
yarn
yarn run start
```

## Deployment

Assuming you've created a Heroku app and have your git configuration done.

```
heroku addons:create heroku-postgresql:hobby-dev
heroku buildpacks:add heroku/nodejs
heroku buildpacks:add heroku/python
heroku config:set SECRET_KEY='123'
git push heroku master
```

## Misc

If you want to clone this project and adjust the naming to be something other than 'django-react-docker-heroku', see below and substitute accordingly. For the DB_NAME, avoid hyphens else you'll need to do some escaping. Use underscores instead.

```
mv ./server/django-react-docker-heroku/ ./server/<NAME>
sed -i 's/django-react-docker-heroku-db/<NAME>-db/g' ./d
sed -i 's/django-react-docker-heroku-db/<NAME>-db/g' ./docker-compose.yml
sed -i 's/-d django-react-docker-heroku/<DB_NAME>/g' ./d
sed -i 's/EXISTS django_react_docker_heroku/EXISTS <DB_NAME>/g' ./d
sed -i 's/DATABASE django_react-docker_heroku/DATABASE <DB_NAME>/g' ./d
sed -i 's/django-react-docker-heroku/<DB_NAME>/g' ./.env.example
sed -i 's/django-react-docker-heroku/<NAME>/g' ./d
sed -i 's/django-react-docker-heroku/<NAME>/g' ./docker-compose.yml
sed -i 's/django-react-docker-heroku/<NAME>/g' ./Procfile
sed -i 's/django-react-docker-heroku/<NAME>/g' ./server/manage.py
sed -i 's/django-react-docker-heroku/<NAME>/g' ./server/<NAME>/settings.py
sed -i 's/django-react-docker-heroku/<NAME>/g' ./server/<NAME>/wsgi.py
sed -i 's/django-react-docker-heroku/<NAME>/g' ./docker/Docker.server/entrypoint.sh
sed -i 's/django-react-docker-heroku/<NAME>/g' ./docker/Docker.server/start_gunicorn.sh
```

PRs welcome from you script wizards to tighten this up. :)



FROM python:3.6.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    sudo && apt-get install -y \
    git \
    nginx \
    postgresql-client \
    python-psycopg2 \
    supervisor
RUN python3 -m pip install pipenv
RUN python3 -m pip install gunicorn

RUN mkdir /code
WORKDIR /code/server

RUN rm /etc/supervisor/supervisord.conf && \
    ln -s /code/docker/Docker.server/supervisord.conf /etc/supervisor/supervisord.conf && \
    rm /etc/nginx/nginx.conf && \
    ln -s /code/docker/Docker.server/nginx.conf /etc/nginx/nginx.conf && \
    mkdir -p /var/log/supervisor && \
    mkdir -p /var/log/gunicorn && \
    mkdir -p /code/logs/supervisord

ADD server /code
ADD .env /code
ADD docker /code

# Install python requirements
# TODO: don't pass --dev in production
ADD Pipfile Pipfile.lock /code/
RUN pipenv install --system --deploy --ignore-pipfile --dev

RUN groupadd -r app -g 1000 && \
    useradd -u 1000 -r -g app -d /code -s /bin/bash -c "Docker image user" app
RUN chown -R app:app /code && \
    chown -R app:app /var/run && \
    chown -R app:app /var/log/gunicorn

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "/code/docker/Docker.server/entrypoint.sh"]
CMD ["development"]

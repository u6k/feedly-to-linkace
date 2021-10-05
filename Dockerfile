FROM python:3.8-slim
LABEL maintainer="u6k.apps@gmail.com"

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get clean && \
    pip install pipenv

VOLUME /var/myapp
WORKDIR /var/myapp

COPY Pipfile Pipfile.lock ./

RUN pipenv install --ignore-pipfile --deploy --dev

CMD ["pipenv", "-h"]

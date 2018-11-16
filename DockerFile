FROM python:3.6
 
ENV PYTHONUNBUFFERED 1
 
# -- install Pipenv
RUN set -ex && pip install pipenv --upgrade
 
# -- creating app dir in container
RUN set -ex && mkdir /app
 
# -- add scripts
ADD /compose/*.sh /
RUN set -ex && chmod +x /*.sh

WORKDIR /app
 
# -- add pipfiles
ADD Pipfile /
ADD Pipfile.lock /
 
# -- install requirements
RUN set -ex && pipenv install --deploy --system
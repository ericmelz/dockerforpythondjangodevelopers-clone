FROM python:3.11

ENV PYTHONDONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv
RUN pipenv install --system

COPY . /code/



FROM python:3.10

RUN apt-get update && apt-get install -y \
    postgresql-client \
    less

ENV POETRY_HOME=/opt/poetry

RUN python3 -m venv $POETRY_HOME && \
    $POETRY_HOME/bin/pip install poetry==1.3.0

WORKDIR /eight-queens-puzzle

COPY . .

ENV VIRTUAL_ENV=/eight-queens-puzzle-env \
    PATH="/eight-queens-puzzle-env/bin:$POETRY_HOME/bin:$PATH"

RUN python3 -m venv $VIRTUAL_ENV && \
    poetry install

CMD "/bin/bash"

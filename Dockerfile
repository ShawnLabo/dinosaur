FROM python:3.10-slim-bullseye

LABEL org.opencontainers.image.source https://github.com/ShawnLabo/dinosaur

ENV POETRY_NO_INTERACTION=1
ENV PORT=8080

WORKDIR /app

RUN pip install poetry && poetry config virtualenvs.create false
COPY poetry.lock /app
COPY pyproject.toml /app
RUN poetry install --no-dev

COPY . /app

CMD ["sh", "-c", "hypercorn main:app --bind 0.0.0.0:$PORT"]
# dinosaur

## Run with Docker

```bash
docker run -p 8080:8080 -e FIREBASE_CONFIG=null ghcr.io/shawnlabo/dinosaur
```

## Development

Install dependencies:

```bash
poetry install
```

Set Firebase config to `FIREBASE_CONFIG` environment variable as a JSON.

```bash
export FIREBASE_CONFIG='{"apiKey":"...","authDomain":"...", ...}'
```

Run development server:

```bash
poetry run hypercorn main:app --reload
```
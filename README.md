# Open Pension Next Generation

## Setup

```
make init
```

## Running

```
make serve
```


## Docker Compose development

This environment resembles the production environment as closely as possible.

Run migrations:

```bash
docker-compose run --build --rm migrate
```

Start the web app:

```bash
docker-compose up -d --build ingress
```

Access at http://localhost:8000

Start a shell to run management commands:

```bash
docker-compose exec web bash
pytyhon manage.py
```

Start the Q Cluster:

```
docker-compose up -d --build qcluster
```

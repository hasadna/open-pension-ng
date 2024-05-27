This is the xls ingester project, it reads data from excele files in a given directory into an sql database.<br>
קבצי המקור הם דוחות "הנכס הבודד" רבעוניים מהגופים הפנסוניים
# The database structure is as follows:
importer_kupot - רשימת כל החברות והמסלולים <br>
importer_reports - linked to kupot - contains the report date and file name <br>
importer_asset_details - linked to reports - contains the details of assets and values. <br>

## Setup

```
make init
```
# build the database
```
make makemigrations
```

## Running

```
make serve
```

```
cd djang
../venv/bin/python3 manage.py  import_from_folder path= <path to directory where excel files are>
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

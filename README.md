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
## Open issues
...
Some of the xlsx files do not open, an exception is thrown.
The list of problematic files is in the database in importer_filesnotingested table.
The error is "Failed to read workbook
<class 'openpyxl.styles.named_styles._NamedCellStyle'>.name should be <class 'str'> but value is <class 'NoneType'>"
...
Another exception is trown with some files, seems to be caused by formula fields.
Error is: "תעודות התחייבות ממשלתיות-R25
+++Code 300. The number of operands is more than available in stack for function "+". Formula: C13+C15++C16+C17+C18+C19+C20+C21".
...
השלב הבא מבחינתי הוא פיתוח ממשק משתמש לניהול הנתונים - זה לא הממשק העקרי לשימוש של המידע אלא ממשק ניהולי לבדיקת המידע.

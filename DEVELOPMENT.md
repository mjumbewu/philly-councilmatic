# Setting up development environment for your city

## Set up virtual environment and install requirements

PostgreSQL, python3 (including dev packages), and pip will be need to be installed first.

```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

## Configure settings

Copy over settings example file.
```bash
cp councilmatic/settings_deployment.py.example councilmatic/settings_deployment.py
```

Edit `settings_deployment.py`:

  - rename the top-level directory `yourcity` to the name for your city's project (not used in display) 
  - change `CITY_APP` string in settings from `yourcity` to the name of your city's project
  - change `DEBUG` to `True` to get detailed error messages
  - set database username, password, and database name under `DATABASES`
  - create database (using `createdb`) and ensure user has access to it

## Run management commands

```bash
./manage.py migrate --no-initial-data
./manage.py createcachetable
```

This will create the database tables, but not add any data.

## Run server
```bash
./manage.py runserver
```

App should now be running [locally](http://127.0.0.1:8000/).

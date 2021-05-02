# Flowreader

## Installation
To set up this project locally, you can use [`docker-compose`](https://docs.docker.com/compose/):<br>
```sh
docker-compose up -d && docker-compose logs -f web
```
Configuration is done via the environment variables `DEBUG`, `SECRET_KEY`, `CACHE_URL`, `STATIC_ROOT` and `DATABASE_URL`, most of which have volatile defaults. The `docker-compose.yml` in this project will spin up services for a persistent database and cache, as well as setting the relevant env vars and loading the database with test data.

## Usage
Navigate to [`http://localhost:8000/admin/`](http://localhost:8000/admin/) and login with the relevant credentials. If you are using the `docker-compose.yml` provided in this project, the default admin credentials will be `admin:admin`, and the admin page will be populated with test data from `files/DTC5259515123502080915D0010.uff`.

To import files manually, use the manage.py command `manage.py import_flow_file` followed by one or more files.

## Running tests
To run tests, use `pytest`. `coverage` is also included in this project's dependencies:
```sh
export DJANGO_SETTINGS_MODULE=core.settings

poetry run pytest --cov=src src
poetry run coverage html

xdg-open htmlcov/index.html
```

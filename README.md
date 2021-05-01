# Flowreader

## Installation
To set up this project locally, you can use [`docker-compose`](https://docs.docker.com/compose/):<br>
```sh
docker-compose up -d && docker-compose logs -f web
```
Configuration is done via the environment variables `DEBUG`, `SECRET_KEY`, `CACHE_URL`, `STATIC_ROOT` and `DATABASE_URL`, most of which have volatile defaults. The `docker-compose.yml` in this project will spin up services for a persistent database and cache, as well as setting the relevant env vars and loading the database with test data.

## Usage
Navigate to [`http://localhost:8000/admin/`](http://localhost:8000/admin/) and login with the relevant credentials. If you are using the `docker-compose.yml` provided in this project, the default admin credentials will be `admin:admin`.

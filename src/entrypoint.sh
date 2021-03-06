#!/usr/bin/env bash

echo "Waiting for postgres... "

# Snippet I wrote to parse DATABASE_URL
# Removes the need for separate env vars
IFS=':/@' read DB _ _ USER PASSWORD HOST PORT _ <<< $DATABASE_URL

while ! nc -z $HOST $PORT
do
  # Wait for postgres port to open
  sleep 0.5
done
echo "Done."

python src/manage.py migrate --no-input
python src/manage.py collectstatic --no-input
python src/manage.py createsuperuser --no-input

# Import some test data for this development entrypoint
python src/manage.py import_flow_file files/DTC5259515123502080915D0010.uff

exec "$@"

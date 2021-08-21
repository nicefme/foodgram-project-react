# praktikum_new_diplom


sudo docker-compose exec backend python manage.py makemigrations main
sudo docker-compose exec backend python manage.py migrate --noinput


sudo docker-compose exec backend python manage.py collectstatic --no-input

docker-compose exec backend python manage.py createsuperuser

sudo docker-compose up --build -d 
docker-compose stop

sudo mount --make-shared /mnt/d
python manage.py loaddata correct.json

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=nicefme
POSTGRES_PASSWORD=6
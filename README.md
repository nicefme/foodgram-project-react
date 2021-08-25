# Foodgram

http://84.201.160.124/recipes/ - Foodgram  

email: admin@mail.com
pass: password22!

![Workflow status](https://github.com/nicefme/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)


### Описание

 Foodgram - Продуктовый помощник. На сайте пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд. Регистрация пользователя реализована на сайте.  

Стек технологий: Python 3 // Django // Django REST Framework // Djoser // Docker // Nginx // PostgreSQL

Проект собран в Docker и содержит четыре образа:

> 1. backend - образ бэка проекта
> 2. frontend - образ фронта проекта
> 3. postgres - образ базы данных PostgreSQL
> 4. nginx - образ backend сервера nginx


### Клонирование репозитория:

https://github.com/nicefme/foodgram-project-react.git


### Запуск проекта:
#### Подготовка репозитория, Secrets

- Сделайте [Fork проекта](https://github.com/nicefme/foodgram-project-react) себе в репозиторий GitHub;
- В файле docker-compose.yaml для сервисв web необходимо изменить имя пользователя DockerHub с ``` nicefme на ваше ```  
- Перейдите в настройки репозитория Settings, выберите на панели слева Secrets, нажмите New secret:  

> DOCKER_USERNAME - имя пользователя docker;  
> DOCKER_PASSWORD - пароль docker;  
> HOST - ip-адрес сервера;  
> USER - имя пользователя для сервера;  
> SSH_KEY - приватный ключ с компьютера, имеющего доступ к боевому серверу ``` cat ~/.ssh/id_rsa ```;  
> PASSPHRASE - пароль для сервера;  
> DB_ENGINE=django.db.backends.postgresql - указываем, что работаем с postgresql;  
> DB_NAME=postgres - имя базы данных;  
> POSTGRES_USER - логин для подключения к базе данных;  
> POSTGRES_PASSWORD - пароль для подключения к БД;  
> DB_HOST=db - название сервиса (контейнера);  
> DB_PORT=5432 - порт для подключения к БД;  
> TELEGRAM_TO - ID своего телеграм-аккаунта. Узнать свой ID можно у бота @userinfobot;
> TELEGRAM_TOKEN - токен вашего бота. Получить этот токен можно у бота @BotFather
 
#### Подготовка сервера

- Запустите сервер и зайдите на него ``` ssh username@ip_address ```;
- Установите обновления apt:  
``` sudo apt update ```;  
``` sudo apt upgrade -y ```;  
- Установите nginx ``` sudo apt install nginx -y ```;
- Остановите службу nginx ``` sudo systemctl stop nginx ``;
- Установите docker ``` sudo apt install docker.io ```;
- Установите docker-compose:  
Выполните команду, чтобы загрузить текущую стабильную версию Docker Compose:  
``` sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose ```;  
Примените к файлу права доступа:  
``` sudo chmod +x /usr/local/bin/docker-compose	```;  
Проверьте установку (должна вернуться версия docker-compose):  
``` docker-compose --version ```;
- Создайте на сервере два файла и скопируйте в них код из проекта на GitHub:  
> docker-compose.yaml из главной дериктории в home/<username>/docker-compose.yml  
``` sudo nano docker-compose.yaml ```  
> default.conf из папки nginx в home/<username>/nginx/default.conf  
``` mkdir nginx ```  
``` sudo nano nginx/default.conf ```  


### Настройка приложения на сервере:

- Для инициирования процесса автоматического развертывания приложения с помощью Actions workflow необходимо зайти в любой файл в репозитории проекта, внести изменение и закомитить изменения. За статусом работы можно проследить на вкладке Actions на GitHub.

- По окончании развертывания проекта, сделать миграции на сервере:  
``` sudo docker-compose exec backend python manage.py makemigrations APP_NAME ``` APP_NAMES: main, users  
``` sudo docker-compose exec backend python manage.py migrate --noinput ```  
``` sudo docker-compose exec backend python manage.py collectstatic --no-input ```  

#### Загрузка ингредиентов в БД:
``` sudo docker-compose exec backend python manage.py loaddata ingredients.json ```

#### Создание суперпользователя:
``` sudo docker-compose exec backend  python manage.py createsuperuser ```
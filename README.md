# Foodgram

ССЫЛКА -Foodgram

![Workflow status](https://github.com/nicefme/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg
)  ... Допишу после загрузки на сервер ...


### Описание

 Foodgram - Продуктовый помощник. На сайте пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.


### Регистрация пользователя

Регистрация проходит по форме регистрации на сайте


### Установка
Проект собран в Docker и содержит четыре образа:

> 1. backend - образ бэка проекта
> 2. frontend - образ фронта проекта
> 3. postgres - образ базы данных PostgreSQL
> 4. nginx - образ backend сервера nginx


### Клонирование репозитория:

https://github.com/nicefme/foodgram-project-react.git


#### Запуск проекта:
... Допишу после загрузки на сервер ...


### Настройка приложения на сервере:
``` sudo docker-compose exec backend python manage.py makemigrations APP_NAME ``` APP_NAMES: main, users
``` docker-compose exec backend python manage.py migrate --noinput ```
``` docker-compose exec backend python manage.py collectstatic --no-input ```

#### Загрузка ингредиентов в БД:
```docker-compose exec backend python manage.py loaddata ingredients.json ```

#### Создание суперпользователя:
``` docker-compose exec backend  python manage.py createsuperuser ```
# Quickstart

Создать новое окружение

    sudo apt-get install python-virtualenv
    virtualenv --no-site-packages venv
    source ~/venv/bin/activate
    pip install -r requirements.txt

Применить миграции

    python manage.py migrate

Запустить локальный сервер

    python manage.py runserver http://localhost:8000/

SwaggerUI: http://localhost:8000/

Админ. панель: http://localhost:8000/admin/

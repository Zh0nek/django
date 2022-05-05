## Backend development workflow

```json
virtualenv env
pip install -r requirements.txt
python manage.py makemigrations api
python manage.py makemigrations users
python manage.py migrate
python manage.py runserver
```


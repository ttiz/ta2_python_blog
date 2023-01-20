#改行コードはLFにすること

cd /code/Django

python manage.py makemigrations

# アプリ指定しないとマイグレーションファイルが自動生成されないため追加
python manage.py makemigrations tech
python manage.py makemigrations social

python manage.py migrate

uwsgi --socket :8001 --module mysite.wsgi
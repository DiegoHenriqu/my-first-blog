cd ..
myvenv\Scripts\activate
cd meublog
python manage.py makemigrations blog
python manage.py migrate
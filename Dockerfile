FROM python:3.9.16-bullseye

WORKDIR /usr/src/site

COPY ./req.txt /usr/src/req.txt

RUN pip install -r /usr/src/req.txt

COPY . /usr/src/site

EXPOSE  8000

CMD python manage.py makemigrations ; python manage.py migrate ; python manage.py runserver 0.0.0.0:8000 ;

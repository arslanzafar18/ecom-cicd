
From python:3

RUN pip install django==3.2.12
RUN pip install django-crispy-forms==1.14.0
RUN pip install Pillow==9.0.1
RUN pip install sqlparse==0.4.2


COPY . .
RUN python manage.py makemigrations

Run python manage.py migrate

CMD ["python","manage.py","runserver","0.0.0.0:8000"]


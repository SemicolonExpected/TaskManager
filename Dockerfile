FROM python:3.6.5-alpine

ENV FLASK_APP wsgi.py
ENV FLASK_CONFIG config.DevelopmentConfig
ENV FLASK_ENV development

WORKDIR /docker

COPY requirements.txt requirements.txt

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN python3 -m pip install -r psycopg2

COPY . /docker/

EXPOSE 5000

CMD ["gunicorn", "wsgi:app"]

#CMD ["flask", "run", "--host=0.0.0.0"]
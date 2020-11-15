FROM python:3.6.5-alpine

ENV FLASK_APP wsgi.py
ENV FLASK_CONFIG config.DevelopmentConfig
ENV FLASK_ENV development

WORKDIR /docker

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY task_manager/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /docker/

EXPOSE 5000

CMD ["gunicorn", "wsgi:app"]

#CMD ["flask", "run", "--host=0.0.0.0"]
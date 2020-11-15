FROM python:3.6.5-alpine

ENV FLASK_APP wsgi.py
ENV FLASK_CONFIG config.DevelopmentConfig
ENV FLASK_ENV development

WORKDIR /docker

COPY task_manager/requirements.txt requirements.txt

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . /docker/

EXPOSE 5000

CMD ["gunicorn", "wsgi:app"]

#CMD ["flask", "run", "--host=0.0.0.0"]
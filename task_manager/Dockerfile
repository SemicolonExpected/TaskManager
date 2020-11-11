FROM python:3.6.5-alpine 

RUN apk update  \
	apk add python-pip python-dev 

# We copy just the requirements.txt first to leverage Docker cache 
COPY ./requirements.txt /app/requirements.txt 

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt 

ENV FLASK_APP=task_manager \ 
	FLASK_ENV=development 

EXPOSE 5000 

CMD ["flask", "run", "--host=0.0.0.0"]
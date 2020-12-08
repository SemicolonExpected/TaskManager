LINTER = flake8
SRC_DIR = task_manager
REQ_DIR = requirements

FORCE:

prod: tests run_migrations document github

document: FORCE
	pydoc -w ./
	mv *.html docs

github: FORCE
	git add .  # this adds every file under the dir
	-git commit -a
	git push origin

tests: lint unit
	#-stestr run
	-echo "Sprinkle some flakey flakey goodness here"

unit: FORCE
	- coverage run --source=task_manager run_tests.py
	- coverage report --omit=/tests/*
	echo "Standardized unit testing"
	#flake8 here

lint: FORCE
	$(LINTER) . --ignore=W191,E265,E501,F841 --exclude=./migrations/
	#$(LINTER) . --exit-zero --ignore=W191,E265
	#lint all python ignoring tabs vs indents, and '# ' wrt block comments

dev_env: FORCE
	-pip3 install -r $(REQ_DIR)/requirements-dev.txt
	-sudo apt-get update
	-sudo apt install python-dev-is-python3	sqlite3 docker.io
	echo "Installing docker"
	-sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
	-curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	#Use the following command to set up the stable repository. To add the nightly or test repository, add the word nightly or test (or both) after the word stable in the commands below. Learn about nightly and test channels.
	-sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable test"
	-sudo apt-get update
	-sudo apt-get install docker-ce docker-ce-cli containerd.io
	echo "Test Docker"
	-sudo docker run hello-world

run_migrations:
	flask db migrate
	flask db upgrade

run:
	sudo docker build -t task-manager:latest .
	sudo docker run -d -p 5000:5000 task-manager
	
run_dev:
	FLASK_APP=wsgi FLASK_ENV=development flask run

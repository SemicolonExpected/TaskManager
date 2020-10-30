LINTER = flake8
SRC_DIR = task_manager
REQ_DIR = requirements

FORCE:

prod: tests document github

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
	- coverage run run_tests.py
	- coverage report
	echo "Standardized unit testing"
	#flake8 here

lint: FORCE
	$(LINTER) . --ignore=W191,E265 --exclude=./migrations/
	#$(LINTER) . --exit-zero --ignore=W191,E265
	#lint all python ignoring tabs vs indents, and '# ' wrt block comments

dev_env: FORCE
	-pip3 install -r $(REQ_DIR)/requirements-dev.txt

run_dev:
	FLASK_APP=$(SRC_DIR) FLASK_ENV=development flask run

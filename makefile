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
	echo "Sprinkle some flakey flakey goodness here"

unit: FORCE
	echo "Standardized unit testing"
	#flake8 here

lint: FORCE
	$(LINTER) . --exit-zero --ignore=W191,E265
	#$(LINTER) $(SRC_DIR)/*py --exit-zero --ignore=W191,E265 # ,E117,E265,E231,E309,E251
	#lint all python ignoring tabs vs indents, and '# ' wrt block comments

dev_env: FORCE
	-pip3 install -r $(REQ_DIR)/requirements-dev.txt
	-sudo apt install python-dev-is-python3

run_dev:
	FLASK_APP=$(SRC_DIR) FLASK_ENV=development flask run

run_dev:
	FLASK_APP=$(SRC_DIR) FLASK_ENV=development flask run
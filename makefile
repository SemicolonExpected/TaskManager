LINTER = flake8
SRC_DIR = task_manager
REQ_DIR = requirements

FORCE:

prod: tests github

github: FORCE
	git add .  # this adds every file under the dir
	-git commit -a
	git push origin master

tests: lint unit 
	echo "Sprinkle some flakey flakey goodness here"

unit: FORCE
	echo "Standardized unit testing"
	#flake8 here

lint: FORCE
	$(LINTER) $(SRC_DIR)/*py --ignore=W191,E117,E265,E231,E309,E251
	#lint all python ignoring tabs vs indents, and '# ' wrt block comments
	#also ignoring the "overindented" E231 and 2 lines between every function E309.
	#also ignoring E251 unexpected spaces around keyword / parameter equals, I like that whitespace

dev_env: FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt 

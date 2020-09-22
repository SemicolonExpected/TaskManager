LINTER = flake8
SRC_DIR = source
REQ_DIR = requirements

FORCE:

prod: tests github

github: FORCE
	-git commit -a
	git push origin master

tests: lint unit 
	echo "Sprinkle some flakey flakey goodness here"

unit: FORCE
	echo "Standardized unit testing"
	#flake8 here

lint: FORCE
	$(LINTER) $(SRC_DIR)/*py #lint all python

dev_env: FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt
tests: test-deps
	nosetests -s

test-deps:
	pip3 install -r requirements.txt

.PHONY: test upload clean bootstrap setup

test:
	NLTK_DATA=_nltk_data _virtualenv/bin/nosetests tests
	
upload: setup assert-converted-readme
	python setup.py sdist upload
	make clean
	
register: setup
	python setup.py register

README: README.md
	pandoc --from=markdown --to=rst README.md > README || cp README.md README

assert-converted-readme:
	test "`cat README`" != "`cat README.md`"

clean:
	rm -f README
	rm -f MANIFEST
	rm -rf dist
	
bootstrap: _virtualenv setup
	_virtualenv/bin/pip install -e .
ifneq ($(wildcard test-requirements.txt),) 
	_virtualenv/bin/pip install -r test-requirements.txt
endif
	make clean
	make _nltk_data
	
_nltk_data:
	_virtualenv/bin/python -m nltk.downloader -d _nltk_data all

setup: README

_virtualenv: 
	virtualenv _virtualenv
	_virtualenv/bin/pip install 'distribute>=0.6.45'

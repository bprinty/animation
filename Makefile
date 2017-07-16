#
# animation Makefile
#
# @author <bprinty@gmail.com>
# ------------------------------------------------------


# config
# ------
VERSION    = `python -c 'import animation; print animation.__version__'`


# targets
# -------
.PHONY: docs clean tag

help:
	@echo "clean    - remove all build, test, coverage and Python artifacts"
	@echo "lint     - check style with flake8"
	@echo "test     - run tests quickly with the default Python"
	@echo "docs     - generate Sphinx HTML documentation, including API docs"
	@echo "release  - package and upload a release"
	@echo "build    - package module"
	@echo "install  - install the package to the active Python's site-packages"

clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

lint:
	flake8 animation tests

test:
	nosetests -c setup.cfg tests

tag:
	VER=$(VERSION) && if [ `git tag | grep "$$VER" | wc -l` -ne 0 ]; then git tag -d $$VER; fi
	VER=$(VERSION) && git tag $$VER -m "animation, release $$VER"

docs:
	cd docs && make html

build: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

release: build tag
	VER=$(VERSION) && git push origin :$$VER || echo 'Remote tag available'
	VER=$(VERSION) && git push origin $$VER
	twine upload --skip-existing dist/*

install: clean
	python setup.py install

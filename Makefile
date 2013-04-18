PYTHON=python

all: build

build:
	$(PYTHON) setup.py sdist
clean:
	$(PYTHON) setup.py clean --all
	find . -name '*.py[co]' -exec rm -f "{}" ';'
	rm -rf build dist djangocas.egg-info temp

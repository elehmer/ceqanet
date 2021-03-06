pkgname = ceqanet
prefix ?= /var/www
rootdir = $(prefix)/ceqanet.ca.gov
pkgroot = $(rootdir)/$(pkgname)

staticdir = $(pkgname)/static
templatesdir = $(pkgname)/templates
# Support virtualenvwrapper installations and ../env
venvdir ?= $(or $(wildcard ../env), $(HOME)/.virtualenvs/$(pkgname))

# Environment variables for all subshells.
# Always use a virtualenv.
export VIRTUAL_ENV=$(venvdir)
export PATH := $(venvdir)/bin:$(PATH)

INSTALL ?= install
# Find path to compileall.py to create python bytecode
PYC ?= python $(shell python -c 'import compileall; print(compileall.__file__)')
pyver ?= $(shell python -c \
	"import sys; print('python{}.{}'.format(sys.version_info.major, sys.version_info.minor))")

.PHONY : all build venv

all: build

# Create virtualenv for managing Python dependencies
venv: $(venvdir)/bin/activate
$(venvdir)/bin/activate: requirements.txt
	test -d $(venvdir) || virtualenv $(venvdir)
	# Django needs to be installed before other django dependent apps	
	. $@; pip install "$$(grep '^django==' $^)"
	# Install other dependencies in requirements.txt
	. $@; pip install -r $^
	touch $@

build: venv $(addsuffix c, $(pysrc))

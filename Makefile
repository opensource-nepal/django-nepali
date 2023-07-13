##
# django-nepali
#
# @file
# @version 0.2

install:
	pipenv install

install-dev:
	pipenv install --dev

test:
	pipenv run pytest

coverage:
	pipenv run pytest --cov=django_nepali/ --no-cov-on-fail

coverage-html:
	pipenv run pytest --cov=django_nepali/ --cov-report=html --no-cov-on-fail

.PHONY: install install-dev test coverage coverage-html
# end

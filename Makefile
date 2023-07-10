##
# django-nepali
#
# @file
# @version 0.1

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

open-coverage-html-mac: coverage-html
	open htmlcov/index.html

open-coverage-html-linux: coverage-html
	xdg-open htmlcov/index.html

# end

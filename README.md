# django-nepali

[![CI status](https://github.com/opensource-nepal/django-nepali/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/opensource-nepal/django-nepali/actions)
[![Downloads](https://img.shields.io/pypi/dm/nepali.svg?maxAge=180)](https://pypi.org/project/django-nepali/)
[![codecov](https://codecov.io/gh/opensource-nepal/django-nepali/branch/main/graph/badge.svg?token=PTUHYWCJ4I)](https://codecov.io/gh/opensource-nepal/django-nepali)

A django package on top of [nepali](https://github.com/opensource-nepal/py-nepali/) python package which supports nepali date time, time conversion, etc on django projects.

## Requirements

    django
    nepali >= 1.0.0

## Installation

    pip install django-nepali

On `settings.py`, add `'django_nepali'` to your `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    ...
    'django_nepali',
    ...
]
```

## Django Templates

### nepalidatetime

In your Template

```python
{% load nepalidatetime %}
```

#### nepalinow

`nepalinow` renders the current Nepali date and time in 'en-US' locale (English).

```python
{% nepalinow %}
```

```python
{% nepalinow '%Y-%m-%d' %}
```

#### nepalinow_ne

`nepalinow_ne` renders the current Nepali date and time in 'ne' locale (Nepali).

```python
{% nepalinow_ne %}
```

#### nepalidate

`nepalidate` renders the datetime object into nepali datetime format in 'en-US' locale (English).

```python
{{ datetime_obj|nepalidate:"%Y-%m-%d" }}
```

#### nepalidate_ne

`nepalidate_ne` renders the datetime object into nepali datetime format in 'ne' locale (Nepali).

```python
{{ datetime_obj|nepalidate_ne:"%Y-%m-%d" }}
```

#### nepalihumanize

`nepalihumanize` renders the datetime object to a human readable form for 'ne' locale (Nepali)

```python
{{ datetime_obj|nepalihumanize }}
```

### nepalinumber

In your Template

```python
{% load nepalinumber %}
```

`nepalinumber` renders the english number into nepali format (devanagari)

```python
{{ forloop.counter|nepalinumber }}

{{ 150|nepalinumber }}
```

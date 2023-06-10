# django-nepali

[![CI status](https://github.com/opensource-nepal/django-nepali/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/opensource-nepal/django-nepali/actions)
[![Downloads](https://img.shields.io/pypi/dm/django-nepali.svg?maxAge=180)](https://pypi.org/project/django-nepali/)
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

##### For default date format

```python
{% nepalinow %}
```

##### For custom date format

```python
{% nepalinow '%Y-%m-%d' %}
```

#### nepalinow_ne

`nepalinow_ne` renders the current Nepali date and time in 'ne' locale (Nepali).

##### For default date format

```python
{% nepalinow_ne %}
```

##### For custom date format

``` python
{% nepalinow_ne '%Y-%m-%d' %}
```

#### nepalidate

`nepalidate` renders the datetime object into nepali datetime format in 'en-US' locale (English).

##### For default date format

``` python
{{ datetime_obj|nepalidate }}
```

##### For custom date format

```python
{{ datetime_obj|nepalidate:"%Y-%m-%d" }}
```

#### nepalidate_ne

`nepalidate_ne` renders the datetime object into nepali datetime format in 'ne' locale (Nepali).

##### For default date format

```python
{{ datetime_obj|nepalidate_ne }}
```

##### For custom date format

```python
{{ datetime_obj|nepalidate_ne:"%Y-%m-%d" }}
```

#### nepalihumanize

`nepalihumanize` renders the datetime object to a human readable form for 'ne' locale (Nepali)

```python
{{ datetime_obj|nepalihumanize }}
```

##### Humanize threshold

You can provide a threshold input, measured in seconds, to the `nepalihumanize` filter. If the time difference between the current time and the `datetime_obj` is greater than the specified threshold, then instead of relative time as provided by the humanize function, the `datetime_obj` will be displayed in the specified format (if provided), or else in the default format.

```python
{{ datetime_obj|nepalihumanize:1000 }}
```

### nepalinumber

In your Template

```python
{% load nepalinumber %}
```

`nepalinumber` renders the english number into nepali format (devanagari)

```python
{{ forloop.counter|nepalinumber }}
```

```python
{{ 150|nepalinumber }}
```

##### nepali_comma

Renders the given value with commas added in Nepali style without converting the number.

```python
{{ number|nepali_comma }}
```

This would convert a number such as `100000` into `1,00,000`.

##### english_comma

Renders the given value with commas added in English style without converting the number.

```python
{{ number|english_comma }}
```

This would convert a number such as `100000` into `100,000`.

##### nepalinumber with comma

Converts the number into nepali number and renders it. Basically same as `{{ number|nepalinumber|nepali_comma }}`

```python
{{ number|nepalinumber_with_comma }}
```

This would convert a number such as `1000` into `१,०००`.

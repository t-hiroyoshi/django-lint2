# django-lint2 ✅

Lint2 is a linter work with Django.

## Requirements

Python 3+
Django
Flake8

## Installation

Install using pip!

```sh
pip install flake8 django-lint2
```

Add 'lint2' to your INSTALLED_APPS setting.

```py
INSTALLED_APPS = (
  ...,
  'lint2',
)
```

## Settings

Add options of flake8 to your settings.

See flake8 documents (http://flake8.pycqa.org/en/latest/user/configuration.html).

```py
LINT2 = {
  'max_line_length': 120,
}
```

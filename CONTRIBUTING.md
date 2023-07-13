# How to Contribute

## Install Development Dependencies (Using Pipenv)

All the dependencies are managed by Pipenv. Please install Pipenv on your system first by following the instructions at [https://pipenv.pypa.io/en/latest/installation/](https://pipenv.pypa.io/en/latest/installation/).

Once Pipenv is installed, you can install the development dependencies by running the following command:

```bash
make install-dev
```

This will ensure that all the necessary packages and dependencies are installed in your development environment.

## Codestyle

A [.editorconfig](./editorconfig) is available to maintain the coding style. Besides, your code will automatically get formatted if you have installed the pre-commit hook.

## Unit tests

Run the unittest using the below command:

```bash
make test
```

### Coverage Report

To run the coverage report:

```bash
make coverage
```

To generate HTML coverage report

```bash
make coverage-html
```

## Before submitting

Before submitting your code please do the following steps:

1. Add any changes you want
1. Add tests for the new changes
1. Update the `CHANGELOG.md` file if necessary
1. Edit documentation if you have changed something significant

## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.

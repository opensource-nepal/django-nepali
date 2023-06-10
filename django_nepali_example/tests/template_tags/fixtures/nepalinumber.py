"""
Contains fixtures for tests related to
nepalinumber module
"""

from django.template import Template


class NepaliNumberFixture:
    template = Template("{% load nepalinumber %}{{ payload|nepalinumber }}")
    return_value = "१"


class NepaliNumberWithCommaFixture:
    template = Template("{% load nepalinumber %}{{ payload|nepalinumber_with_comma }}")
    return_value = "१,०००"


class NepaliCommaFixture:
    template = Template("{% load nepalinumber %}{{ payload|nepali_comma }}")
    return_value = "1,00,000"


class EnglishCommaFixture:
    template = Template("{% load nepalinumber %}{{ payload|english_comma }}")
    return_value = "100,000"

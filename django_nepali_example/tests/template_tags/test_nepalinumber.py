"""
Contains tests for nepalinumber.py module
"""

from unittest import mock

import pytest
from django.template.context import Context

from .fixtures.nepalinumber import (
    EnglishCommaFixture,
    NepaliCommaFixture,
    NepaliNumberFixture,
    NepaliNumberWithCommaFixture,
)

MODULE_TO_TEST = "django_nepali.templatetags.nepalinumber"


class TestNepaliNumber:
    """
    Tests for nepalinumber template tag
    """

    @pytest.fixture(scope="class")
    def fixture_data(self):
        yield NepaliNumberFixture()

    @mock.patch(f"{MODULE_TO_TEST}.english_to_nepali")
    def test_nepalinumber_returns_nepali_value(
        self, mock_english_to_nepali: mock.MagicMock, fixture_data: NepaliNumberFixture
    ):
        mock_english_to_nepali.return_value = fixture_data.return_value

        rendered = fixture_data.template.render(Context({"payload": 1}))

        mock_english_to_nepali.assert_called_once_with(1)
        assert rendered == fixture_data.return_value


class TestNepaliNumberWithComma:
    """
    Tests for nepalinumber_with_comma template tag
    """

    @pytest.fixture(scope="class")
    def fixture_data(self):
        yield NepaliNumberWithCommaFixture()

    @mock.patch(f"{MODULE_TO_TEST}.convert_and_add_comma")
    def test_nepalinumber_returns_nepali_value_with_comma(
        self,
        mock_convert_and_add_comma: mock.MagicMock,
        fixture_data: NepaliNumberWithCommaFixture,
    ):
        mock_convert_and_add_comma.return_value = fixture_data.return_value

        rendered = fixture_data.template.render(Context({"payload": 1000}))

        mock_convert_and_add_comma.assert_called_once_with(1000)
        assert rendered == fixture_data.return_value


class TestNepaliComma:
    """
    Tests for nepali_comma template tag
    """

    @pytest.fixture(scope="class")
    def fixture_data(self):
        yield NepaliCommaFixture()

    @mock.patch(f"{MODULE_TO_TEST}.add_comma")
    def test_nepalinumber_returns_number_with_nepali_style_comma(
        self,
        mock_add_comma: mock.MagicMock,
        fixture_data: NepaliCommaFixture,
    ):
        mock_add_comma.return_value = fixture_data.return_value

        rendered = fixture_data.template.render(Context({"payload": 100000}))

        mock_add_comma.assert_called_once_with(100000)
        assert rendered == fixture_data.return_value


class TestEnglishComma:
    """
    Tests for english_comma template tag
    """

    @pytest.fixture(scope="class")
    def fixture_data(self):
        yield EnglishCommaFixture()

    @mock.patch(f"{MODULE_TO_TEST}.add_comma_english")
    def test_nepalinumber_returns_number_with_english_style_comma(
        self,
        mock_add_comma_english: mock.MagicMock,
        fixture_data: EnglishCommaFixture,
    ):
        mock_add_comma_english.return_value = fixture_data.return_value

        rendered = fixture_data.template.render(Context({"payload": 100000}))

        mock_add_comma_english.assert_called_once_with(100000)
        assert rendered == fixture_data.return_value

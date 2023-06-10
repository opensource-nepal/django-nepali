"""
Contains tests for nepalidatetime.py module
"""

from unittest import mock

import pytest
from django.template import Context

from .fixtures.nepalidatetime import (
    NepaliDateEnFixture,
    NepaliDateFixture,
    NepaliDateNeFixture,
    NepaliHumanizeFixture,
    NepaliNowEnFixture,
    NepaliNowFixture,
    NepaliNowNeFixture,
)

MODULE_TO_TEST = "django_nepali.templatetags.nepalidatetime"


class TestNepaliDate:
    """
    Tests for nepalidate template tag
    """

    @pytest.fixture(scope="class")
    def fixture_data(self):
        yield NepaliDateFixture()

    def test_nepalidate_returns_empty_string_when_invalid_object_is_passed(
        self, fixture_data: NepaliDateFixture
    ):
        rendered = fixture_data.template.render(
            Context({"payload": fixture_data.invalid_payload})
        )

        assert rendered == ""

    def test_nepalidate_renders_date_in_default_format(
        self, fixture_data: NepaliDateFixture
    ):
        rendered = fixture_data.template.render(
            Context({"payload": fixture_data.date_payload})
        )

        assert rendered == fixture_data.payload_expected_template

    def test_nepalidate_renders_datetime_in_default_format(
        self, fixture_data: NepaliDateFixture
    ):
        rendered = fixture_data.template.render(
            Context({"payload": fixture_data.datetime_payload})
        )

        assert rendered == fixture_data.payload_expected_template

    def test_nepalidate_renders_nepalidate_in_default_format(
        self, fixture_data: NepaliDateFixture
    ):
        rendered = fixture_data.template.render(
            Context({"payload": fixture_data.nepalidate_payload})
        )

        assert rendered == fixture_data.payload_expected_template

    def test_nepalidate_renders_nepalidatetime_in_default_format(
        self, fixture_data: NepaliDateFixture
    ):
        rendered = fixture_data.template.render(
            Context({"payload": fixture_data.nepalidatetime_payload})
        )

        assert rendered == fixture_data.payload_expected_template


class TestNepaliDateEn:
    """
    Tests for nepalidate_en template tag
    """

    @pytest.fixture(scope="class")
    def fixture_data(self):
        yield NepaliDateEnFixture()

    def test_nepalidate_en_renders_date_in_default_format(
        self, fixture_data: NepaliDateEnFixture
    ):
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.date_payload})
        )

        assert rendered == fixture_data.payload_expected_template

    def test_nepalidate_en_renders_date_in_custom_format(
        self, fixture_data: NepaliDateEnFixture
    ):
        rendered = fixture_data.custom_template.render(
            Context({"payload": fixture_data.date_payload})
        )

        assert rendered == fixture_data.payload_expected_custom_template

    def test_nepalidate_en_renders_datetime_in_default_format(
        self, fixture_data: NepaliDateEnFixture
    ):
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.datetime_payload})
        )

        assert rendered == fixture_data.payload_expected_template

    def test_nepalidate_en_renders_datetime_in_custom_format(
        self, fixture_data: NepaliDateEnFixture
    ):
        rendered = fixture_data.custom_template.render(
            Context({"payload": fixture_data.datetime_payload})
        )

        assert rendered == fixture_data.payload_expected_custom_template

    def test_nepalidate_en_renders_nepalidate_in_default_format(
        self, fixture_data: NepaliDateEnFixture
    ):
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.nepalidate_payload})
        )

        assert rendered == fixture_data.payload_expected_template

    def test_nepalidate_en_renders_nepalidate_in_custom_format(
        self, fixture_data: NepaliDateEnFixture
    ):
        rendered = fixture_data.custom_template.render(
            Context({"payload": fixture_data.nepalidate_payload})
        )

        assert rendered == fixture_data.payload_expected_custom_template

    def test_nepalidate_en_renders_nepalidatetime_in_default_format(
        self, fixture_data: NepaliDateEnFixture
    ):
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.nepalidatetime_payload})
        )

        assert rendered == fixture_data.payload_expected_template

    def test_nepalidate_en_renders_nepalidatetime_in_custom_format(
        self, fixture_data: NepaliDateEnFixture
    ):
        rendered = fixture_data.custom_template.render(
            Context({"payload": fixture_data.nepalidatetime_payload})
        )

        assert rendered == fixture_data.payload_expected_custom_template

    def test_nepalidate_en_returns_empty_string_when_invalid_object_is_passed(
        self, fixture_data: NepaliDateEnFixture
    ):
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.invalid_payload})
        )

        assert rendered == ""


class TestNepaliDateNe:
    """
    Tests for nepalidate_ne template tag
    """

    @pytest.fixture(scope="class")
    def fixture_data(self):
        yield NepaliDateNeFixture()

    def test_nepalidate_en_renders_date_in_default_format(
        self, fixture_data: NepaliDateNeFixture
    ):
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.date_payload})
        )

        assert rendered == fixture_data.payload_expected_template

    def test_nepalidate_en_renders_date_in_custom_format(
        self, fixture_data: NepaliDateNeFixture
    ):
        rendered = fixture_data.custom_template.render(
            Context({"payload": fixture_data.date_payload})
        )

        assert rendered == fixture_data.payload_expected_custom_template

    def test_nepalidate_en_renders_datetime_in_default_format(
        self, fixture_data: NepaliDateNeFixture
    ):
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.datetime_payload})
        )

        assert rendered == fixture_data.payload_expected_template

    def test_nepalidate_en_renders_datetime_in_custom_format(
        self, fixture_data: NepaliDateNeFixture
    ):
        rendered = fixture_data.custom_template.render(
            Context({"payload": fixture_data.datetime_payload})
        )

        assert rendered == fixture_data.payload_expected_custom_template

    def test_nepalidate_en_renders_nepalidate_in_default_format(
        self, fixture_data: NepaliDateNeFixture
    ):
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.nepalidate_payload})
        )

        assert rendered == fixture_data.payload_expected_template

    def test_nepalidate_en_renders_nepalidate_in_custom_format(
        self, fixture_data: NepaliDateNeFixture
    ):
        rendered = fixture_data.custom_template.render(
            Context({"payload": fixture_data.nepalidate_payload})
        )

        assert rendered == fixture_data.payload_expected_custom_template

    def test_nepalidate_en_renders_nepalidatetime_in_default_format(
        self, fixture_data: NepaliDateNeFixture
    ):
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.nepalidatetime_payload})
        )

        assert rendered == fixture_data.payload_expected_template

    def test_nepalidate_en_renders_nepalidatetime_in_custom_format(
        self, fixture_data: NepaliDateNeFixture
    ):
        rendered = fixture_data.custom_template.render(
            Context({"payload": fixture_data.nepalidatetime_payload})
        )

        assert rendered == fixture_data.payload_expected_custom_template

    def test_nepalidate_en_returns_empty_string_when_invalid_object_is_passed(
        self, fixture_data: NepaliDateNeFixture
    ):
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.invalid_payload})
        )

        assert rendered == ""


class TestNepaliHumanize:
    """
    Tests for nepalihumanize template tag
    """

    @pytest.fixture(scope="class")
    def fixture_data(self):
        yield NepaliHumanizeFixture()

    @mock.patch(f"{MODULE_TO_TEST}.humanize")
    @mock.patch(f"{MODULE_TO_TEST}.to_nepalidatetime")
    def test_nepalihumanize_renders_date_in_default_format_with_no_threshold(
        self,
        mock_to_nepalidatetime: mock.MagicMock,
        mock_humanize: mock.MagicMock,
        fixture_data: NepaliHumanizeFixture,
    ):
        # arrange
        mock_to_nepalidatetime.return_value = (
            fixture_data.to_nepalidate_return_value_for_date
        )
        mock_humanize.return_value = fixture_data.payload_expected_template

        # act
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.date_payload})
        )

        # assert
        mock_to_nepalidatetime.assert_called_once_with(fixture_data.date_payload)
        mock_humanize.assert_called_once_with(
            fixture_data.to_nepalidate_return_value_for_date,
            threshold=None,
            format=None,
        )
        assert rendered == fixture_data.payload_expected_template

    @mock.patch(f"{MODULE_TO_TEST}.humanize")
    @mock.patch(f"{MODULE_TO_TEST}.to_nepalidatetime")
    def test_nepalihumanize_renders_datetime_in_default_format_with_no_threshold(
        self,
        mock_to_nepalidatetime: mock.MagicMock,
        mock_humanize: mock.MagicMock,
        fixture_data: NepaliHumanizeFixture,
    ):
        # arrange
        mock_to_nepalidatetime.return_value = (
            fixture_data.to_nepalidate_return_value_for_datetime
        )
        mock_humanize.return_value = fixture_data.payload_expected_template

        # act
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.datetime_payload})
        )

        # assert
        mock_to_nepalidatetime.assert_called_once_with(fixture_data.datetime_payload)
        mock_humanize.assert_called_once_with(
            fixture_data.to_nepalidate_return_value_for_datetime,
            threshold=None,
            format=None,
        )
        assert rendered == fixture_data.payload_expected_template

    @mock.patch(f"{MODULE_TO_TEST}.humanize")
    @mock.patch(f"{MODULE_TO_TEST}.to_nepalidatetime")
    def test_nepalihumanize_renders_nepalidate_in_default_format_with_no_threshold(
        self,
        mock_to_nepalidatetime: mock.MagicMock,
        mock_humanize: mock.MagicMock,
        fixture_data: NepaliHumanizeFixture,
    ):
        # arrange
        mock_to_nepalidatetime.return_value = (
            fixture_data.to_nepalidate_return_value_for_nepalidate
        )
        mock_humanize.return_value = fixture_data.payload_expected_template

        # act
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.nepalidate_payload})
        )

        # assert
        mock_to_nepalidatetime.assert_called_once_with(fixture_data.nepalidate_payload)
        mock_humanize.assert_called_once_with(
            fixture_data.to_nepalidate_return_value_for_nepalidate,
            threshold=None,
            format=None,
        )
        assert rendered == fixture_data.payload_expected_template

    @mock.patch(f"{MODULE_TO_TEST}.humanize")
    @mock.patch(f"{MODULE_TO_TEST}.to_nepalidatetime")
    def test_nepalihumanize_renders_nepalidatetime_in_default_format_with_no_threshold(
        self,
        mock_to_nepalidatetime: mock.MagicMock,
        mock_humanize: mock.MagicMock,
        fixture_data: NepaliHumanizeFixture,
    ):
        # arrange
        mock_to_nepalidatetime.return_value = (
            fixture_data.to_nepalidate_return_value_for_nepalidatetime
        )
        mock_humanize.return_value = fixture_data.payload_expected_template

        # act
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.nepalidatetime_payload})
        )

        # assert
        mock_to_nepalidatetime.assert_called_once_with(
            fixture_data.nepalidatetime_payload
        )
        mock_humanize.assert_called_once_with(
            fixture_data.to_nepalidate_return_value_for_nepalidatetime,
            threshold=None,
            format=None,
        )
        assert rendered == fixture_data.payload_expected_template

    def test_nepalihumanize_returns_empty_string_during_error(
        self, fixture_data: NepaliHumanizeFixture
    ):
        rendered = fixture_data.default_template.render(
            Context({"payload": fixture_data.invalid_payload})
        )

        assert rendered == ""


class TestNepaliNow:
    """
    Tests nepalinow template tag
    """

    @pytest.fixture(scope="class")
    def fixture_data(self):
        yield NepaliNowFixture()

    @mock.patch(f"{MODULE_TO_TEST}.nepalinow_en")
    def test_nepalinow_renders_current_time_in_default_format(
        self, mock_nepali_now_en: mock.MagicMock, fixture_data: NepaliNowFixture
    ):
        # arrange
        mock_nepali_now_en.return_value = fixture_data.default_expected_template

        # act
        rendered = fixture_data.default_template.render(Context({}))

        # assert
        mock_nepali_now_en.assert_called_once_with(fixture_data.default_date_format)
        assert rendered == fixture_data.default_expected_template

    @mock.patch(f"{MODULE_TO_TEST}.nepalinow_en")
    def test_nepalinow_renders_current_time_in_custom_format(
        self, mock_nepali_now_en: mock.MagicMock, fixture_data: NepaliNowFixture
    ):
        # arrange
        mock_nepali_now_en.return_value = fixture_data.custom_expected_template

        # act
        rendered = fixture_data.custom_template.render(Context({}))

        # assert
        mock_nepali_now_en.assert_called_once_with(fixture_data.custom_date_format)
        assert rendered == fixture_data.custom_expected_template


class TestNepaliNowEn:
    """
    Tests nepalinow_en template tag
    """

    @pytest.fixture(scope="class")
    def fixture_data(self):
        yield NepaliNowEnFixture()

    @mock.patch(f"{MODULE_TO_TEST}.timezone.now")
    @mock.patch(f"{MODULE_TO_TEST}.to_nepalidatetime")
    def test_nepalinow_en_renders_current_time_in_default_format(
        self,
        mock_to_nepalidatetime: mock.MagicMock,
        mock_timezone_now: mock.MagicMock,
        fixture_data: NepaliNowEnFixture,
    ):
        mock_to_nepalidatetime.return_value.strftime.return_value = (
            fixture_data.default_expected_template
        )
        mock_timezone_now.return_value = fixture_data.dummy_time

        rendered = fixture_data.default_template.render(Context({}))

        mock_timezone_now.assert_called_once()
        mock_to_nepalidatetime.assert_called_once_with(fixture_data.dummy_time)
        mock_to_nepalidatetime.return_value.strftime.assert_called_once_with(
            fixture_data.default_date_format
        )
        assert rendered == fixture_data.default_expected_template

    @mock.patch(f"{MODULE_TO_TEST}.timezone.now")
    @mock.patch(f"{MODULE_TO_TEST}.to_nepalidatetime")
    def test_nepalinow_en_renders_current_time_in_custom_format(
        self,
        mock_to_nepalidatetime: mock.MagicMock,
        mock_timezone_now: mock.MagicMock,
        fixture_data: NepaliNowEnFixture,
    ):
        mock_to_nepalidatetime.return_value.strftime.return_value = (
            fixture_data.custom_expected_template
        )
        mock_timezone_now.return_value = fixture_data.dummy_time

        rendered = fixture_data.custom_template.render(Context({}))

        mock_timezone_now.assert_called_once()
        mock_to_nepalidatetime.assert_called_once_with(fixture_data.dummy_time)
        mock_to_nepalidatetime.return_value.strftime.assert_called_once_with(
            fixture_data.custom_date_format
        )
        assert rendered == fixture_data.custom_expected_template


class TestNepaliNowNe:
    """
    Tests nepalinow_ne template tag
    """

    @pytest.fixture(scope="class")
    def fixture_data(self):
        yield NepaliNowNeFixture()

    @mock.patch(f"{MODULE_TO_TEST}.timezone.now")
    @mock.patch(f"{MODULE_TO_TEST}.to_nepalidatetime")
    def test_nepalinow_en_renders_current_time_in_default_format(
        self,
        mock_to_nepalidatetime: mock.MagicMock,
        mock_timezone_now: mock.MagicMock,
        fixture_data: NepaliNowNeFixture,
    ):
        mock_to_nepalidatetime.return_value.strftime_ne.return_value = (
            fixture_data.default_expected_template
        )
        mock_timezone_now.return_value = fixture_data.dummy_time

        rendered = fixture_data.default_template.render(Context({}))

        mock_timezone_now.assert_called_once()
        mock_to_nepalidatetime.assert_called_once_with(fixture_data.dummy_time)
        mock_to_nepalidatetime.return_value.strftime_ne.assert_called_once_with(
            fixture_data.default_date_format
        )
        assert rendered == fixture_data.default_expected_template

    @mock.patch(f"{MODULE_TO_TEST}.timezone.now")
    @mock.patch(f"{MODULE_TO_TEST}.to_nepalidatetime")
    def test_nepalinow_en_renders_current_time_in_custom_format(
        self,
        mock_to_nepalidatetime: mock.MagicMock,
        mock_timezone_now: mock.MagicMock,
        fixture_data: NepaliNowNeFixture,
    ):
        mock_to_nepalidatetime.return_value.strftime_ne.return_value = (
            fixture_data.custom_expected_template
        )
        mock_timezone_now.return_value = fixture_data.dummy_time

        rendered = fixture_data.custom_template.render(Context({}))

        mock_timezone_now.assert_called_once()
        mock_to_nepalidatetime.assert_called_once_with(fixture_data.dummy_time)
        mock_to_nepalidatetime.return_value.strftime_ne.assert_called_once_with(
            fixture_data.custom_date_format
        )
        assert rendered == fixture_data.custom_expected_template

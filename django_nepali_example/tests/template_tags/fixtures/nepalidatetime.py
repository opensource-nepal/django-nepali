"""
Contains fixtures for tests related to
nepalidatetime module
"""

import datetime

from django.template import Template
from nepali.datetime import nepalidate as _nepalidate
from nepali.datetime import nepalidatetime as _nepalidatetime


class NepaliDateFixture:
    # common fixtures
    template = Template("{% load nepalidatetime %}{{ payload|nepalidate }}")
    payload_expected_template = "Jestha 13, 2080, Saturday"

    # fixtures for date(built-in)
    date_payload = datetime.date(2023, 5, 27)

    # fixtures for datetime(built-in)
    datetime_payload = datetime.datetime(2023, 5, 27, 9, 24, 29)

    # fixtures for nepalidate
    nepalidate_payload = _nepalidate(2080, 2, 13)

    # fixtures for nepalidatetime
    nepalidatetime_payload = _nepalidatetime(2080, 2, 13)

    # fixtures for errors
    invalid_payload = object


class NepaliDateEnFixture:
    # default/common fixtures
    default_template = Template("{% load nepalidatetime %}{{ payload|nepalidate_en }}")
    payload_expected_template = "Jestha 24, 2080, Wednesday"

    # custom fixtures
    custom_template = Template(
        "{% load nepalidatetime %}{{ payload|nepalidate_en:'%Y/%m/%d' }}"
    )
    payload_expected_custom_template = "2080/02/24"

    # fixtures for date(built-in)
    date_payload = datetime.date(2023, 6, 7)

    # fixtures for datetime(built-in)
    datetime_payload = datetime.datetime(2023, 6, 7, 9, 34, 40)

    # fixtures for nepalidate
    nepalidate_payload = _nepalidate(2080, 2, 24)

    # fixtures for nepalidatetime
    nepalidatetime_payload = _nepalidatetime(2080, 2, 24, 9, 34, 40)

    # fixtures for errors
    invalid_payload = object


class NepaliDateNeFixture:
    # default/common fixtures
    default_template = Template("{% load nepalidatetime %}{{ payload|nepalidate_ne }}")
    payload_expected_template = "जेठ २४, २०८०, बुधबार"

    # custom fixtures
    custom_template = Template(
        "{% load nepalidatetime %}{{ payload|nepalidate_ne:'%Y/%m/%d' }}"
    )
    payload_expected_custom_template = "२०८०/०२/२४"

    # fixtures for date(built-in)
    date_payload = datetime.date(2023, 6, 7)

    # fixtures for datetime(built-in)
    datetime_payload = datetime.datetime(2023, 6, 7, 9, 34, 40)

    # fixtures for nepalidate
    nepalidate_payload = _nepalidate(2080, 2, 24)

    # fixtures for nepalidatetime
    nepalidatetime_payload = _nepalidatetime(2080, 2, 24, 9, 34, 40)

    # fixtures for errors
    invalid_payload = object


class NepaliHumanizeFixture:
    # default/common fixtures
    default_template = Template("{% load nepalidatetime %}{{ payload|nepalihumanize }}")
    payload_expected_template = "२२ घण्टा अघि"

    # fixtures for date(built-in)
    date_payload = datetime.date(2023, 6, 7)
    to_nepalidate_return_value_for_date = "<nepalidatetime> 2080-02-24 00:00:00"

    # fixtures for datetime(built-in)
    datetime_payload = datetime.datetime(2023, 6, 7, 21, 30)
    to_nepalidate_return_value_for_datetime = "<nepalidatetime> 2080-02-24 21:30:00"

    # fixtures for nepalidate
    nepalidate_payload = _nepalidate(2080, 2, 24)
    to_nepalidate_return_value_for_nepalidate = "<nepalidatetime> 2080-02-24 00:00:00"

    # fixtures for nepalidatetime
    nepalidatetime_payload = _nepalidatetime(2080, 2, 24, 21, 30)
    to_nepalidate_return_value_for_nepalidatetime = (
        "<nepalidatetime> 2080-02-24 21:30:00"
    )

    # fixtures for error
    invalid_payload = object


class NepaliNowFixture:
    # default values
    default_expected_template = "Jestha 25, 2080, Thursday"
    default_template = Template("{% load nepalidatetime %}{% nepalinow %}")
    default_date_format = "%B %d, %Y, %A"

    # custom values
    custom_template = Template("{% load nepalidatetime %}{% nepalinow '%Y/%m/%d' %}")
    custom_expected_template = "2080/02/25"
    custom_date_format = "%Y/%m/%d"


class NepaliNowEnFixture:
    # default values
    default_expected_template = "Jestha 25, 2080, Thursday"
    default_template = Template("{% load nepalidatetime %}{% nepalinow_en %}")
    default_date_format = "%B %d, %Y, %A"

    # custom values
    custom_template = Template("{% load nepalidatetime %}{% nepalinow_en '%Y/%m/%d' %}")
    custom_expected_template = "2080/02/25"
    custom_date_format = "%Y/%m/%d"

    # common values
    dummy_time = datetime.datetime(2023, 6, 9, 15, 55, 17, 564349)


class NepaliNowNeFixture:
    # default values
    default_expected_template = "जेठ २६, २०८०, शुक्रबार"
    default_template = Template("{% load nepalidatetime %}{% nepalinow_ne %}")
    default_date_format = "%B %d, %Y, %A"

    # custom values
    custom_template = Template("{% load nepalidatetime %}{% nepalinow_ne '%Y/%m/%d' %}")
    custom_expected_template = "२०८०/०२/२६"
    custom_date_format = "%Y/%m/%d"

    # common values
    dummy_time = datetime.datetime(2023, 6, 9, 15, 55, 17, 564349)

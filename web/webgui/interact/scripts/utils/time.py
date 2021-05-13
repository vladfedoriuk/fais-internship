import re
from datetime import datetime
from django.conf import settings


DATETIME_FORMATS = settings.DATETIME_INPUT_FORMATS + settings.DATE_INPUT_FORMATS


def convert_datetime(date_time: datetime) -> str:
    for pattern in DATETIME_FORMATS:
        try:
            str_datetime = date_time.strftime(pattern)
            return str_datetime
        except:
            pass

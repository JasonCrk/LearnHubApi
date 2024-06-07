from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_datetime_is_future(value: datetime):
    if value <= datetime.now():
        raise ValidationError(
            _("It cannot be a past datetime"),
            params={'value': value}
        )

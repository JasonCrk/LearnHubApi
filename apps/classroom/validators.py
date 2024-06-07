from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import re


def validate_hex_color(value: str):
    if len(value) != 7 or value[0] != '#':
        raise ValidationError(
            _("%(value)s is not a hexadecimal color"),
            params={'value': value}
        )

def validate_access_code(value: str):
    if re.match("[a-z0-9]{7}", value) is None:
        raise ValidationError(
            _("The access code is invalid"),
            params={'value': value}
        )

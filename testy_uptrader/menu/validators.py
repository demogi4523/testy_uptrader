from json import JSONDecodeError, dumps

from django.core.exceptions import ValidationError


def validate_json_content(value):
    try:
        print(value)
        res = dumps(value)
        print(res)
    except JSONDecodeError as err:
        raise ValidationError(message=err)

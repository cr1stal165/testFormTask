import re
from datetime import datetime


def validate_form_fields(value, field_type):
    if field_type == "date":
        date_formats = ['%d.%m.%Y', '%Y-%m-%d']
        for date_format in date_formats:
            try:
                datetime.strptime(value, date_format)
                return True
            except ValueError:
                pass
        return False
    elif field_type == "phone":
        phone_pattern = re.compile(r'^\+\d{1,2}\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{2}[-.\s]?\d{2}$')
        return bool(phone_pattern.match(value))
    elif field_type == "email":
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        return bool(email_pattern.match(value))


def typing_form(fields_dict):
    field_types = {}
    for field_name, field_value in fields_dict.items():
        if validate_form_fields(field_value, "date"):
            field_types[field_name] = "date"
        elif validate_form_fields(field_value, "phone"):
            field_types[field_name] = "phone"
        elif validate_form_fields(field_value, "email"):
            field_types[field_name] = "email"
        else:
            field_types[field_name] = "text"

    return field_types
import re
from datetime import datetime

from fastapi import APIRouter, Query
from database import db
from src.forms.validation import typing_form

router_forms = APIRouter(
    tags=["Forms"]
)


def find_template(fields):
    for template in db.all():
        template_fields = template.copy()
        template_name = template_fields.pop("name", None)
        temp_fields = typing_form(fields)
        if all(
            field in temp_fields and temp_fields[field] == template_fields[field]
            for field in template_fields
        ):
            return template_name
    return None


def convert_params(fields: str) -> dict:
    query_dict = {}
    params_list = fields.split("&")
    for param in params_list:
        key, value = param.split("=")
        query_dict[key] = value
    return query_dict


@router_forms.post("/get_form")
def get_form(fields: str):
    fields_dict = convert_params(fields)
    matching_template = find_template(fields_dict)

    if matching_template:
        return {"template_name": matching_template}

    return typing_form(fields_dict)


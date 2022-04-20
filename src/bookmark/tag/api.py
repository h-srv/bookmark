from flask import Blueprint, jsonify, request

from .domain import TagRepository, Tag
from ..infrastructure import validator

blueprint_tag = Blueprint('blueprint_tag', __name__)


@blueprint_tag.get('')
def tag_list():
    """return tag list for user_rel"""
    list_schema = {
        'user_rel': {'type': 'string', 'required': True}
    }

    if not validator.validate(request.args, list_schema):
        raise ValueError(validator.errors, 422)

    tags = TagRepository.get_where(request.args)
    return jsonify(tags)


@blueprint_tag.post('')
def tag_create():
    list_schema = {
        'title': {'type': 'string', 'required': True},
        'user_rel': {'type': 'string', 'required': True}
    }

    if not validator.validate(request.json, list_schema):
        raise ValueError(validator.errors, 422)

    tag = TagRepository.create_or_fail(Tag, request.json)
    return jsonify(tag)

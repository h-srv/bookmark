from flask import Blueprint, jsonify, request

from .domain import TagRepository, Tag
from ..infrastructure import validate_or_fail

blueprint_tag = Blueprint('blueprint_tag', __name__)


@blueprint_tag.get('')
def tag_list():
    """return tag list for user_rel"""
    list_schema = {
        'user_rel': {'type': 'string', 'required': True}
    }

    validate_or_fail(request.args, list_schema)

    tags = TagRepository.get_where(request.args)
    return jsonify(tags)


@blueprint_tag.post('')
def tag_create():
    list_schema = {
        'title': {'type': 'string', 'required': True},
        'user_rel': {'type': 'string', 'required': True}
    }

    validate_or_fail(request.json, list_schema)

    tag = TagRepository.create_or_fail(Tag, request.json)
    return jsonify(tag)

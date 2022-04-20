from flask import Blueprint, jsonify, request

from .domain import TagRepository
from ..infrastructure import validator

blueprint_tag = Blueprint('blueprint_tag', __name__)


@blueprint_tag.get('')
def tag_list():
    list_schema = {
        'user_rel': {
            'type': 'string',
            'required': True
        }
    }

    if not validator.validate(request.args, list_schema):
        raise ValueError(validator.errors, 422)

    tags = TagRepository.get_where(request.args)
    return jsonify(tags)

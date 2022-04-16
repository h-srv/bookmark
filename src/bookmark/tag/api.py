from flask import Blueprint, jsonify

from .domain import TagRepository

blueprint_tag = Blueprint('blueprint_tag', __name__)


@blueprint_tag.get('')
def tag_list():
    tags = TagRepository.get_where({})
    return jsonify(tags)

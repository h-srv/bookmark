# from .domain import TagRepository
# from . import blueprint_tag
from flask import Blueprint

blueprint_tag = Blueprint('blueprint_tag', __name__)


@blueprint_tag.get('')
def tag_list():
    return {}

# @tag_ns.route('')
# class TagList(Resource):
    # def post(self):
    #     """Create a tag"""
    #     tag_mdl = TagDTO.to_tag(tag_ns.payload)
    #     TagRepository.create_or_fail(tag_mdl)
    #     return tag_mdl

    # @tag_ns.expect(tag_parser)
    # def get(self):
    #     """List of tag by user"""
    #     tag_parser.add_argument(
    #         'user_rel',
    #         type=int,
    #         required=True,
    #         help='`user_rel` missing,',
    #         location='args')
    #     args = tag_parser.parse_args()
    #
    #     tags = TagSchema(many=True)
    #     return tags.dump(TagRepository.get_where(args))

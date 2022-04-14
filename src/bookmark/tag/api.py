from flask_restx import Namespace, Resource, reqparse

from .domain import TagRepository, TagSchema

tag_ns = Namespace('api/v1/tags', description='Tag api')
tag_parser = reqparse.RequestParser()


@tag_ns.route('')
class TagList(Resource):
    # def post(self):
    #     """Create a tag"""
    #     tag_mdl = TagDTO.to_tag(tag_ns.payload)
    #     TagRepository.create_or_fail(tag_mdl)
    #     return tag_mdl

    @tag_ns.expect(tag_parser)
    def get(self):
        """List of tag by user"""
        tag_parser.add_argument(
            'user_rel',
            type=int,
            required=True,
            help='`user_rel` missing,',
            location='args')
        args = tag_parser.parse_args()

        tags = TagSchema(many=True)
        return tags.dump(TagRepository.get_where(args))

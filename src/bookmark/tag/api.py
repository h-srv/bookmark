from flask_restx import Namespace, Resource, fields

from .domain import TagRepository, TagDTO


tag_ns = Namespace('api/v1/tags', description='Tag api')
tag = tag_ns.model('Tag', {
    'id': fields.Integer(readonly=True, description='The tag unique identifier'),
    'title': fields.String(required=True, description='The tag title'),
    'user_rel': fields.String(required=False, description='The tag user identifier'),
    'created_at': fields.String(readonly=True, description='The tag create datetime'),
    'updated_at': fields.String(readonly=True, description='The tag update datetime'),
})


@tag_ns.route('')
class TagList(Resource):
    @tag_ns.doc('tag.create')
    @tag_ns.expect(tag)
    @tag_ns.marshal_with(tag, code=201)
    def post(self):
        """Create a tag"""
        tag_mdl = TagDTO.to_tag(tag_ns.payload)
        TagRepository.create_or_fail(tag_mdl)
        return tag_mdl


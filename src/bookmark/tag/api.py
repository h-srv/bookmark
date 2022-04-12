from flask_restx import Namespace, Resource, fields, reqparse

from .domain import TagRepository, TagDTO

tag_ns = Namespace('api/v1/tags', description='Tag api')
tag = tag_ns.model('Tag', {
    'id': fields.Integer(readonly=True, description='The tag unique identifier'),
    'title': fields.String(required=True, description='The tag title'),
    'user_rel': fields.String(required=False, description='The tag user identifier'),
    'created_at': fields.String(readonly=True, description='The tag create datetime'),
    'updated_at': fields.String(readonly=True, description='The tag update datetime'),
})

reqp = reqparse.RequestParser()


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

    @tag_ns.doc('tag.list')
    @tag_ns.expect(reqp)
    @tag_ns.marshal_list_with(tag)
    def get(self):
        """Create a tag"""
        reqp.add_argument('user_rel',
                          type=int,
                          required=True,
                          location='args',
                          help='`user_rel` is')
        req_args = reqp.parse_args()

        return TagRepository.get_where(req_args)

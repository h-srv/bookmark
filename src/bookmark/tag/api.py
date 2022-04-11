from flask_restx import Namespace, Resource, fields

tag_ns = Namespace('api/v1/tags', description='Tag api')

tag = tag_ns.model('Tag', {
    'id': fields.Integer(readonly=True, description='The tag unique identifier'),
    'title': fields.String(required=True, description='The tag title'),
    'user_rel': fields.String(required=False, description='The tag user identifier'),
})


@tag_ns.route('')
class TagList(Resource):
    @tag_ns.doc('create-tag')
    @tag_ns.expect(tag)
    @tag_ns.marshal_with(tag, code=201)
    def post(self):
        """Create a tag"""
        print(tag_ns.payload)
        return tag_ns.payload

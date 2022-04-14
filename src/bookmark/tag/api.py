from flask_restx import Namespace, Resource, fields, reqparse

from .domain import TagRepository, TagDTO

tag_ns = Namespace('api/v1/tags', description='Tag api')


@tag_ns.route('')
class TagList(Resource):
    def post(self):
        """Create a tag"""
        tag_mdl = TagDTO.to_tag(tag_ns.payload)
        TagRepository.create_or_fail(tag_mdl)
        return tag_mdl

    def get(self):
        """List of tag by user"""
        # return TagRepository.get_where()

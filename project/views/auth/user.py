from flask import request
from flask_restx import Resource, Namespace

from project.tools.security import auth_required, get_email_from_token
from project.setup.api.models import user
from project.container import user_service

api = Namespace('user')


@api.route('/')
class UserView(Resource):

    @auth_required
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self, email=None):
        return user_service.get_by_email(email)

    @auth_required
    def patch(self, email=None):
        req_json = request.json
        req_json['email'] = email
        user_service.update(req_json)
        return '', 204


@api.route('/password/')
class PasswordView(Resource):

    @auth_required
    def put(self, email=None):
        req_json = request.json
        req_json['email'] = email
        user_service.update_password(req_json)
        return '', 204

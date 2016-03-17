# -*- coding: utf-8 -*-

from flask import render_template,jsonify,current_app,g
from flask import Blueprint
from flask_restful import reqparse, abort, Api, Resource,marshal
from flask.ext.httpauth import HTTPBasicAuth
from models import *


testRest = Blueprint('testRest', __name__,url_prefix='/api')
api = Api()
api.init_app(testRest)

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('expire',type=int)


# Create a new resource
class Users(Resource):
  def post(self):
    data = parser.parse_args()
    username = data['username']
    password = data['password']
    if username is None or password is None:
        print "missing argument"
        abort(400,message='missing argument')    # missing argument
    if User.query.filter_by(username=username).first() is not None:
        print "existing user"
        abort(400,message='existing user')    # existing user
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return {'username':user.username}

#Get the User details
class UserRes(Resource):
  def get(self,tid):
    user = User.query.get(tid)
    if not user:
        abort(400,message='user not found')
    return {'username': user.username}


# Generate an authentication token
class AuthToken(Resource):
  @auth.login_required
  def get(self):
    data = parser.parse_args()
    print data['expire']
    exipery = 600
    if data['expire'] != None:
      exipery = data['expire']
    token = g.user.generate_auth_token(exipery)
    return {'token': token.decode('ascii'), 'duration': exipery}

# Get a user resource after authentication
class HResource(Resource):
  @auth.login_required
  def get(self):
    return {'data': 'Hello, %s!' %g.user.username}

api.add_resource(Users, '/users')
api.add_resource(UserRes, '/user/<tid>')
api.add_resource(AuthToken, '/token')
api.add_resource(HResource, '/resource')

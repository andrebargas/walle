import logging
from flask import request, jsonify, abort, make_response
from flask_restplus import Resource, Api
from ..restplus import api
from ..model.user_actions import give_points, list_users, use_points, get_user_detail, add_user
from ..model.benefits_actions import insert_benefit, get_benefits_cost


ns = api.namespace('user', description='Api para gerenciamento de usuarios')


@ns.route('/add')
class User(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def get(self):
        add_user()
        return 200


@ns.route('/detail')
class UserDetail(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        user_id = data["user_id"]
        user = get_user_detail(user_id)
        return jsonify(user)


@ns.route('/list')
class UserList(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def get(self):
        users = list_users()
        return jsonify(users)


@ns.route('/give_points')
class GivePoints(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        user_id = data["user_id"]
        points_to_give = data["points"]

        if give_points(user_id, points_to_give):
            return 200
        else:
            return 500


@ns.route('/use_points')
class UsePoints(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        user_id = data["user_id"]
        benefit_id = data["benefit_id"]

        user = get_user_detail(user_id)
        cost = get_benefits_cost(benefit_id)

        if use_points(user, cost):
            return 200
        else:
            return 500

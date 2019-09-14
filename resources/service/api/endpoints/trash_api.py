import logging
from flask import request, jsonify, abort, make_response
from flask_restplus import Resource, Api
from ..restplus import api
from ..model.trash_actions import  get_trash_detail, list_trash, insert_trash


ns = api.namespace('trash', description='Api para gerenciamento de usuarios')

@ns.route('/add')
class Trash(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def get(self):
        insert_trash()
        return 200

@ns.route('/detail')
class TrashDetail(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        trash_id = data["trash_id"]
        trash = get_trash_detail(trash_id)
        return jsonify(trash)


@ns.route('/list')
class TrashList(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def get(self):
        trashs = list_trash()
        return jsonify(trashs)

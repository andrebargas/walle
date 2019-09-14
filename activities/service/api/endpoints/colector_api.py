import logging
from flask import request, jsonify, abort, make_response
from flask_restplus import Resource, Api
from ..restplus import api
from ..model.colector_actions import insert_colector, get_colector_by_trash, list_colector
import requests

ns = api.namespace('colector', description='Api para gerenciamento de coletas')


@ns.route('/new')
class Colector(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        trash_id = data["trash_id"]
        trash_type = data["trash_type"]
        insert_colector(trash_id, trash_type)

        return 200


@ns.route('/bytrash')
class ColectorListTrash(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        trash_id = data["trash_id"]
        colector = get_colector_by_trash(trash_id)
        return jsonify(colector)


@ns.route('/list')
class ColectorList(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def get(self):
        colectors = list_colector()
        return jsonify(colectors)

import logging
from flask import request, jsonify, abort, make_response
from flask_restplus import Resource, Api
from ..restplus import api
from ..model.partner_actions import get_partner_detail, list_partner, insert_partner


ns = api.namespace('partner', description='Api para gerenciamento de usuarios')


@ns.route('/add')
class Partner(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def get(self):
        insert_partner()
        return 200


@ns.route('/detail')
class PartnerDetail(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        partner_id = data["partner_id"]
        partner = get_partner_detail(partner_id)
        return jsonify(partner)


@ns.route('/list')
class PartnerList(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def get(self):
        partner = list_partner()
        return jsonify(partner)

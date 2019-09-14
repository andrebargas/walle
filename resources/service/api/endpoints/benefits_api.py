import logging
from flask import request, jsonify, abort, make_response
from flask_restplus import Resource, Api
from ..restplus import api
from ..model.benefits_actions import  get_benefit_detail, list_benefits


ns = api.namespace('benefits', description='Api para gerenciamento de usuarios')


@ns.route('/detail')
class BenefitsDetail(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        benefit_id = data["benefit_id"]
        benefit = get_benefit_detail(benefit_id)
        return jsonify(benefit)


@ns.route('/list')
class BenefitsList(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def get(self):
        benefits = list_benefits()
        return jsonify(benefits)

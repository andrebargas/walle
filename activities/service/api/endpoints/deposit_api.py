import logging
from flask import request, jsonify, abort, make_response
from flask_restplus import Resource, Api
from ..restplus import api
from ..model.deposit_actions import get_deposits_by_trash,\
                                    list_deposit, \
                                    insert_deposit,\
                                    get_deposits_by_user,\
                                    deleteAllDeposits
from ..bo.preprocess import preprocessmessage
import requests

ns = api.namespace('deposit', description='Api para gerenciamento de depositos')


@ns.route('/postman/new')
class Deposit(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        user_id = data[1]
        trash_id = 1
        trash_type = data[1]
        deposit = insert_deposit(user_id, trash_id, trash_type)

        print(deposit)
        print(type(deposit))

        points = trash_type * 10

        payload = {
            "user_id": user_id,
            "points": points,
        }

        requests.post("http://resources:5000/api/user/give_points", json=payload)


        return 200

@ns.route('/new')
class Deposit(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        data = preprocessmessage(data)
        user_id = data[1]
        trash_id = 1
        trash_type = data[1]
        deposit = insert_deposit(user_id, trash_id, trash_type)

        print(deposit)
        print(type(deposit))

        points = trash_type * 10

        payload = {
            "user_id": user_id,
            "points": points,
        }

        requests.post("http://resources:5000/api/user/give_points", json=payload)


        return 200

@ns.route('/byuser')
class DepositListUser(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        deposit_id = data["user_id"]
        deposit = get_deposits_by_user(deposit_id)
        return jsonify(deposit)

@ns.route('/bytrash')
class DepositListTrash(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def post(self):
        data = request.get_json()
        trash_id = data["trash_id"]
        deposit = get_deposits_by_trash(trash_id)
        return jsonify(deposit)


@ns.route('/list')
class DepositList(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def get(self):
        deposits = list_deposit()
        return jsonify(deposits)

@ns.route('/delete_all')
class DepositList(Resource):

    @ns.doc(params={
        "exp": "exemplo"
    })
    def get(self):
        deleteAllDeposits()
        return 200
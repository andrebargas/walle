from ..restplus import deposit_collection
import datetime
import pytz


def insert_deposit(user_id, trash_id, trash_type):
    deposit = {
        "date_time": datetime.datetime.now(tz=pytz.utc).strftime("%d/%m/%Y %H:%M"),
        "user_id": user_id,
        "trash_id": trash_id,
        "trash_type": trash_type
    }
    deposit_collection.insert_one(deposit)



def deleteAllDeposits():
    deposit_collection.drop({})


def list_deposit():

    deposits = []
    query_result = deposit_collection.find()

    for deposit in query_result:
        deposit["_id"] = str(deposit["_id"])
        deposits.append(deposit)

    return deposits


def get_deposits_by_trash(trash_id):

    deposits = []
    query = {"trash_id": trash_id}
    query_result = deposit_collection.find_many(query)

    for deposit in query_result:
        deposit["_id"] = str(deposit["_id"])
        deposits.append(deposit)

    return deposits


def get_deposits_by_user(user_id):
    deposits = []
    query = {"user_id": user_id}
    query_result = deposit_collection.find_many(query)

    for deposit in query_result:
        deposit["_id"] = str(deposit["_id"])
        deposits.append(deposit)

    return deposits
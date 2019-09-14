from ..restplus import colector_collection
import datetime


def insert_colector( trash_id, trash_type):
    colector = {
        "date_time": str(datetime.datetime.now()),
        "trash_id": trash_id,
        "trash_type": trash_type
    }
    colector_collection.insert_one(colector)

def list_colector():

    deposits = []
    query_result = colector_collection.find()

    for colector in query_result:
        colector["_id"] = str(colector["_id"])
        deposits.append(colector)

    return deposits


def get_colector_by_trash(trash_id):

    deposits = []
    query = {"trash_id": trash_id}
    query_result = colector_collection.find_many(query)

    for colector in query_result:
        colector["_id"] = str(colector["_id"])
        deposits.append(colector)

    return deposits

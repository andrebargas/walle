from ..restplus import trash_collection


# para mock
def insert_trash():
    benefit = {
        "id":1,
        "location": [15.7107969, -47.911003],
        "status": "ok"
    }
    trash_collection.insert_one(benefit)

def list_trash():

    trashs = []
    query_result = trash_collection.find()

    for trash in query_result:
        trash["_id"] = str(trash["_id"])
        trashs.append(trash)

    return trashs


def get_trash_detail(trash_id):

    query = {"id": trash_id}
    trash = trash_collection.find_one(query)

    trash["_id"] = str(trash["_id"])

    return trash

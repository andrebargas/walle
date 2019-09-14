from ..restplus import partner_collection


# para mock
def insert_partner():
    partner = {
        "id":1,
        "name": "parceiro X",
        "description": "Nos oferecemos o serviço X",
        "localizacao": [15.8367892, -47.9708206]
    }
    partner_collection.insert_one(partner)


def list_partner():

    partners = []
    query_result = partner_collection.find()

    for partner in query_result:
        partner["_id"] = str(partner["_id"])
        partners.append(partner)

    return partner


def get_partner_detail(partner_id):

    query = {"id": partner_id}
    partner = partner_collection.find_one(query)

    partner["_id"] = str(partner["_id"])

    return partner
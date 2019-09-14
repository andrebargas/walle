from ..restplus import benefits_collection


# para mock
def insert_benefit():
    benefit = {
        "id":1,
        "name": "beneficioX",
        "description": "Descrição do beneficio",
        # Dado mockado
        "partner_id": 1,
        "cost": 5
    }
    benefits_collection.insert_one(benefit)


def list_benefits():

    benefits = []
    query_result = benefits_collection.find()

    for benefit in query_result:
        benefit["_id"] = str(benefit["_id"])
        benefits.append(benefit)

    return benefits


def get_benefit_detail(benefit_id):

    query = {"id": benefit_id}
    benefit = benefits_collection.find_one(query)

    benefit["_id"] = str(benefit["_id"])

    return benefit


def get_benefits_cost(benefit_id):
    query = {"id": benefit_id}
    benefit = benefits_collection.find_one(query)

    return benefit["cost"]

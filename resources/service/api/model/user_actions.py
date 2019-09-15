from ..restplus import user_collection


def list_users():
    query = user_collection.find()
    users = []
    for user in query:
        user["_id"] = str(user["_id"])
        users.append(user)
    return users


def get_user_detail(user_id):
    my_query = {"id": user_id}
    user = user_collection.find_one(my_query)
    user["_id"] = str(user["_id"])

    return user


#usado só para iserir o dado mockado
def add_user(name, email):
    user = {
        "id":2,
        "name":name,
        "email":email,
        "points": 0
    }
    user_collection.insert_one(user)


def give_points(user_id, points):

    my_query = {"id": user_id}
    user = user_collection.find_one(my_query)

    new_points = user["points"] + points

    new_values = {"$set": {"points": new_points}}

    user_collection.update_one(user, new_values)

    return True


def use_points(user, cost):

    if user["points"] < cost:
        return False

    new_points = user["points"] - cost

    new_values = {"$set": {"points": new_points}}

    user_collection.update_one(user, new_values)

    return True
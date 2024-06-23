from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    results = []
    if args == {}:
        return USERS

    # for user in USERS:

    #     # search for id
    #     if "id" in args:
    #         if user['id'] == args['id']:
    #             results.append(user)
    #             continue

    #     # partial search for name
    #     if "name" in args:
    #         # if user["name"] in USERS 
    #         if args["name"].lower() in user["name"].lower():
    #             results.append(user)
    #             continue
        
    #     # search for age (+-1) 
    #     if "age" in args:
    #         if (user['age'] >= int(args['age'])-1) and (user['age'] <= int(args['age'])+1):
    #             results.append(user)
    #             continue
        
    #     if "occupation" in args:
    #         if args["occupation"].lower() in user["occupation"].lower():
    #             results.append(user)
    #             continue

    # return results

    # tempUsers = USERS

    
    # BONUS CHALLENGE
    seen_ids = []
    for arg in args:
        for user in USERS:
            if arg == "id":
                if user["id"] == args["id"] and user["id"] not in seen_ids:
                    results.append(user)
                    seen_ids.append(user["id"])
                    continue
            elif arg == "age":
                if (user["age"] >= int(args["age"]) - 1) and (user["age"] <= int(args["age"]) + 1) and user["id"] not in seen_ids:
                    results.append(user)
                    seen_ids.append(user["id"])
                    continue
            elif arg == "name":
                if args["name"].lower() in user["name"].lower() and user["id"] not in seen_ids:
                    results.append(user)
                    seen_ids.append(user["id"])
                    continue
            elif arg == "occupation":
                if args["occupation"].lower() in user["occupation"].lower() and user["id"] not in seen_ids:
                    results.append(user)
                    seen_ids.append(user["id"])
                    continue

    return results
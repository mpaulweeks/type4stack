import json

with open("../scripts/multiverse_ids.json") as json_file:
    id_dict = json.load(json_file)


def get_id(name):
    lower = name.lower()
    return id_dict.get(lower)

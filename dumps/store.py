
import json


def load_cards():
    with open("data.json") as cards_file:
        data = json.load(cards_file)
    cards_by_id = {card["id"]: card for card in data["card"]}
    status = data["status"]

    print cards_by_id
    print status

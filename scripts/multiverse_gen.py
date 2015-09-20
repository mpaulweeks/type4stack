import json

out = {}
with open("AllSets.json") as file:
    sets = json.load(file)
for card_set in sets.values():
    for card in card_set["cards"]:
        name = card["name"].lower()
        out[name] = card.get("multiverseid")

with open("multiverse_ids.json", "w") as file:
    json.dump(out, file)

import json

def save_json(data, name):
    with open(name, "w") as f:
        json.dump(data, f, indent=2)
import json

def save(data, file_name="data.json"):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)
        return data

def load(file_name="data.json"):
    with open(file_name) as f:
        data = json.load(f)
        return data
import json


with open("blabla.json", "r") as f:
    loaded_json = json.load(f)


if __name__ == '__main__':
    print(type(loaded_json))
    print(loaded_json)

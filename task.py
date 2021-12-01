import json

# Opening JSON file
with open('sample-data.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)

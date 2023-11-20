import json

with open('steam.json') as f:
    data_steam = json.load(f)

for data in data_steam:
    print(data_steam[0]['name'])
    break
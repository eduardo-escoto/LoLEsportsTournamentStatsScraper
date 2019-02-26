import sys
import json

slugList = []
navItemsPath = sys.argv[1]
leagueSlugsPath = sys.argv[2]

with open(navItemsPath, "r") as read_file:
    data = json.load(read_file)
    leagues = data["leagues"]
    for league in leagues:
        slugList.append({
            "name": league["name"],
            "slug": league["slug"],
            "id": league["id"]
        })


with open(leagueSlugsPath, "w") as data_file:
    json.dump(slugList, data_file, indent=2)

import sys
import json
import requests

navItemsPath = sys.argv[1]
navItemsUri = "https://api.lolesports.com/api/v1/navItems"

with open(navItemsPath, "w") as write_file:
    data = requests.get(navItemsUri).json()
    json.dump(data, write_file, indent=2)

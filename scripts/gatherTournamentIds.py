import requests
import sys
import json

leagueData = []
leagueSlugsPath = sys.argv[1]
leagueDataPath = "data/leagueData/"
leagueApiUrl = "https://api.lolesports.com/api/v1/leagues"


def saveLeagueData(leagueSlug):
    with open(leagueDataPath + leagueSlug + ".json", "w") as write_file:
        data = requests.get(leagueApiUrl, {"slug": leagueSlug}).json()
        json.dump(data, write_file, indent=2)
        return data


def getTournamentData(league):
    tournamentData = []
    slug = league["slug"]
    fileData = saveLeagueData(slug)
    highlanderTournaments = fileData["highlanderTournaments"]
    for tournament in highlanderTournaments:
        tournamentData.append({
            "id": tournament.get("id", None),
            "title": tournament.get("title", None),
            "description": tournament.get("description", None),
            "rosters": tournament.get("rosters", None),
            "breakpoints": tournament.get("breakpoints", None),
            "brackets": tournament.get("brackets", None),
            "startDate": tournament.get("startDate", None),
            "endData": tournament.get("endDate", None),
            "leagueId": tournament.get("leagueId", None),
            "gameIds": tournament.get("gameIds", None),
            "league": tournament.get("league", None)
        })
    data = {
        "id": league["id"],
        "name": league["name"],
        "slug": league["slug"],
        "tournamentData": tournamentData
    }
    return data


# Getting all league slugs
with open(leagueSlugsPath, "r") as read_file:
    data = json.load(read_file)
    for league in data:
        print("Saved league data from : " + league["name"])
        leagueData.append(getTournamentData(league))


with open("data/leagueData.json", "w") as write_file:
    json.dump(leagueData, write_file, indent=2)

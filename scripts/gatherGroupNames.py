import os
import sys
import json

groupNames = {}
leagueDataPath = sys.argv[1]
groupNameDataPath = "data/groupNameData.json"


def getTournamentBracketData(tournamentData):
    bracketNameData = []
    for tournament in tournamentData:
        id = tournament.get("id")
        title = tournament.get("title")
        brackets = tournament.get("brackets")
        groupNames = list(map(
            lambda bracketKey: brackets.get(bracketKey).get(
                "groupName"), brackets.keys()
        ))
        bracketNameData.append(
            {"tournamentId": id, "title": title, "groupNames": list(set(groupNames))})
    return bracketNameData


def getGroupNames(data):
    groupNameData = []
    for league in data:
        id, slug, tournamentData = [league[key]
                                    for key in ("id", "slug", "tournamentData")]
        bracketNameData = getTournamentBracketData(tournamentData)
        groupNameData.append({
            "leagueId": id,
            "leagueSlug": slug,
            "tournamentData": bracketNameData
        })
    return groupNameData


with open(leagueDataPath, "r") as read_file:
    data = json.load(read_file)
    groupNames = getGroupNames(data)

with open(groupNameDataPath, "w") as write_file:
    json.dump(groupNames, write_file, indent=2)

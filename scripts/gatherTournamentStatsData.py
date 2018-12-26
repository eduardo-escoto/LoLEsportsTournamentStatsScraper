import os
import sys
import json
import requests

groupNameDataPath = sys.argv[1]
tournamentStatsPath = "data/tournamentStats"
tournametStatsApiUri = "https://api.lolesports.com/api/v2/tournamentPlayerStats"


def createPathString(*data):
    path = ""
    for index, pathStr in enumerate(data, 0):
        strToAppend = pathStr + "/" if index != len(data)-1 else pathStr
        path += strToAppend
    return path


def getStatsByLeague(league):
    for tournament in league["tournamentData"]:
        getTournamentStats(tournament, league["leagueSlug"])


def formatGroupNames(groupNames):
    groupNames.append("")
    groupNames = set(groupNames)
    groupNames = list(filter(None.__ne__, groupNames))
    return groupNames


def getTournamentStats(tournament, leagueSlug):
    tournamentId, title, groupNames = [tournament[key]
                                       for key in ('tournamentId', 'title', 'groupNames')]
    groupNames = formatGroupNames(groupNames)
    for group in groupNames:
        response = requests.get(tournametStatsApiUri, {
                                "tournamentId": tournamentId,
                                "groupName": group}).json()

        group = "tournament_wide" if not group else group

        os.system("mkdir -p " + createPathString(tournamentStatsPath,
                                                 leagueSlug, title, group))
        outputPath = createPathString(tournamentStatsPath, leagueSlug,
                                      title, group, title + "_" + group + ".json")
        response.update({"leagueSlug": leagueSlug, "tournamentId": tournamentId,
                         "title": title, "groupName": group})
        with open(outputPath, "w") as output_file:
            json.dump(response, output_file, indent=2)
            print("Saved data for: " + title + "_" + group)


with open(groupNameDataPath, "r") as read_file:
    data = json.load(read_file)
    for league in data:
        getStatsByLeague(league)

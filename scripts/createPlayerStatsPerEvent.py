import sys
import json
import os


groupNameDataPath = sys.argv[1]
tournamentStatsPath = "data/tournamentStats"
playerStatsPath = "data/playerStats"
globalPlayerData = {}


def getPlayerData(player, tournamentId, title, leagueSlug, groupName):
    stats = []
    name = player.get("name")
    player.update({"tournamentId": tournamentId, "tournamentTitle": title,
                   "leagueSlug": leagueSlug, "groupName": groupName})
    globalPlayerStats = globalPlayerData.get(name)
    if (globalPlayerStats == None):
        stats = [player]
    else:
        stats = globalPlayerStats.get('stats')
        stats.append(player)
    globalPlayerData.update({
        name: {
            "id": player.get("id"),
            "name": player.get("name"),
            "playerSlug": player.get("playerSlug"),
            "stats": stats
        }
    })
    return player


def savePlayerDataTournament(playerData, subdir):
    name = playerData["name"]
    os.system('mkdir -p ' + subdir + '/players')
    with open(subdir+'/players/'+name + '.json', 'w') as player_file:
        json.dump(playerData, player_file, indent=2)


def savePlayerDataCareer():
    os.system('mkdir -p ' + playerStatsPath)
    for player in globalPlayerData.keys():
        pData = globalPlayerData.get(player)
        with open(playerStatsPath + "/" + player + ".json", "w") as player_file:
            json.dump(pData, player_file, indent=2)


def getAllPlayerData(statsData, subdir):
    leagueSlug, tournamentId, title, playerStats, groupName = [
        statsData[key] for key in ('leagueSlug', 'tournamentId', 'title', 'stats', 'groupName')]
    for player in playerStats:
        pData = getPlayerData(player, tournamentId,
                              title, leagueSlug, groupName)
        savePlayerDataTournament(pData, subdir)


def createPlayerStatsFiles(statsFilePath, subdir):
    with open(statsFilePath, "r") as stats_file:
        statsData = json.load(stats_file)
        getAllPlayerData(statsData, subdir)


for subdir, dirs, files in os.walk(tournamentStatsPath):
    for file in files:
        if 'player' not in subdir:
            statsFilePath = os.path.join(subdir, file)
            createPlayerStatsFiles(statsFilePath, subdir)

savePlayerDataCareer()

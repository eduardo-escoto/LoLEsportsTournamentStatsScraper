import sys
import json
import os


groupNameDataPath = sys.argv[1]
tournamentStatsPath = "data/tournamentStats"


def getPlayerData(statsFilePath):
    with open(statsFilePath, "r") as stats_file:
        statsData = json.load(stats_file)


for subdir, dirs, files in os.walk(tournamentStatsPath):
    for file in files:
        statsFilePath = os.path.join(subdir, file)
        getPlayerData(statsFilePath)

# groupNameData = {}
# with open(groupNameDataPath, "r") as read_file:
#     groupNameData = json.load(read_file)

mkdir -p data
mkdir -p data/leagueData
mkdir -p data/tournamentStats

navItemsPath=data/navItems.json
leagueDataPath=data/leagueData.json
leagueSlugsPath=data/leagueSlugs.json
groupNameDataPath=data/groupNameData.json

python scripts/saveNavItems.py $navItemsPath
python scripts/gatherLeagueSlugs.py $navItemsPath $leagueSlugsPath
python scripts/gatherTournamentIds.py $leagueSlugsPath
python scripts/gatherGroupNames.py $leagueDataPath
python scripts/gatherTournamentStatsData.py $groupNameDataPath
python scripts/createPlayerStatsPerEvent.py $groupNameDataPath

# rm -rf data/leagueData
# rm $leagueSlugsPath
# rm $navItemsPath
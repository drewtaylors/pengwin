"""

nba.py - Drew Taylor - 4.27.18

Module which stores all function logic for NBA specific commands.

"""

import urllib.request
import json

# NEED TO STORE IN THIS IN A DB
teams = {
    'Hawks': {'id': '1610612737', 'acronym': 'ATL', 'city': 'Atlanta', 'team': 'Hawks'}, 
    'Nets': {'id': '1610612751', 'acronym': 'BKN', 'city': 'Brooklyn', 'team': 'Nets'}, 
    'Celtics': {'id': '1610612738', 'acronym': 'BOS', 'city': 'Boston', 'team': 'Celtics'}, 
    'Hornets': {'id': '1610612766', 'acronym': 'CHA', 'city': 'Charlotte', 'team': 'Hornets'}, 
    'Bulls': {'id': '1610612741', 'acronym': 'CHI', 'city': 'Chicago', 'team': 'Bulls'}, 
    'Cavaliers': {'id': '1610612739', 'acronym': 'CLE', 'city': 'Cleveland', 'team': 'Cavaliers'}, 
    'Mavericks': {'id': '1610612742', 'acronym': 'DAL', 'city': 'Dallas', 'team': 'Mavericks'}, 
    'Nuggets': {'id': '1610612743', 'acronym': 'DEN', 'city': 'Denver', 'team': 'Nuggets'}, 
    'Pistons': {'id': '1610612765', 'acronym': 'DET', 'city': 'Detroit', 'team': 'Pistons'}, 
    'Warriors': {'id': '1610612744', 'acronym': 'GSW', 'city': 'Golden State', 'team': 'Warriors'}, 
    'Rockets': {'id': '1610612745', 'acronym': 'HOU', 'city': 'Houston', 'team': 'Rockets'}, 
    'Pacers': {'id': '1610612754', 'acronym': 'IND', 'city': 'Indiana', 'team': 'Pacers'}, 
    'Clippers': {'id': '1610612746', 'acronym': 'LAC', 'city': 'L.A.', 'team': 'Clippers'}, 
    'Lakers': {'id': '1610612747', 'acronym': 'LAL', 'city': 'L.A.', 'team': 'Lakers'}, 
    'Grizzlies': {'id': '1610612763', 'acronym': 'MEM', 'city': 'Memphis', 'team': 'Grizzlies'}, 
    'Heat': {'id': '1610612748', 'acronym': 'MIA', 'city': 'Miami', 'team': 'Heat'}, 
    'Bucks': {'id': '1610612749', 'acronym': 'MIL', 'city': 'Milwaukee', 'team': 'Bucks'}, 
    'Timberwolves': {'id': '1610612750', 'acronym': 'MIN', 'city': 'Minnesota', 'team': 'Timberwolves'}, 
    'Pelicans': {'id': '1610612740', 'acronym': 'NOP', 'city': 'New Orleans', 'team': 'Pelicans'}, 
    'Knicks': {'id': '1610612752', 'acronym': 'NYK', 'city': 'New York', 'team': 'Knicks'}, 
    'Thunder': {'id': '1610612760', 'acronym': 'OKC', 'city': 'Oklahoma City', 'team': 'Thunder'}, 
    'Magic': {'id': '1610612753', 'acronym': 'ORL', 'city': 'Orlando', 'team': 'Magic'}, 
    '76ers': {'id': '1610612755', 'acronym': 'PHI', 'city': 'Philadelphia', 'team': '76ers'}, 
    'Suns': {'id': '1610612756', 'acronym': 'PHX', 'city': 'Phoenix', 'team': 'Suns'}, 
    'Blazers': {'id': '1610612757', 'acronym': 'POR', 'city': 'Portland', 'team': 'Trail Blazers'}, 
    'Kings': {'id': '1610612758', 'acronym': 'SAC', 'city': 'Sacramento', 'team': 'Kings'}, 
    'Spurs': {'id': '1610612759', 'acronym': 'SAS', 'city': 'San Antonio', 'team': 'Spurs'}, 
    'Raptors': {'id': '1610612761', 'acronym': 'TOR', 'city': 'Toronto', 'team': 'Raptors'}, 
    'Jazz': {'id': '1610612762', 'acronym': 'UTA', 'city': 'Utah', 'team': 'Jazz'}, 
    'Wizards': {'id': '1610612764', 'acronym': 'WAS', 'city': 'Washington', 'team': 'Wizards'}
}

def current():
    with urllib.request.urlopen("http://data.nba.net/10s/prod/v1/20180427/scoreboard.json") as url:
        data = json.loads(url.read().decode())
        if data is not None:
            for game in data['games']:
                if game['isGameActivated'] == True:
                    print(game['vTeam']['linescore'])
                    print(game['hTeam']['linescore'])
        else:
            return ''
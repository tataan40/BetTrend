from bs4 import BeautifulSoup
import numpy
import pandas
import requests
from datetime import datetime
from attrdict import AttrDict

betclic_nba_url = "https://www.betclic.fr/basket-ball-s4/nba-c13"
nba_teams = ['Atlanta Hawks','Boston Celtics','Brooklyn Nets','Charlotte Hornets','Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks','Denver Nuggets','Detroit Pistons','Golden State Warriors','Houston Rockets','Indiana Pacers','Los Angeles Clippers','Los Angeles Lakers','Memphis Grizzlies','Miami Heat','Milwaukee Bucks','Minnesota Timberwolves','New Orleans Pelicans','New York Knicks','Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers','Phoenix Suns','Portland Trail Blazers','Sacramento Kings','San Antonio Spurs','Toronto Raptors','Utah Jazz','Washington Wizards']
list_nba_teams_data=[]

# Creation of Team Class
class Team:

    data = {}

    def __init__(self, name):
        self.name = name


# To be used only once to initialize teams and data
def initialize(list):
    for i in range (len(nba_teams)):
        team = Team(nba_teams[i])
        list.append(team)
    return list

# Retrieve html from a given url and converts to lxml
def make_soup(url):
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
    except:
        return None
    return BeautifulSoup(html, "lxml")

#
def update_score(Team,soup):
    for i in range(40):
        link_test_name = "ng-tns-c0-{}".format(i)
        team_name = soup.find('span', {"class": link_test_name}).text
        time = datetime.now()
        if team_name[:4] in Team.name:
            link_test_odd = "oddValue ng-tns-c0-{} ng-star-inserted".format(i)
            odd_value = soup.find('span', {"class": link_test_odd}).text
            odd_int_value = int(odd_value)
            Team.data['odd'] = odd_int_value
            Team.data['time'] = time
        else:
            Team.data['odd'] = 0
            Team.data['time'] = time
    return

#Code already used to initialize list of teams
initialize(list_nba_teams_data)
soup = make_soup(betclic_nba_url)
for team in list_nba_teams_data:
    update_score(team,soup)
    print (team.data)
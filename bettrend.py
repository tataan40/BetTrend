from bs4 import BeautifulSoup
import numpy
import pandas
import requests
from datetime import datetime

betclic_nba_url = "https://www.betclic.fr/basket-ball-s4/nba-c13"
nba_teams = ['Atlanta Hawks','Boston Celtics','Brooklyn Nets','Charlotte Hornets','Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks','Denver Nuggets','Detroit Pistons','Golden State Warriors','Houston Rockets','Indiana Pacers','Los Angeles Clippers','Los Angeles Lakers','Memphis Grizzlies','Miami Heat','Milwaukee Bucks','Minnesota Timberwolves','New Orleans Pelicans','New York Knicks','Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers','Phoenix Suns','Portland Trail Blazers','Sacramento Kings','San Antonio Spurs','Toronto Raptors','Utah Jazz','Washington Wizards']


class Team:

    data = numpy.array(3)

    def __init__(self, name):
        self.name = name


def make_soup(url):
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
    except:
        return None
    return BeautifulSoup(html, "lxml")


def update_score(Team,soup):
    for i in range(40):
        link_test_name = "ng-tns-c0-{}".format(i)
        team_name = soup.find('span', {"class": link_test_name}).text
        if team_name[:3] in Team.name:
            link_test_odd = "oddValue ng-tns-c0-{} ng-star-inserted".format(i)
            odd_value = soup.find('span', {"class": link_test_odd}).text
            odd_int_value=int(odd_value)
            time = datetime.now()
            update = numpy.array([odd_int_value,time])
    return update


#soup = make_soup(betclic_nba_url)
#for nba_team in Team.objects.all():
#    new_data = update_score(nba_team)
#    print(new_data)
#    nba_team.odd_variation.append(new_data)
#print('salut')

for i in range (len(nba_teams)):
    team = Team(nba_teams[i])
    print(team.name)


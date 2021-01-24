from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
from datetime import datetime
from attrdict import AttrDict
betclic_nba_url = "https://www.betclic.fr/basket-ball-s4/nba-c13"
nba_teams = ['Atlanta Hawks','Boston Celtics','Brooklyn Nets','Charlotte Hornets','Chicago Bulls','Cleveland Cavaliers','Dallas Mavericks','Denver Nuggets','Detroit Pistons','Golden State Warriors','Houston Rockets','Indiana Pacers','Los Angeles Clippers','Los Angeles Lakers','Memphis Grizzlies','Miami Heat','Milwaukee Bucks','Minnesota Timberwolves','New Orleans Pelicans','New York Knicks','Oklahoma City Thunder','Orlando Magic','Philadelphia 76ers','Phoenix Suns','Portland Trail Blazers','Sacramento Kings','San Antonio Spurs','Toronto Raptors','Utah Jazz','Washington Wizards']
list_nba_teams_data=[]
# Creation of Team Class
class Team:
def __init__(self, name,odd,time):
self.name = name
self.odd = odd
self.time = time

# To be used only once to initialize teams and data
# def initialize(list):
# # for i in range (len(nba_teams)):
# # team = Team(nba_teams[i])
# # list.append(team)
# # return list
# team = Team(nba_teams[i]))

# Retrieve html from a given url and converts to lxml
def make_soup(url):
try:
html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
except:
return None
return BeautifulSoup(html, "lxml")

# Update odd from Betclic and tuple {odd:time} in team.data
def update_odd(Team,soup):
for i in range(40):
link_test_name = "ng-tns-c0-{}".format(i)
time = datetime.now()
# if soup.find('span', {"class": link_test_name}).text[1:4] in Team.name[:3]:
if soup.find('span', {"class": link_test_name}).text[1:4] in Team.name[:3]:
link_test_odd = "oddValue ng-tns-c0-{} ng-star-inserted".format(i)
odd_value = soup.find('span', {"class": link_test_odd}).text
if odd_value != "-":
odd_point_value = odd_value.replace(",",".")
odd_float_value = float(odd_point_value)
# name = Team.name
Team.odd = odd_float_value
Team.time = time
return Team

#Code already used to initialize list of teams
# initialize(list_nba_teams_data)
time = datetime.now()
for x in nba_teams:
list_nba_teams_data.append(Team(name=x,odd=0,time=time))
soup = make_soup(betclic_nba_url)
print(soup)
list_names=[]
list_odds=[]
list_times=[]
for team in list_nba_teams_data:
list_names.append(team.name)
list_odds.append(team.odd)
list_times.append(team.time)
update_odd(team,soup)
list_names.append(team.name)
list_odds.append(team.odd)
list_times.append(team.time)
data_teams=pd.DataFrame({'Team_name':list_names,'odd':list_odds,'time':list_times})
print(data_teams)

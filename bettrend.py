from bs4 import BeautifulSoup
import numpy
import pandas
import requests

betclic_nba_url = "https://www.betclic.fr/basket-ball-s4/nba-c13"
#print(soup)
#nba_teams = ['Ind', 'Hou', 'Phi', 'Was', 'Orl', 'Cle', 'Atl', 'Cha', 'NY', 'Uta', 'Mia', 'Bos', 'Mil', 'Det', 'New', 'Okl', 'Pho', 'Tor', 'Pho', 'Tor', 'Sac', 'Chi', 'Sac', 'Chi', 'Bro', 'Phi', 'Bro', 'Phi', 'Mem', 'Cle', 'Mem', 'Cle', 'Por', 'Min', 'Por', 'Min', 'Den', 'Dal', 'Den', 'Dal']
nba_teams = []
link = "ellipsis"
link_2="oddValue ng-tns-c0-21 ng-star-inserted"



def make_soup(url):
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}).content
    except:
        return None
    return BeautifulSoup(html, "lxml")


def list_teams(list,soup):

    for span in soup.find_all('span',{"class" : link}):
        text = span.text
        text = text.replace('\xa0', ',')
        text=text.split(',',1)[0]
        list.append(text)
        myset=set(list)

    return myset


def update_score(team,soup,list_odds):
    link="betBox_odds betBox_oddsSpecial"
    link1="ellipsis"
    for betbox in soup.find_all('div', {"class": link}):
        if team in betbox.find('span', {"class": link1}).text:
            print("team")
        else:
            print("not working")
        #new_odd = int(new_odd)
        #last_odd = list_odds[-1]
        #list_odds.append(new_odd)
        #return (new_odd/last_odd)


def list_first_odds(list, soup):
    for span in soup.find_all('span', {"class": "odds" }):
        text = span.text
        #text = text.replace('\xa0', ',')
        #text = text.split(',', 1)[0]
        list.append(text)
        # myset=set(list)

    return list


soup = make_soup(betclic_nba_url)
print(soup)
link="betBox_odds betBox_oddsSpecial"
link1="ellipsis"

for betbox in soup.find_all('div', {"class": link}):
    text = betbox.find('span', {"class": link1}).text
    if "Denver" in text:
        print(text)
    else:
        print("not working")


#proper_list_teams = list_teams(nba_teams,soup)
nba_actual_odds = [3]
#evolution = update_score("Denver",soup,nba_actual_odds)
#list_of_odds=list_odds(nba_actual_odds, soup)
#print(evolution)

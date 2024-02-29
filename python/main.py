import requests
from bs4 import BeautifulSoup

from ncaad1xc.table_scraper import get_race_tables, get_athletes
from ncaad1xc.analytics import Race, Performance, Athlete

url    = 'https://www.tfrrs.org/results/xc/16731/NCAA_Division_I_Cross_Country_Championships'
page   = requests.get(url)
soup   = BeautifulSoup(page.content, 'html.parser')
tags   = soup.find_all('a')
tables = soup.find_all('table')

women_table, men_table = get_race_tables(tables)
for table in (women_table, men_table):
    races        = list()
    performances = list()
    athletes     = list()

    athletenames, athleteids, athletelinks = get_athletes(table)
    for name, id, link in zip(athletenames, athleteids, athletelinks):
        athlete = Athlete(name, id, link, list())
        athletes.append(athlete)
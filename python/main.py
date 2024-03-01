import requests
from bs4 import BeautifulSoup
from dateutil import parser

import ncaad1xc.table_scraper as ts
from ncaad1xc.analytics import Race, Performance, Athlete

# First goal is to compile statistics on all athletes from the D1 champs
# Second goal is to use these statistics to correctly predict the championship against
# what actually happened.
# Third goal is to then predict a race using known competitors and distance and 
# predict performance outcomes.

url    = 'https://www.tfrrs.org/results/xc/16731/NCAA_Division_I_Cross_Country_Championships'
page   = requests.get(url)
soup   = BeautifulSoup(page.content, 'html.parser')
tags   = soup.find_all('a')
tables = soup.find_all('table')

women_table, men_table = ts.get_race_tables(tables)
for table in (women_table, men_table):
    races        = list()
    performances = list()
    athletes     = list()

    athletenames, athleteids, athletelinks = ts.get_athletes(table)
    for name, id, link in zip(athletenames, athleteids, athletelinks):
        athlete = Athlete(name, id, link, list())
        athletes.append(athlete)
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        #trackmeets = soup.select('table.table-hover.\>')
        meet_results = soup.find('div', attrs={'id':'meet-results'})
        meets        = meet_results.select('table.table-hover.xc')
        meetnames, meetdates, meetlinks, distances, times, places = ts.get_athlete_xc_meets(meets)

        # Turn the meet data into races
        # Turn the performance data into performances
        # Add these performances to the athlete
                    


                
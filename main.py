import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

import ncaad1xc.table_scraper as ts

# First goal is to compile statistics on all athletes from the D1 champs
# Second goal is to use these statistics to correctly predict the championship against
# what actually happened.
# Third goal is to then predict a race using known competitors and distance and 
# predict performance outcomes.

print("> Starting ncaad1xc program...")

url    = 'https://www.tfrrs.org/results/xc/16731/NCAA_Division_I_Cross_Country_Championships'
page   = requests.get(url)
soup   = BeautifulSoup(page.content, 'html.parser')
tags   = soup.find_all('a')
tables = soup.find_all('table')

print("> Tables collected. Analyzing...")

women_table, men_table = ts.get_race_tables(tables)

df      = pd.DataFrame(columns=["athlete_id", "athlete_name", "athlete_link"])
meetsdf = pd.DataFrame(
    columns=["athlete_id", "meet_name", "meet_date", "meet_link", \
        "meet_distance", "meet_time", "meet_place"])

t = time.time()
athletenames, athleteids, athletelinks = ts.get_athletes(women_table)
for name, id, link in zip(athletenames, athleteids, athletelinks):
    print("> Analyzing athlete {}".format(id))

    df.loc[-1] = [id, name, link]
    df.index = df.index + 1
    df = df.sort_index()

    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    #trackmeets = soup.select('table.table-hover.\>')
    meet_results = soup.find('div', attrs={'id':'meet-results'})
    meets        = meet_results.select('table.table-hover.xc')
    
    meetnames, meetdates, meetlinks, distances, times, places = ts.get_athlete_xc_meets(meets)
    for idx, mname, mdate, mlink, mdistance, mtime, mplace in \
        zip(range(len(meetnames)), meetnames, meetdates, meetlinks, distances, times, places):
        meetsdf.loc[-1] = [id, mname, mdate, mlink, mdistance, mtime, mplace]
        meetsdf.index = meetsdf.index + 1
        meetsdf = meetsdf.sort_index()

df.to_csv("women.csv")
meetsdf.to_csv("women_meets.csv")
t_ = time.time()
print(t_ - t)

    # Turn the meet data into races
    # Turn the performance data into performances
    # Add these performances to the athlete


# for table in men_table:
#     break
                
import bs4
import re

def get_race_tables(tables):
    women_table = None
    men_table = None
    for table in tables:
        table_label = None
        for sibling in table.previous_siblings:
            if type(sibling) == bs4.element.Tag:
                if sibling.has_attr('class'):
                    if sibling['class'] == ['custom-table-title', 'custom-table-title-xc']:
                        for child in sibling.children:
                            if type(child) == bs4.element.Tag and child.name == 'h3':
                                table_label = str(child.text)
                                break
            if table_label != None:
                if 'Women' in table_label and 'Individual' in table_label:
                    women_table = table
                elif 'Men' in table_label and 'Individual' in table_label:
                    men_table = table
                break
    return women_table, men_table

def get_athletes(table):
    athletelinks = list()
    athletenames = list()
    athleteids   = list()
    tags = table.find_all('a')
    athlete_link_checker = re.compile(r'https://www.tfrrs.org/athletes/')
    athlete_id_fetcher   = re.compile(r'https://www.tfrrs.org/athletes/(\d+)/.*')
    for tag in tags:
        if tag.has_key('href'):
            link = tag['href']
            if bool(athlete_link_checker.search(link)):
                athletenames.append(tag.text)
                id = int(athlete_id_fetcher.findall(link)[0])
                athleteids.append(id)
                athletelinks.append(link)
    return athletenames, athleteids, athletelinks
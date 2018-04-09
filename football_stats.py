# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" Assignment 9. """

from bs4 import BeautifulSoup
import urllib

url = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns'
soup = BeautifulSoup(urllib.urlopen(url), "html.parser")
dataTable = soup.find_all('table', class_='data')[0]
players = dataTable.findAll('tr', id=True)

ind = {'player': 0, 'pos': 1, 'team': 2, 'td': 6}
for i, p in enumerate(players[:20]):
    name = p.contents[ind['player']].find_all('a')[0].get_text()
    pos = p.contents[ind['pos']].get_text()
    team = p.contents[ind['team']].find_all('a')[0].get_text()
    td = p.contents[ind['td']].get_text()
    print '{:d} player: {} position: {} team:{} touchdowns: {}'.format(i + 1, name, pos, team, td)

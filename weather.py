# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" Assignment 9. """

from bs4 import BeautifulSoup
import urllib

url = 'https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html'
soup = BeautifulSoup(urllib.urlopen(url), "html5lib")
dataTable = soup.find(id='obsTable')
year = dataTable.find_all('thead')[0].find_all('th')[0].get_text()
days = dataTable.find_all('tbody')
month = days[0].find_all('td')[0].get_text()
print 'Date: {}, {}'.format(month, year)
for day in days[1:]:
    day = day.find_all('td')
    n = day[0].get_text()
    temps = [str(i.get_text()).strip() for i in day[1:4]]
    print '{}. high: {}, avg: {}, low: {}'.format(n, temps[0], temps[1], temps[2])

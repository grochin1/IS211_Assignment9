# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" Assignment 9. """

from bs4 import BeautifulSoup
import urllib

url = 'https://finance.yahoo.com/quote/AAPL/history?ltr=1'
soup = BeautifulSoup(urllib.urlopen(url), "html.parser")
dataTable = soup.find_all('table', {'data-test': 'historical-prices'})[0]
stocks = dataTable.find_all('tbody')[0].find_all('tr')

for stk in stocks:
    date = stk.contents[0].get_text()
    close = stk.contents[min(4, len(stk.contents) - 1)].get_text()
    print 'date: {}  close price: {}'.format(date, close)

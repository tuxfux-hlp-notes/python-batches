content=[]
import urllib2
from bs4 import BeautifulSoup
import re
url = 'http://www.espncricinfo.com/india-v-england-2016-17/engine/match/1034809.html'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

for row in soup.findAll('table')[6].findAll('tr'):
    cols = row.findAll('td')
    cols = [element.text.strip() for element in cols]
    content.append([element for element in cols if element])

    
# finding kohli now :)
for value in content:
    if value:
        if re.search("^V.*Kohli.*","".join(value),re.I):
            print value

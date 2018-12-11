# Scraping used camry prices from autotrader, ebay, etc

# 2011 Toyota Camry LE 61000mi. Standard Equipment

import csv
import requests
from BeautifulSoup import BeautifulSoup

ebayurl = 'https://www.ebay.com/sch/Cars-Trucks/6001/i.html?_from=R40&_fosrp=1&_dcat=6001&_dmpt=US_Cars_Trucks&makeval=Toyota&modelval=Camry&Model%2520Year=2011&_sadis=200&_mtrvfc=1&_fspt=1&_stpos=07645&_nkw=Toyota%20Camry&LH_PrefLoc=99'
response = requests.get(ebayurl)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('ul', attrs={'id': 'ListViewInner'})

list_of_rows = []
for row in table.findAll('li'):
    list_of_cells = []
    for cell in row.findAll('h3'):
        text = cell.text
        list_of_cells.append(text)
    for cell in row.findAll('ul'):
        text = cell.text
        list_of_cells.append(text)
    if list_of_cells == []:
        print('blank row')
    else:
        list_of_rows.append(list_of_cells)

outfile = open("./ebay.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(['Title', 'Price', 'Details'])
writer.writerows(list_of_rows)

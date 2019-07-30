import requests
import urllib.request
import time
from bs4 import BeautifulSoup
url = "https://www.starcar.de/specials/kostenlos-mieten/"
response = requests.get(url) #200 means it went through
# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

soup.findAll('p')

pickup_locations = soup.find_all('p', attrs={'class': 'bold uppercase'})
pickup_locations = [x.text.strip() for x in pickup_locations]

la = [x.parent.text.splitlines() for x in pickup_locations]

string_length = [len(x) for x in la]

indices = [i for i, x in enumerate(string_length) if x == 8]

select = [la[x] for x in indices]


def Extract(lst, index):
    return [item[index] for item in lst]

return_locations = Extract(select, index = -1)
pickup_locations = Extract(select, index = 5)

pickup_hamburg = [i for i, x in enumerate(pickup_locations) if 'HH' in x]
pickup_berlin = [i for i, x in enumerate(pickup_locations) if 'Berlin' in x]

select[pickup_berlin[6]]


import itertools
for a, b in itertools.combinations(select, 2):
    print(a == b)

la = soup.findAll('i', attrs={'class': 'fa fa-angle-double-down'})

len(pickup_locations)

len('uppercase')

return_locations = soup.find_all('p', attrs={'class': 'uppercase'})
# remove other uppercase classes:
return_locations


x.parent.text.parent.text

for x in return_locations:
    if '<p class='uppercase'>' in x:
        print(x)


return_locations = [x.text.strip() for x in return_locations]

len(return_locations)

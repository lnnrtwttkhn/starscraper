import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import html2text
import markdown
import html5lib

def download_html(URL):
    import requests
    response = requests.get(URL)
    if response.status_code == 200:
        print('download successful!')
    return(response)

URL = "https://www.starcar.de/specials/kostenlos-mieten/"
response = download_html(URL)

# parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")



def get_pickup_locations(soup):
    pickup_locations = soup.find_all('p', attrs={'class': 'bold uppercase'})
    pickup_locations = [x.text.strip() for x in pickup_locations]
    return(pickup_locations)

pickup = get_pickup_locations(soup)

def check_alphabetical_order(word_list, index = 0):
    alphabet = [True] * len(word_list)
    for i in range(len(word_list) - 1):
        if word_list[i][index] <= word_list[i + 1][index]:
            alphabet[i] = False
    return(alphabet)

def filter_locations(location_list):
    alphabet = check_alphabetical_order(word_list=location_list)
    indices = [i for i, x in enumerate(alphabet) if x]
    locations_filtered = location_list[:indices[0]]
    return(locations_filtered)






soup.findAll('p')



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

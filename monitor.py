import requests
import json
from bs4 import BeautifulSoup
import randomheaders

# URL and stuff
URL = 'https://www.nike.com/de/launch?s=upcoming'
ua = randomheaders.LoadHeader()
headers = { 'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.13) Gecko/20060501 Epiphany/2.14', 'referer': 'https://www.nike.com/de/launch' }

# Monitor
def monitor():
    r = requests.get(URL, headers=headers).text
    res = BeautifulSoup(r, 'lxml')

    # URLGEN

    for hrefs in res.find_all('figure', class_='pb2-sm'):
        a = hrefs.find('a')
        print('https://www.nike.com/' + a.get('href'))

monitor()
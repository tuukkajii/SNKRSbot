import requests
import json
from bs4 import BeautifulSoup
import randomheaders
import threading

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
        h6 = hrefs.find('h6')
        h3 = hrefs.find('h3')

        #print(h3)

        print(h3.text + '- ' + h6.text, ': ', 'https://www.nike.com' + a.get('href'))

monitor()
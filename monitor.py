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

    for hrefs in res.find_all('figure', class_='pb2-sm va-sm-t ncss-col-sm-12 ncss-col-md-6 ncss-col-lg-4 pb4-md '
                                                    'prl0-sm prl2-md ncss-col-sm-6 ncss-col-lg-3 pb4-md prl2-md '
                                                    'pl0-md pr1-md d-sm-h d-md-ib'):
        print(hrefs.get('href'))
    #print(res)
monitor()

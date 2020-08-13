import requests
import json
from bs4 import BeautifulSoup
import randomheaders
import threading

proxies = {
    'https':  'http://142.93.130.169:8118',
    'https': 'http://52.179.18.244:8080',
    'https': 'http://80.78.237.2:55443',
    'https': 'http://95.179.178.172:8080',
    'https': 'http://46.218.155.194:3128',
    'https': 'http://198.98.58.178:8080',
    'https': 'http://169.57.1.84:25',
    'https': 'http://205.185.115.100:8080',
    'https': 'http://77.247.94.131:48602',
    'https': 'http://144.217.101.245:3129',
    'https': 'http://212.66.61.118:37141',
    'https': 'http://169.57.1.84:80',
    'https': 'http://169.57.1.85:25',
    'https': 'http://159.8.114.34:8123',
    'https': 'http://104.244.77.254:8080',
    'https': 'http://51.255.103.170:3129',
    'https': 'http://124.41.213.122:45871',
    'https': 'http://185.184.208.187:5836',
    'https': 'http://185.184.243.198:5836',
    'https': 'http://198.98.59.87:8080',
    'https': 'http://173.192.128.238:8123',
    'https': 'http://85.175.99.136:8080',
    'https': 'http://185.184.243.212:5836',
    'https': 'http://173.192.128.238:25',
    'https': 'http://173.82.17.188:5836',
    'https': 'http://159.8.114.37:80',
    'https': 'http://51.77.61.152:3128',
    'https': 'http://201.249.190.235:3128',
    'https': 'http://51.77.35.134:3128',
    'https': 'http://51.77.61.153:3128',
    'https': 'http://81.201.60.130:80',
    'https': 'http://87.197.156.62:23500',
    'https': 'http://187.130.75.77:3128',
    'https': 'http://145.239.121.218:3129',
    'https': 'http://50.249.79.18:8080',
    'https': 'http://119.81.71.27:25',
    'https': 'http://110.44.128.200:3128',
    'https': 'http://125.99.100.193:40390',
    'https': 'http://159.203.44.177:3128',
    'https': 'http://51.38.155.117:3128',
    'https': 'http://169.57.157.148:25',
    'https': 'http://169.57.157.148:8123',
    'https': 'http://185.114.137.14:12451',
    'https': 'http://193.169.20.102:5836',
}

# URL and stuff
URL = 'https://www.nike.com/de/launch?s=upcoming'
ua = randomheaders.LoadHeader()
headers = { 'user-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.13) Gecko/20060501 Epiphany/2.14', 'referer': 'https://www.nike.com/de/launch' }

# Monitor
def monitor():
    r = requests.get(URL, headers=headers, cookies=proxies).text
    res = BeautifulSoup(r, 'lxml')
    # URLGEN

    for hrefs in res.find_all('figure', class_='pb2-sm'):
        a = hrefs.find('a')
        h6 = hrefs.find('h6')
        h3 = hrefs.find('h3')

        print(h3.text + '- ' + h6.text, ': ', 'https://www.nike.com' + a.get('href'))
        threading.Timer(5.0, monitor).start()


monitor()
print('\n')
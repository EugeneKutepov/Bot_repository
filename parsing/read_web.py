import pandas as pd
import requests
from random import choice
from bs4 import BeautifulSoup

#url = "https://www.vsegei.ru/ru/public/sprav/geodictionary/"
#url = 'https://www.kinopoisk.ru/lists/top250/'

# tables = pd.read_html(url)
#
# print(tables)

# делаем запрос и получаем html
#html_text = requests.get(url).text

# используем парсер lxml
#soup = BeautifulSoup(html_text, 'lxml')

url = 'http://httpbin.org/ip'

# while line := open('user_agent.txt').read().split('\n'):
#     user_agent = {'user-agent': choice(line)}
#     response = requests.get(url=url, headers=user_agent)
with open('filter_proxy.txt') as file:
    proxy_file = file.read().split('\n')
    for _ in range(1000):
        try:
            ip = choice(proxy_file).strip()
            proxy = {
                'http': f'http://{ip}',
                'https': f'http://{ip}'
            }
            response = requests.get(url=url, proxies=proxy)
            print(response.json(), 'Success connection')
        except Exception as _ex:
            continue
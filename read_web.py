import pandas as pd
import requests
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

from random import choice

url = 'http://httpbin.org/user-agent'

# while line := open('user_agent.txt').read().split('\n'):
#     user_agent = {'user-agent': choice(line)}
#     response = requests.get(url=url, headers=user_agent)

from fake_useragent import UserAgent
ua = UserAgent()

for x in range(10):
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=url, headers=fake_ua)
    print(response.text)
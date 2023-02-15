import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.vsegei.ru/ru/public/sprav/geodictionary/"
tables = pd.read_html(url)

print(tables)

# # делаем запрос и получаем html
# html_text = requests.get(url).text
#
# # используем парсер lxml
# soup = BeautifulSoup(html_text, 'lxml')
#
# print(soup)
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

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
}

response = requests.get(url='http://httpbin.org/user-agent', headers=headers)
print(response.text)
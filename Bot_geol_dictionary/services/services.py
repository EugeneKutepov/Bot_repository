from random import choice
import requests
from bs4 import BeautifulSoup

line = open('user_agent.txt').read().split('\n')
user_agent = {'user-agent': choice(line)}

def read_direct_link(link:str):
    print(link)

    url = f'https://www.vsegei.ru/ru/public/sprav/geodictionary/{link}'
    #print(url)
    html_text = requests.get(url, headers=user_agent).text
    soup = BeautifulSoup(html_text, 'lxml')
    search_in = soup.find_all('p', align='justify')
    #print(search_in)
    for element in (search_in):
        #hrefs = str(element).split('"')
        #print(hrefs)
        # wrref = {}
        # for i in range(len(hrefs)):
        #     if 'ELEMENT_ID' in hrefs[i]:
        #         word = hrefs[i+1].split('><')[1][2:-3]
        #         wrref[word] = f'https://www.vsegei.ru{hrefs[i]}'
        return element.text
        # print(element)
        # print(wrref)
        # print(element.text)

def parse_term(term):
    url = f'https://www.vsegei.ru/ru/public/sprav/geodictionary/geosearch.php?q={term}&s=Поиск'
    html_text = requests.get(url, headers=user_agent).text
    soup = BeautifulSoup(html_text, 'lxml')
    search_in = soup.find_all('a', target='_blank', href=True)
    links={}
    for element in (list(search_in)):
        if 'ELEMENT_ID' in element['href']:
            # read_direct_link(element['href'])
            # print(element['href'], element.text)
            links[element.text] = element['href']
    print(links)
    return links


if __name__ == '__main__':
    print(parse_term('Конус выноса'))
    #print(read_direct_link('article.php?ELEMENT_ID=85931'))
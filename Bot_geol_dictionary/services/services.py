from random import choice
import requests
from bs4 import BeautifulSoup

line = open('user_agent.txt').read().split('\n')
user_agent = {'user-agent': choice(line)}

def _get_part_text(text: str, start: int, size = 4096) -> tuple[str, int]:
    symbols = ",.!;:?"
    if text and len(text)-1-start>size:
        text_edit = text[start:start+size]
        for i in range(len(text_edit)-1, 0, -1):
            if text_edit[i] in symbols:
                try:
                    if text[start+i+1] in symbols:
                        i-=1
                        pass
                    else:
                        text_edit = text_edit[:i+1]
                        return text_edit, len(text_edit)
                except IndexError:
                    text_edit = text[start:len(text)]
                    return text_edit, len(text_edit)
    else:
        return text[start:len(text)-1], len(text[start:len(text)-1])


# Функция, формирующая словарь книги
def prepare_message(text: str):
    position = 0
    norm_mes = []
    while position < len(text)-1:
        page = _get_part_text(text, position)
        position += int(page[1])
        norm_mes.append(page[0].lstrip())
    return norm_mes

def read_direct_link(link:str):
    url = f'https://www.vsegei.ru/ru/public/sprav/geodictionary/{link}'
    #print(url)
    html_text = requests.get(url, headers=user_agent).text
    soup = BeautifulSoup(html_text, 'lxml')
    search_in = soup.find_all('tbody')
    print(type(search_in))
    #print(search_in)
    for element in (search_in):
        text = element.text.replace('\n\n\n\n', '')
        print(text)
            #hrefs = str(element).split('"')
            #print(hrefs)
            # wrref = {}
            # for i in range(len(hrefs)):
            #     if 'ELEMENT_ID' in hrefs[i]:
            #         word = hrefs[i+1].split('><')[1][2:-3]
            #         wrref[word] = f'https://www.vsegei.ru{hrefs[i]}'

        return prepare_message(text)
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
    #print(links)
    return links


if __name__ == '__main__':
    print(parse_term('Конус выноса'))
    #print(read_direct_link('article.php?ELEMENT_ID=85931'))
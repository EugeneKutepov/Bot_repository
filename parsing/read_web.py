import pandas as pd
import requests


#url = 'http://httpbin.org/ip'
for i in range(1, 161):
    response = requests.get(url=f'https://parsinger.ru/img_download/img/ready/{i}.png')
    with open(f'img/image{i}.jpeg', 'wb') as file:
        file.write(response.content)
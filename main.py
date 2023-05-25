import requests
from bs4 import BeautifulSoup
response = requests.get('https://uk.wikipedia.org/')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    img = soup.find_all('img')#Список
    for i in img:
        print('https://' + i['src'])

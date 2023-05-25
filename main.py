import  requests
from bs4 import BeautifulSoup
response = requests.get('https://weather.com/uk-UA/weather/'
                        'today/l/2261b41a35498e667410cb84dfb'
                        '95d455f977b64d2c02b673df410b7d9ec31ed')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features= "html.parser")
    city = soup.find('h1',{"class":"CurrentConditions--location--1YWj_"})
    weather = soup.find('span')
    if city:
        city_name = city.text.strip()
        weather = weather.text.strip()
        print(city_name)
        print(f'Температура - {weather}')
    else:
        print('Місто не знайдено ')
except:
    print('Немає підключння')
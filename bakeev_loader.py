from datetime import date
import re
import requests
from bs4 import BeautifulSoup


decimal = r'[0-9]*\.[0-9]*'
integer = r'[0-9]*'
price_regex = r'[0-9]* [0-9][0-9][0-9] [0-9][0-9][0-9]'

URL = "http://bakeevopark.ru/selection/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
apts = soup.find_all("div", class_="flat-item row hidden-xs hidden-sm")


def extract_data(apt_data):
    flat_num_building_data = apt_data.find("p",class_="flat-location").text.strip()
    building, flat_num = [x for x in re.findall(integer, flat_num_building_data) if x]
    floor = ...
    area_rooms_data = apt_data.find('div', class_='configurator-title hidden-xs hidden-sm').text.strip()
    area = re.findall(decimal, area_rooms_data)[0]
    rooms = [x for x in re.findall(integer, area_rooms_data) if x][0]
    price_data = apt_data.find('div', class_='flat-item-right-extra-price').text.strip()
    price = re.findall(price_regex, price_data)[0]
    sprice = round(float(price.replace(' ', ''))/float(area), 2)
    status = 'В продаже'
    updated = date.today()
    return f'flat num {flat_num}\nbuilding {building}\narea {area}\nrooms {rooms}\nprice {price}\ns price {sprice}\n{updated}\n'

print(extract_data(apts[0]))

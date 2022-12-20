from datetime import date
import requests
from bs4 import BeautifulSoup


flats_sold = []
flats_booked = []
flats_onsale = []


def get_sold_data():
    URL_sold = 'https://2.ac-biryuzovaya-zhemchuzhina.ru/flats/all?floor=&type=&status=4&minArea=&maxArea=&minPrice=&maxPrice='
    page_sold = requests.get(URL_sold)
    soup_sold = BeautifulSoup(page_sold.content, "html.parser")
    apts_sold = soup_sold.find('tbody')
    return parse_data(apts_sold.text, 'sold')


def get_onsale_data():
    URL_onsale = "https://2.ac-biryuzovaya-zhemchuzhina.ru/flats/all?floor=&type=&status=2&minArea=&maxArea=&minPrice=&maxPrice="
    page_onsale = requests.get(URL_onsale)
    soup_onsale = BeautifulSoup(page_onsale.content, "html.parser")
    apts_onsale = soup_onsale.find('tbody')
    return parse_data(apts_onsale.text, 'onsale')


def get_booked_data():
    URL_booked = 'https://2.ac-biryuzovaya-zhemchuzhina.ru/flats/all?floor=&type=&status=3&minArea=&maxArea=&minPrice=&maxPrice='
    page_booked = requests.get(URL_booked)
    soup_booked = BeautifulSoup(page_booked.content, "html.parser")
    apts_booked = soup_booked.find('tbody')
    return parse_data(apts_booked.text, 'booked')


def parse_data(data, status):
    result = []
    data = [x for x in data.split('\n') if x]
    if status == 'onsale':
        for i in range(0, len(data), 9):
            apt = {}
            apt['rooms'], apt['area'], apt['price'], apt['status'], apt['floor'], apt['number'], a, b, c = data[i:i+9]
            result.append(apt)
    else:
        for i in range(0, len(data), 8):
            apt = {}
            apt['rooms'], apt['area'], apt['status'], apt['floor'], apt['number'], a, b, c = data[i:i + 8]
            result.append(apt)
    return result

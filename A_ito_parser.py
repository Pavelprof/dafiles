import requests
from bs4 import BeautifulSoup
import pandas as pd

# item = '8250u'
# url = f'https://www.avito.ru/moskva/noutbuki?f=ASgCAQECAUCo5A1E0Nlm1NlmwNlmttlmAUXGmgwZeyJmcm9tIjoxMjgwMCwidG8iOjMzNzAwfQ&geoCoords=55.715297%2C37.564529&q={item}+-%D0%B7%D0%B0%D0%BF%D1%87%D0%B0%D1%81%D1%82%D0%B8+-ddr3+-%2215.6%22&radius=25&searchRadius=25&user=1'



url = 'https://www.avito.ru'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

file_path = r'C:\Users\Павел\Desktop\page3.html'

# Записать содержимое страницы в файл
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(response.text)

# html = '<span class="page-title-count-wQ7pG" data-marker="page-title/count">41</span>'
#
# # Создаем объект BeautifulSoup и передаем HTML код
# soup = BeautifulSoup(html, 'html.parser')
#
# # Используем метод find() для поиска элемента по классу
# element = soup.find('span', class_='page-title-count-wQ7pG')
#
# # Получаем текст из найденного элемента
# number = element.text
#
# print(number)  # Выводит: 41
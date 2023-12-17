import sys
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

try:
    lien = input("Enter website: ")
    link = f'https://www.{lien}/'
    page = requests.get(link)
except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print("Error occurs on : ", url)
    print(error_type, 'Line: ', error_info.tb_lineno)

time.sleep(2)
soup = BeautifulSoup(page.text, 'html.parser')
links = soup.find_all('div', attrs={'class':'cb-nws-intr'})

for i in links:
    print(i.text)
    print('\n')
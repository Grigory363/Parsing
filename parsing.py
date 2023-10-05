import random
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
import lxml

# url = "https://www.globus.ru/catalog/chay-kofe-kakao/kofe/"
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text

# with open ("index.html", "w") as file:
#     file.write(src)

with open ("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
cofee_href = soup.find(class_="pim-list__item pim-list__item--standart ga-event")
# cofee_text = soup.find_all("div", class_="pim-list__item-title js-crop-text") # рабочий вариант
# for i in cofee_text: # Рабочий вариант
#      i_text = i.text # Рабочий вариант
#      print(i_text) # Рабочий вариант
for item in cofee_href:
    item_text = item.find("div", class_="pim-list__item-content").text()
    # item_href = "https://www.globus.ru" + item.get("href")
    print(item_text)

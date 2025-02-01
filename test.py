from bs4 import BeautifulSoup
import requests
import re
import time

url = "https://rocket.com/homes/places/ca/berkeley"
page = requests.get(url).text
time.sleep()
doc = BeautifulSoup(page, "html.parser")
print(doc)
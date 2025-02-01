from bs4 import BeautifulSoup
import requests
import re


number = 1
decision = {}
address = input("Which location interests you? ")
url = f"https://rocket.com/homes/places/ca/{address}"
page = requests.get(url).text  # timeout in seconds
doc = BeautifulSoup(page, "html.parser")
print(doc)
page = doc.findAll(class_="p4 mr-4 inline-block h-[26px] w-[26px] text-center leading-[24px]")
for x in page[-1:]:
    a_tag = x.find("a")
    if a_tag:  # Ensure the 'a' tag exists
        page_number = a_tag.text
    else:
        page_number = 1


while number <= int(page_number):
    url = f"https://rocket.com/homes/places/ca/{gpu}/?page={number}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    prices = doc.findAll(class_="flex items-center")
       
    for price in prices:
            name = price.parent.next_sibling.next_sibling
            a_tag = name.find("a")
            if a_tag:  # Ensure the 'a' tag exists
                list = a_tag.get("aria-label")
                list = str(list.split(" ", 3)[3:])
                href_value = a_tag.get("href")
                href_value = "https://rocket.com" + href_value
                
 
            price_text = price.get_text(strip=True) 
            decision[list] = {"price": int(price_text.replace("$", "").replace(",", "")), "link": href_value}

    number +=1


sorted_items = sorted(decision.items(), key = lambda x: x[1]['price'])

for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("------------------------------------")







        



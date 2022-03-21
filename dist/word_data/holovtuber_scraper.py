# -*- coding: UTF-8 -*- 

import json
from bs4 import BeautifulSoup
import requests

response = requests.get("https://virtualyoutuber.fandom.com/wiki/Hololive")

root = BeautifulSoup(response.text, "html.parser")

def remove_special_char(string):
    string = string.replace(" ", "")
    string = string.replace("&", "")
    string = string.replace("‧", "")      
    string = string.replace("·", "")
    string = string.replace("．", "")
    string = string.replace(".", "")
    string = string.replace("-", "")
    string = string.replace("!", "")
    string = string.replace("_", "")
    string = string.replace("・", "")
    string = string.replace("\n", "")
    string = string.replace("+", "plus")
    string = string.replace("'", "")
    
    return string

channel_name = root.find_all("th", attrs = {'style': 'padding: 5px; width:70px; text-align:center'})

data = []

for el in channel_name:
    if el.text == "Motoaki TanigoCOVER CEO\n":
        break
    data.append(remove_special_char(el.text))

data = list(set(data))

sorted_data = sorted(data, key = lambda k: (len(k), k))

with open("./hololive_vtuber.json", "w", encoding = "utf8") as f:
    json.dump(sorted_data, f, indent = 4, ensure_ascii = False)
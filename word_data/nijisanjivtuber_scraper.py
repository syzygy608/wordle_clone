# -*- coding: UTF-8 -*- 

import json
from bs4 import BeautifulSoup
import requests

response = requests.get("https://en.everybodywiki.com/Nijisanji")

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
''
parents = root.find_all("ul")

data = []

for parent in parents:
    children = parent.find_all("li")
    for el in children:
        if "(retired)" not in el.text and "(suspended)" not in el.text:
            data.append(remove_special_char(el.text))
        elif "Yugo Asuma" in el.text:
            break

data = list(set(data))
sorted_data = sorted(data, key = lambda k: (len(k), k))
print(sorted_data)


# with open("./hololive_vtuber.json", "w", encoding = "utf8") as f:
#     json.dump(sorted_data, f, indent = 4, ensure_ascii = False)
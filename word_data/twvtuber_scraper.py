# -*- coding: UTF-8 -*- 

import json
from logging.config import stopListening
from bs4 import BeautifulSoup
import requests

response = requests.get("https://taiwanvtuberdata.github.io/all/CombinedCount.html")

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
    
    return string

channel = root.find_all("tr")
data = []
for row in channel:
    col = row.find_all("td")
    if len(col) == 5 and col[4].text == "TW":
        if col[1].text != "已停止活動":
            if int(eval(col[1].text)) >= 5000:
                if "官方" not in col[0].text:
                    data.append(col[0].text)

for i in range(len(data)):
    data[i] = remove_special_char(data[i])

sorted_data = sorted(data, key = lambda k: (len(k), k))

with open("./twvtuber.json", "w", encoding = "utf8") as f:
    json.dump(sorted_data, f, indent = 4, ensure_ascii = False)
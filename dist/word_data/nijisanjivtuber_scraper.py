# -*- coding: UTF-8 -*- 

import json
from bs4 import BeautifulSoup
import requests

response = requests.get("https://zh.wikipedia.org/wiki/彩虹社")

root = BeautifulSoup(response.text, "html.parser")

def remove_special_char(string):
    string = string.replace(" ", "")
    string = string.replace("&", "")
    string = string.replace("‧", "")      
    string = string.replace("·", "")
    string = string.replace("．", "")
    string = string.replace(".", "")
    string = string.replace("-", "")
    string = string.replace("・", "")
    string = string.replace("\n", "")
    string = string.replace("★", "")
    string = string.replace("(バーチャルYouTuber)", "")
    return string

parents = root.find_all("table", class_ = "nowraplinks navbox-subgroup", attrs = {'style': 'border-spacing:0'})

raw_data = []

for parent in parents:
    children = parent.find_all("li")
    if children != None:
        for el in children:
            raw_data.append(el.text)

nijisanji_data = []
flag = False
for el in raw_data:
    if el == "月之美兔":
        flag = True
    if el == "海夜叉神":
        flag = False
    if flag:
        nijisanji_data.append(el)
    
for i in range(len(nijisanji_data)):
    if "日语" in nijisanji_data[i]:
        nijisanji_data[i] = nijisanji_data[i].split("：")[1].replace("）", "")
        nijisanji_data[i] = remove_special_char(nijisanji_data[i])
        
sorted_data = sorted(nijisanji_data, key = lambda k: (len(k), k))

with open("./nijisanji_vtuber.json", "w", encoding = "utf8") as f:
    json.dump(sorted_data, f, indent = 4, ensure_ascii = False)
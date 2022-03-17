import json

def isEnglish(s):
    return s.isascii()

with open("twvtuber.json", "r", encoding = 'utf8') as f:
    data = json.load(f)

en_vtuber = []
other_vtuber = []

for i in data:
    if isEnglish(i):
        en_vtuber.append(i)
    else:
        other_vtuber.append(i)

with open("hololive_vtuber.json", "r", encoding = 'utf8') as f:
    data = json.load(f)

for i in data:
    if isEnglish(i):
        en_vtuber.append(i)
    else:
        other_vtuber.append(i)

finish_data = {"en" : en_vtuber, "other": other_vtuber}

with open("./vtuber_final.json", "w", encoding = "utf8") as f:
    json.dump(finish_data, f, indent = 4, ensure_ascii = False)

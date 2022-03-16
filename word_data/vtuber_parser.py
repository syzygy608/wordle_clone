import json

f = open("vtuber_raw.txt")
raw_words = f.readlines()
for i in range(len(raw_words)):
    raw_words[i] = raw_words[i].strip().replace(" ", "")

sorted_words = sorted(raw_words, key = lambda k: (len(k), k))

data = []
for i in sorted_words:
    data.append(i)

f.close()

with open("vtuber.json", "w") as f:
    json.dump(data, f, indent = 4)
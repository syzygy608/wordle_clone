import json

f = open("vtuber_raw.txt")
raw_words = f.readlines()
for i in range(len(raw_words)):
    raw_words[i] = raw_words[i].strip().replace(" ", "")

sorted_words = sorted(raw_words, key = lambda k: (len(k), k))

data = {4: []}
length = 4
for i in sorted_words:
    if len(i) == length:
        data[length].append(i)
    elif len(i) > length:
        length = len(i)
        data[length] = []
        data[length].append(i)

f.close()

with open("vtuber.json", "w") as f:
    json.dump(data, f, indent = 4)
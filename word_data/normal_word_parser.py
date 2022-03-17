import json

f = open("words_raw.txt")
raw_words = f.readlines()
for i in range(len(raw_words)):
    raw_words[i] = raw_words[i].strip()

sorted_words = sorted(raw_words, key = lambda k: (len(k), k))

data = {5: []}
length = 5
for i in sorted_words:
    if len(i) == length:
        data[length].append(i)
    elif len(i) > length:
        if length > 14:
            break
        length = len(i)
        data[length] = []
        data[length].append(i)

f.close()

with open("words.json", "w") as f:
    json.dump(data, f, indent = 4)
import eel
import json 
import random

with open('./word_data/words.json') as f:
    data = json.load(f)

with open('./word_data/vtuber.json') as v:
    v_data = json.load(v)

def xss_protect(string):
    string = string.replace("<", "")
    string = string.replace("&", "")
    string = string.replace("<", "")
    string = string.replace(":", "")
    string = string.replace("(", "")
    string = string.replace("\"", "")
    string = string.replace("'", "")
    string = string.replace(">", "")
    string = string.replace("\\", "")

@eel.expose
def select_voc(length):
    ans_voc = random.choice(data[str(length)])
    print("Answer for this round is:", ans_voc)
    return ans_voc

@eel.expose
def check_input_if_valid(input, ans_voc):
    xss_protect(input)
    if str(input).isalpha():
        if len(input) == len(ans_voc):
            return 1
        else:
            return 0
    else:
        return -1

@eel.expose
def check_used(input, chararr):
    chararr = list(chararr)
    return input in chararr

@eel.expose
def check_input_if_indict(input):
    return str(input) in data[str(len(input))]

@eel.expose
def check_ans(input, ans_voc):
    status = []
    ans_voc = list(ans_voc)
    for i in range(len(input)):
        if input[i] == ans_voc[i]:
            status.append(1)
        elif input[i] in ans_voc and ans_voc.index(input[i]) > i:
            status.append(0)
        else:
            status.append(-1)
    return status

eel.init('web')
eel.start('index.html', size = (1200, 700))
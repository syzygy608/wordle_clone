import eel
import json 
import random


with open('./word_data/words.json') as f:
    data = json.load(f)

with open('./word_data/vtuber_final.json', encoding = 'utf8') as v:
    v_data = json.load(v)

# string replacement for simple xss protection
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

# random choose word
@eel.expose #decorator for js import
def select_voc(type, length):
    if int(type) == 1:  
        ans_voc = random.choice(data[str(length)])
    else:
        language = ["en", "other"]
        ans_voc = random.choice(v_data[language[random.randint(0, 1)]])
    print("Answer for this round is:", ans_voc)
    return ans_voc

@eel.expose()
def check_vtuber_name_type(name):
    if name in v_data["en"]:
        return "該名vtuber名稱為英文或羅馬拼音，<br>請輸入英文字元"
    else:
        return "該名vtuber名稱為中文或日文，<br>請輸入日文或漢字或中文"

@eel.expose
def check_name_if_valid(input, ans_voc):
    xss_protect(input)
    if len(input) == len(ans_voc):
        return 1
    else:
        return 0

@eel.expose
def check_input_if_valid(input, ans_voc):
    xss_protect(input)
    if str(input).isalpha(): #check if all chars are alphabet
        if len(input) == len(ans_voc):
            return 1
        else:
            return 0
    else:
        return -1

@eel.expose
def check_input_if_indict(input):
    return str(input).lower() in data[str(len(input))]

@eel.expose
def check_ans(input, ans_voc):
    status = []
    check = []
    ans_voc = ans_voc.lower()
    ans_voc = list(ans_voc)
    input = input.lower()
    for i in range(len(input)):
        if input[i] == ans_voc[i]:
            status.append(1)
        elif input[i] not in ans_voc:
            status.append(-1)
            check.append(ans_voc[i])
        else:
            status.append(0)
            check.append(ans_voc[i])
    for i in range(len(status)):
        if status[i] == 0:
            if input[i] in check:
                check.remove(input[i])
                status[i] = 0
            else:
                status[i] = -1
    return status

@eel.expose
def return_result_copy(table):
    table = list(table)
    result = ""
    for i in range(len(table)):
        flag = 0
        for j in range(len(table[i])):
            if table[i][j] == -2:
                flag = 1
                break
            elif table[i][j] == -1:
                result += "🖤"
            elif table[i][j] == 1:
                result +=  "💚"
            else:
                result += "🧡"
        result += "\n"
        if flag == 1:
            break
    cnt = result.count('\n')
    result += f"Vordle win in {cnt - 1} / {len(table)} Games\n"
    return result

eel.init('web')
eel.start('index.html', mode = 'chrome', host = 'localhost')

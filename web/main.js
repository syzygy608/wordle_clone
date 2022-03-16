var ans_word = JSON.parse(localStorage.used);
var guessing_times = JSON.parse(localStorage.times);

async function sleep(ms = 0)
{
    return new Promise(r => setTimeout(r, ms));
}

async function guessing()
{
    var guess = document.getElementById("guessword").value;
    document.getElementById("guessword").value = '';
    var valid = await eel.check_input_if_valid(guess, ans_word)();
    if(valid === 0)
    {
        alert("輸入的單字長度不符合或者為空，請重新輸入!");
        document.getElementById("guessword").value = '';
        return;
    }
    else if(valid === -1)
    {
        alert("輸入的單字有非法字元，請重新輸入!");
        document.getElementById("guessword").value = '';
        return;
    }
    var indict = await eel.check_input_if_indict(guess)();
    if(!indict)
    {
        alert("該字串並不在單字庫內，請重新輸入!");
        document.getElementById("guessword").value = '';
        return;
    }
    var ifans = await eel.check_ans(guess, ans_word)();
    var table = document.getElementById("gametable").rows;
    var row = table[table.length - guessing_times];
    var corrects = 0;
    for(let i = 0; i < guess.length; ++i)
    {
        row.cells[i].textContent = guess[i];
        if(ifans[i] == 1)
        {
            corrects++;
            row.cells[i].className = 'correct';
        }
        else if(ifans[i] == 0)
            row.cells[i].className = 'used';
        else
            row.cells[i].className = 'wa';
        await sleep(100);
    }
    guessing_times--;
    localStorage.times = JSON.stringify(guessing_times);
    document.getElementById("guess_left").innerHTML = "剩餘可猜測次數為 <strong>" + guessing_times + "</strong> 次";
    if(corrects == guess.length)
    {
        var myModal = new bootstrap.Modal(document.getElementById("win"), {});
        myModal.show();
        var audio = new Audio('./music/win.mp3');
        audio.play();
    }
    else if(guessing_times == 0)
    {
        var myModal = new bootstrap.Modal(document.getElementById("lose"), {});
        myModal.show();
        var audio = new Audio('./music/fail.mp3');
        audio.play();
    }
    else
    {
        var audio = new Audio('./music/try.mp3');
        audio.play();
    }

}

async function init_table()
{
    var newelment = "<tbody>"
    for(let i = 0; i < guessing_times; ++i)
    {
        newelment += "<tr>";
        for(let j = 0; j < guessing_times - 1; ++j)
            newelment += "<td></td>";
        newelment += "</tr>"
    }
    newelment += '</tbody>'
    document.getElementById("gametable").innerHTML = newelment;
    document.getElementById("guess_left").innerHTML = "剩餘可猜測次數為 <strong>" + guessing_times + "</strong> 次";
}

async function select_word()
{
    var length = document.getElementById("word_length").value;
    var ans_word = await eel.select_voc(length)();
    localStorage.used = JSON.stringify(ans_word);
    localStorage.times = JSON.stringify(ans_word.length + 1)
    window.location.replace('normal.html');
}

if(window.location.pathname == "/normal.html")
    init_table();
    
if(document.getElementById("vtaudio") != null)
    document.getElementById("vtaudio").volume = 0.1;
if(document.getElementById("idxaudio") != null)
    document.getElementById("idxaudio").volume = 0.5;
if(document.getElementById("noraudio") != null)
    document.getElementById("noraudio").volume = 0.3;
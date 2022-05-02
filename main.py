import pyautogui
import time
from PIL import ImageGrab

row1 = 470
col1 = 425
Green = (46, 216, 60)
Yellow = (214, 190, 0)
Purple = (155, 93, 247)

def checkLetterResult(col=1, row=1):
    image = ImageGrab.grab()

    color = image.getpixel((row1 + (row-1)*75, (col1 + (col-1)*75)))
    # pyautogui.moveTo((row1 + (row-1)*75, (col1 + (col-1)*75)))

    if color == Green:
        return 2
    elif color == Yellow:
        return 1
    elif color == Purple:
        return 0
    else:
        print("NEW" + str(color))
        time.sleep(5)
        return -1

def MakeGuess(word, row, currlist):
    pyautogui.write(word)
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(0.3)

    win = True
    for letterIndex in range(5):
        color = checkLetterResult(row, letterIndex + 1)
        if color == 2:
            currlist = list(filter(lambda option: option[letterIndex] == word[letterIndex], currlist))
        if color == 1:
            win = False
            currlist = list(filter(lambda option: option[letterIndex] != word[letterIndex] and word[letterIndex] in option, currlist))
        if color == 0:
            win = False
            currlist = list(filter(lambda option: word[letterIndex] not in option, currlist))
    return win, currlist


if __name__ == '__main__':
    time.sleep(1)
    wordlistbackup = []
    wordlist = []
    with open("Wordlist.txt", "r") as file:
        for line in file:
            wordlistbackup.append(line[0:5])

    while True:
        wordlist = wordlistbackup
        checkWin, wordlist = MakeGuess('paint', 1, wordlist)
        checkWin, wordlist = MakeGuess('model', 2, wordlist)
        checkWin, wordlist = MakeGuess('crush', 3, wordlist)

        currRow = 4

        while checkWin is not True and len(wordlist) > 0:
            checkWin, wordlist = MakeGuess(wordlist[0], currRow, wordlist)
            currRow += 1

        if not checkWin:
            break
        time.sleep(1.5)

    print(len(wordlist))
    print(wordlist)

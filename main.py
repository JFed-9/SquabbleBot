import pyautogui
import time

row1 = 420
col1 = 820
Green = 0x2ED83C
Yellow = 0xD6BE00
Purple = 0x9B5DF7


def MakeGuess(word, row, currlist):
    pyautogui.write(word)
    win = True
    for letterIndex in range(5):
        columnPixel = col1 + letterIndex * 75
        # Get Pixel information for this pixel: row1, columnPixel
        color = Purple
        if color == Green:
            currlist = list(filter(lambda option: option[letterIndex] == word[letterIndex], currlist))
        if color == Yellow:
            win = False
            currlist = list(filter(lambda option: option[letterIndex] != word[letterIndex] and word[letterIndex] in option, currlist))
        if color == Purple:
            win = False
            currlist = list(filter(lambda option: word[letterIndex] not in option, currlist))
    return win, currlist


if __name__ == '__main__':
    time.sleep(3)
    wordlist = []
    with open("Wordlist.txt", "r") as file:
        for line in file:
            wordlist.append(line[0:5])

    print(len(wordlist))

    checkWin, wordlist = MakeGuess('paint', 1, wordlist)
    checkWin, wordlist = MakeGuess('model', 1, wordlist)
    # checkWin, wordlist = MakeGuess('crush', 1, wordlist)

    print(len(wordlist))
    print(wordlist)

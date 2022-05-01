import pyautogui
import ImageGrab

row1 = 420
col1 = 820
Green = 0x2ED83C
Yellow = 0xD6BE00
Purple = 0x9B5DF7


def MakeGuess(word, row, currlist):
    pyautogui.write(word, interval=0.05)
    win = True
    for letterIndex in range(5):
        columnPixel = col1 + letterIndex * 75
        # Get Pixel information for this pixel: row1, columnPixel
        color = 0xFFFFFF
        if color == Green:
            currlist = filter(lambda option: option[letterIndex] == word[letterIndex], currlist)
        if color == Yellow:
            win = False
            currlist = filter(lambda option: option[letterIndex] != word[letterIndex] and word[letterIndex] in option,
                              currlist)
        if color == Purple:
            win = False
            currlist = filter(lambda option: word[letterIndex] not in option, currlist)
    return win


if __name__ == '__main__':
    with open('Wordlist.txt', 'r') as wordlist:
        list = wordlist.readlines()

    checkWin = MakeGuess('paint', 1, list)

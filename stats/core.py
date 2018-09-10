import numpy as np
import os
from sort import sort, lettersort

alphabeth = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def addWord(word):
    with open("ordbok_eng.txt", "a") as file:
        file.write(" ")
        file.write(word)
        file.close()

    file = open("ordbok_eng.txt", "r+")
    filename = "ordbok_eng.txt"
    sort(file, filename)

def readWords(language):
    words = []
    if language == "english":
        ordbok = open('ordbok_eng.txt', 'r')
    if language == "norwegian":
        ordbok = open('ordbok_nor.txt', 'r')
    with ordbok as f:
        for line in f:
            for word in line.split():
                words.append(word)
    return words

def setLength(words, wordlength):

    wordstemp = []
    for word in words:
        if len(word) == wordlength:
            wordstemp.append(word)

    words = wordstemp
    return words

def guessLetter(words, usedletters):
    i = 0
    j = 0
    numtemp = 0
    with open("ordboktemp.txt", "w") as file:
        for word in words:
            file.write(word)
            file.write(" ")
            i+=1
            if i > 20:
                file.write("\n")
                i = 0

    ordboktemp = open('ordboktemp.txt', 'r')
    bokstaver = lettersort(ordboktemp)

    for h in range(len(usedletters)):
        for m in range(len(alphabeth)):
            if usedletters[h] == alphabeth[m]:
                bokstaver[m] = 0

    myfile = "C:\python\stats\ordboktemp.txt"

    if os.path.isfile(myfile):
        os.remove(myfile)
    else:
        print("Error: %s file not found" % ordboktemp)

    for number in bokstaver:
        if number >= numtemp:
            numtemp = number
            nummax = j
        j += 1

    guess = alphabeth[nummax]

    return guess

def eliminateFromLetter(words, guess, placement):
    rightwords = []
    for word in words:
        rightletter = []
        guessingword = list(word)
        for i in range(len(guessingword)):
            if i in placement and guessingword[i] == guess:
                rightletter.append('y')
            if i not in placement and guessingword[i] != guess:
                rightletter.append('y')
        if len(rightletter) == len(guessingword):
            rightwords.append(word)
    return rightwords

def eliminateWrongWords(words, guess):
    wordstemp = []
    for word in words:
        if guess not in word:
            wordstemp.append(word)

    return wordstemp

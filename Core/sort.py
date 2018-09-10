import numpy as np

def sort(fil, filename):
    i = 0
    j = 0
    words = []
    output = []

    with fil as f:
        for line in f:
            for word in line.split():
                words.append(word)

        for word in words:
            if word not in output:
                output.append(str.lower(word))

        output.sort(key=lambda v: v.upper())

    with open(filename, "w") as f:
        for word in output:
            f.write(word)
            f.write(" ")
            i+=1
            if i > 20:
                f.write("\n")
                i = 0

    return(words)

def lettersort(file):
    alphabeth = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    ALPHABETH = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    i = 0
    letters = []
    times = np.zeros(26)
    with file as f:
        for line in f:
            for word in line.split():
                for letter in word:
                    letters.append(letter)

    for letter in letters:
        for i in range(len(alphabeth)):
            if letter == alphabeth[i] or letter == ALPHABETH[i]:
                times[i] = times[i] + 1

    return(times)

"""guess = []
al = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
fil = open("ordbok_eng.txt", "r+")
times = lettersort(fil)

for k in range(len(times)):
    itemindex = np.where(times==max(times))
    guess.append(al[itemindex[0][0]])
    times[itemindex[0]]=0
print(guess)"""

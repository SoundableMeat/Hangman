from core import *
import numpy as np
import os
from sort import sort, lettersort

words=readWords("english")
iter=[]

for word in words:
    wordstemp=words

    wordstemp=setLength(wordstemp,len(word))
    Tries=0
    used=[]
    carryOn = True
    while carryOn:
        guess=guessLetter(wordstemp,used)
        used.append(guess)

        if guess in word:
            place=[]
            i=0
            for letter in word:
                if letter==guess:
                    place.append(i)
                i+=1
            wordstemp=eliminateFromLetter(wordstemp,guess,place)
        else:
            wordstemp=eliminateWrongWords(wordstemp,guess)
            Tries+=1

        if len(wordstemp)==1:
            carryOn=False
        if len(wordstemp)==0:
            raise ValueError('Que?')
    iter.append(Tries)
    if len(iter)%2==0:
        print(round(len(iter)/len(words)*100,2),'%')

"""tmp = 0
tmpi = 0
for i in range(len(iter)):
    if iter[i]>tmp:
        tmp = iter[i]
        tmpi = i

print(tmp,words[tmpi])"""

h=0
tri=[]
for h in range(len(iter)):
    tri.append(words[h])
    tri.append(str(iter[h]))
    tri.append("    ")
i=0
with open("Tries.txt", "w") as f:
    for word in tri:
        f.write(word)
        f.write(" ")
        i+=1
        if i > 2:
            f.write("\n")
            i = 0

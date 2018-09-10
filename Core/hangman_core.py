from graphics import *
from graphics_hangman import *
from sort import *

SCREENWIDTH, SCREENHEIGHT = 1000, 500

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def inBox(pt1, box):

    # get the distance between pt1 and circ using the
    # distance formula
    dx = abs(pt1.getX() - box.getCenter().getX())
    dy = abs(pt1.getY() - box.getCenter().getY())

    # check whether the distance is less than the radius
    return dx <= abs(box.getP1().getX() - box.getCenter().getX()) and dy <= abs(box.getP1().getY() - box.getCenter().getY())

def LengthBoxes():

    boxes = []
    for k in range(1,5):
        for j in range(10):
            boxes.append(Rectangle(Point((3*j+1)*SCREENWIDTH/31, (3*k+1)*SCREENHEIGHT/16), Point((3*(j+1)*SCREENWIDTH/31), 3*(k+1)*SCREENHEIGHT/16)))

    return boxes

def PlacementBoxes(wordlength):

    h = 1
    boxes = []
    carryOn = True
    k = 2
    while carryOn:
        for j in range(5,10):
            boxes.append(Rectangle(Point((3*j+1)*SCREENWIDTH/31, (3*k)*SCREENHEIGHT/16), Point((3*(j+1)*SCREENWIDTH/31), (3*(k+1)-1)*SCREENHEIGHT/16)))
            if h >= wordlength:
                carryOn = False
                break
            h+=1
        k+=1
        j = 5
    return boxes

def main():

    carryOn = True
    welcome = True
    length = True
    i = 0

    win = GraphWin("My Window", SCREENWIDTH, SCREENHEIGHT)
    win.setBackground(color_rgb(100,100,255))

    Welcome_Message = Text(Point(SCREENWIDTH/2, SCREENHEIGHT/5),"Hangman")
    Welcome_Message.setSize(36)
    Welcome_Message.setTextColor("White")

    Welcome_rect_eng = Rectangle(Point(3*SCREENWIDTH/14,4*SCREENHEIGHT/6), Point(6*SCREENWIDTH/14,5*SCREENHEIGHT/6))
    Welcome_rect_eng.setFill(color_rgb(0,255,50))
    Welcome_rect_nor = Rectangle(Point(8*SCREENWIDTH/14,4*SCREENHEIGHT/6), Point(11*SCREENWIDTH/14,5*SCREENHEIGHT/6))
    Welcome_rect_nor.setFill(color_rgb(0,255,50))


    Welcome_text_eng = Text(Welcome_rect_eng.getCenter(), "English")
    Welcome_text_eng.setSize(36)
    Welcome_text_eng.setFace('arial')
    Welcome_text_eng.setTextColor("White")
    Welcome_text_nor = Text(Welcome_rect_nor.getCenter(), "Norsk")
    Welcome_text_nor.setSize(36)
    Welcome_text_nor.setFace('arial')
    Welcome_text_nor.setTextColor("White")

    Welcome_Message.draw(win)
    Welcome_rect_eng.draw(win)
    Welcome_text_eng.draw(win)
    Welcome_rect_nor.draw(win)
    Welcome_text_nor.draw(win)

    hangman = [Line(Point(SCREENWIDTH/14, 9*SCREENHEIGHT/10), Point(2*SCREENWIDTH/14, 7*SCREENHEIGHT/10)),
    Line(Point(3*SCREENWIDTH/14, 9*SCREENHEIGHT/10), Point(2*SCREENWIDTH/14, 7*SCREENHEIGHT/10)),
    Line(Point(2*SCREENWIDTH/14, 7*SCREENHEIGHT/10), Point(2*SCREENWIDTH/14, 3*SCREENHEIGHT/10)),
    Line(Point(2*SCREENWIDTH/14, 3*SCREENHEIGHT/10), Point(4*SCREENWIDTH/14, 3*SCREENHEIGHT/10)),
    Line(Point(2*SCREENWIDTH/14, 4*SCREENHEIGHT/10), Point(3*SCREENWIDTH/14, 3*SCREENHEIGHT/10)),
    Line(Point(4*SCREENWIDTH/14, 3*SCREENHEIGHT/10), Point(4*SCREENWIDTH/14, 7*SCREENHEIGHT/20)),
    Circle(Point(4*SCREENWIDTH/14, 4*SCREENHEIGHT/10), SCREENHEIGHT/20),
    Line(Point(4*SCREENWIDTH/14, 9*SCREENHEIGHT/20), Point(4*SCREENWIDTH/14, 13*SCREENHEIGHT/20)),
    Line(Point(4*SCREENWIDTH/14, 10*SCREENHEIGHT/20), Point(7*SCREENWIDTH/28, 9*SCREENHEIGHT/20)),
    Line(Point(4*SCREENWIDTH/14, 10*SCREENHEIGHT/20), Point(9*SCREENWIDTH/28, 9*SCREENHEIGHT/20)),
    Line(Point(4*SCREENWIDTH/14, 13*SCREENHEIGHT/20), Point(7*SCREENWIDTH/28, 14*SCREENHEIGHT/20)),
    Line(Point(4*SCREENWIDTH/14, 13*SCREENHEIGHT/20), Point(9*SCREENWIDTH/28, 14*SCREENHEIGHT/20)),]

    for line in hangman:
        line.setWidth(2)

    #Startskjermen med knapp
    while welcome:
        mouse = win.getMouse()
        if inBox(mouse, Welcome_rect_eng):
            language = "eng"
            clear(win)
            welcome=False
        if inBox(mouse, Welcome_rect_nor):
            language = "nor"
            clear(win)
            welcome=False

    #Velger lengden på ordet fra bokser på skjermen
    while length:
        numbers = LengthBoxes()
        number = 1
        for box in numbers:
            box.draw(win)
            Text(box.getCenter(), number).draw(win)
            number+=1
        if language == "eng":
            txt = Text(Point(SCREENWIDTH/2, 2*SCREENHEIGHT/16), "How long is your word?")
        if language == "nor":
            txt = Text(Point(SCREENWIDTH/2, 2*SCREENHEIGHT/16), "Hvor langt er ordet?")
        txt.setSize(20)
        txt.draw(win)
        mouse = win.getMouse()
        number = 0
        for box in numbers:
            number+=1
            if inBox(mouse, box):
                wordlength = number
                clear(win)
                length = False

    if language == "eng":
        words = readWords("english")
    if language == "nor":
        words = readWords("norwegian")
    words = setLength(words, wordlength)

    usedletters = []
    answer = True
    Placement = False
    rightguess = False
    finalanswer = False
    guessedletters = 0
    placetext = []

    for k in range(wordlength):
        Line(Point((4*k+1)*SCREENWIDTH/(wordlength*4 + 1), 3*SCREENHEIGHT/16), Point((4*k+4)*SCREENWIDTH/(wordlength*4 + 1), 3*SCREENHEIGHT/16)).draw(win)

    #Hovedloop med spillet
    while carryOn:

        if len(words) == 1:
            if language == "eng":
                finalword = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), 'Is {} your word?'.format(words[0]))
            if language == "nor":
                finalword = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), 'Er ordet ditt: {}?'.format(words[0]))
            finalword.setSize(20)
            finalword.draw(win)
            finalyes = yes = Rectangle(Point(10*SCREENWIDTH/16, 6*SCREENHEIGHT/16), Point(11*SCREENWIDTH/16, 7*SCREENHEIGHT/16)).draw(win)
            if language == "eng":
                finalyestext = Text(yes.getCenter(), "Yes").draw(win)
            if language == "nor":
                finalyestext = Text(yes.getCenter(), "Ja").draw(win)
            finalno = Rectangle(Point(13*SCREENWIDTH/16, 6*SCREENHEIGHT/16), Point(14*SCREENWIDTH/16, 7*SCREENHEIGHT/16)).draw(win)
            if language == "eng":
                finalnotext = Text(no.getCenter(), "No").draw(win)
            if language == "nor":
                finalnotext = Text(no.getCenter(), "Nei").draw(win)
            finalanswer = True

        if len(words) == 0:
            defeated = True
            for text in placetext:
                text.undraw()
            if language == "eng":
                defeat = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), "What is your word?")
            if language == "nor":
                defeat = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), "Hva er ditt ord?")
            defeat.setSize(20)
            defeat.draw(win)
            finalplacement = 0
            placetext = []
            rightword = []
            outputword = ""
            while defeated:
                key = win.getKey()
                for letter in alphabeth:
                    if key == letter:
                        placetext.append(Text(Point((8*finalplacement+5)*SCREENWIDTH/(wordlength*8 + 2), 9*SCREENHEIGHT/64), letter))
                        placetext[finalplacement].setSize(30)
                        placetext[finalplacement].draw(win)
                        rightword.append(letter)
                finalplacement+=1
                if len(rightword) == wordlength:
                    for letter in rightword:
                        outputword+=letter
                    addWord(outputword)
                    defeated = False
                    carryOn = False
                    answer = False

        while finalanswer:
            mouse = win.getMouse()
            if inBox(mouse, finalyes):
                finalword.undraw()
                finalyes.undraw()
                finalyestext.undraw()
                finalno.undraw()
                finalnotext.undraw()
                if language == "eng":
                    victory = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), "Yey, I won!")
                if language == "nor":
                    victory = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), "Jaa, jeg vant!")
                victory.setSize(20)
                victory.draw(win)
                victorydone =  Rectangle(Point(10*SCREENWIDTH/16, 6*SCREENHEIGHT/16), Point(14*SCREENWIDTH/16, 9*SCREENHEIGHT/16)).draw(win)
                if language == "eng":
                    victorydonetext = Text(victorydone.getCenter(), "Done")
                if language == "nor":
                    victorydonetext = Text(victorydone.getCenter(), "Ferdig")
                victorydonetext.setSize(36)
                victorydonetext.draw(win)
                while finalanswer:
                    mouse = win.getMouse()
                    if inBox(mouse, victorydone):
                        finalanswer = False
                        carryOn = False
                        answer = False
            if inBox(mouse, finalno):
                finalword.undraw()
                finalyes.undraw()
                finalyestext.undraw()
                finalno.undraw()
                finalnotext.undraw()
                for text in placetext:
                    text.undraw()
                if language == "eng":
                    defeat = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), "What is your word?")
                if language == "nor":
                    defeat = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), "Hva er ditt ord?")
                defeat.setSize(20)
                defeat.draw(win)
                finalplacement = 0
                placetext = []
                rightword = []
                outputword = ""
                while finalanswer:
                    key = win.getKey()
                    for letter in alphabeth:
                        if key == letter:
                            placetext.append(Text(Point((8*finalplacement+5)*SCREENWIDTH/(wordlength*8 + 2), 9*SCREENHEIGHT/64), letter))
                            placetext[finalplacement].setSize(30)
                            placetext[finalplacement].draw(win)
                            rightword.append(letter)
                    finalplacement+=1
                    if len(rightword) == wordlength:
                        for letter in rightword:
                            outputword+=letter
                        addWord(outputword)
                        finalanswer = False
                        carryOn = False
                        answer = False


        if carryOn:
            guess = guessLetter(words, usedletters)
            usedletters.append(guess)

            if language == "eng":
                txt = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), 'Is {} in your word?'.format(guess))
            if language == "nor":
                txt = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), 'Er {} i ditt ord?'.format(guess))
            txt.setSize(20)
            txt.draw(win)

            yes = Rectangle(Point(10*SCREENWIDTH/16, 6*SCREENHEIGHT/16), Point(11*SCREENWIDTH/16, 7*SCREENHEIGHT/16)).draw(win)
            if language == "eng":
                yestext = Text(yes.getCenter(), "Yes").draw(win)
            if language == "nor":
                yestext = Text(yes.getCenter(), "Ja").draw(win)
            no = Rectangle(Point(13*SCREENWIDTH/16, 6*SCREENHEIGHT/16), Point(14*SCREENWIDTH/16, 7*SCREENHEIGHT/16)).draw(win)
            if language == "eng":
                notext = Text(no.getCenter(), "No").draw(win)
            if language == "nor":
                notext = Text(no.getCenter(), "Nei").draw(win)

        while answer:
            mouse = win.getMouse()
            if inBox(mouse, yes):
                answer = False
                Placement = True
            if inBox(mouse, no):
                hangman[i].draw(win)
                i+=1
                if i >= 12:
                    gameover = Text(Point(SCREENWIDTH/2, SCREENHEIGHT/2), 'GAME OVER!')
                    gameover.setSize(36)
                    gameover.setTextColor('Red')
                    gameover.setStyle('bold italic')
                    gameover.setFace('arial')
                    gameover.draw(win)
                    gameoverrect = Rectangle(Point(2*SCREENWIDTH/5, 5*SCREENHEIGHT/8), Point(3*SCREENWIDTH/5, 7*SCREENHEIGHT/8)).draw(win)
                    if language == "eng":
                        gameovertext = Text(gameoverrect.getCenter(), 'DONE')
                    if language == "nor":
                        gameovertext = Text(gameoverrect.getCenter(), 'Ferdig')
                    gameovertext.setSize(36)
                    gameovertext.draw(win)
                    gameOver = True
                    while gameOver:
                        mouse = win.getMouse()
                        if inBox(mouse, gameoverrect):
                            gameOver = False
                            carryOn = False
                            answer = False
                words = eliminateWrongWords(words, guess)
                answer = False

        if carryOn:
            txt.undraw()
            yes.undraw()
            no.undraw()
            yestext.undraw()
            notext.undraw()

        if Placement:
            placement = []
            if language == "eng":
                text = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), 'Where is the letter?')
            if language == "nor":
                text = Text(Point(3*SCREENWIDTH/4, 5*SCREENHEIGHT/16), 'Hvor er bokstaven?')
            text.setSize(20)
            text.draw(win)
            placementboxes = PlacementBoxes(wordlength)
            placementtext = []
            number = 1
            for box in placementboxes:
                box.draw(win)
                placementtext.append(Text(box.getCenter(), number))
                placementtext[number-1].draw(win)
                number+=1
            done = Rectangle(Point(19*SCREENWIDTH/31, 15*SCREENHEIGHT/17), Point(27*SCREENWIDTH/31, 16*SCREENHEIGHT/17))
            done.draw(win)
            if language == "eng":
                donetext = Text(done.getCenter(), "Done").draw(win)
            if language == "nor":
                donetext = Text(done.getCenter(), "Ferdig").draw(win)
            picking = True
            while picking:
                mouse = win.getMouse()
                number = 0
                for box in placementboxes:
                    if inBox(mouse, box):
                        placement.append(number)
                        placetext.append(Text(Point((8*number+5)*SCREENWIDTH/(wordlength*8 + 2), 9*SCREENHEIGHT/64), guess))
                        placetext[guessedletters].setSize(30)
                        placetext[guessedletters].draw(win)
                        guessedletters += 1
                    number+=1
                if inBox(mouse, done):
                    picking = False
            words = eliminateFromLetter(words, guess, placement)
            rightguess = True


        if rightguess == True:
            text.undraw()
            number = 0
            for box in placementboxes:
                box.undraw()
                placementtext[number].undraw()
                number+=1
            done.undraw()
            donetext.undraw()
            rightguess = False
            Placement = False

        if win.checkKey() == "x":
            carryOn = False

        win.update()
        answer = True
        print(len(words))

    win.close()

main()

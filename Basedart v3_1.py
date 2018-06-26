import random
import math
import time
from tkinter import *

def getNewHitter():
    x = random.random()*math.pi
    y = random.random()
    if(y<math.sin(x)):
        return 20 + (x/math.pi)*(100-20)
    return getNewHitter()

def IsCaught(Hit):
    r = random.random()
    if(Hit == 1):
        if r < 0.10:
            PlayAnimation('Animation/Catch.gif', False)
            return True
    elif(Hit == 2):
        if r < 0.05:
            PlayAnimation('Animation/Catch.gif', False)
            return True
    elif(Hit == 4):
        if r < 0.01:
            PlayAnimation('Animation/Catch.gif', False)
            return True


    PlayAnimation('Animation/NoCatch.gif', False)
    return False

def ChangeNumber(Key, Number):
    # (Row, Col, FrameId
    Dic = {'Pitches': (0,0,0),
           'Ball'   : (0,1,0),
           'Strike' : (0,2,0),
           'Out'    : (0,3,0),
           'Hitter' : (0,4,0),
           'Inning1': (0,3,1),
           'Inning2': (0,1,2),
           'Inning3': (0,2,2),
           'Inning4': (0,3,2),
           'Inning5': (0,4,2),
           'Inning6': (0,5,2),
           'Inning7': (0,6,2),
           'Inning8': (0,7,2),
           'Inning9': (0,8,2),
           'Runs'   : (0,9,2)
           }


    if((Number < 10 and Number != -1) or 'Inning' in Key):
        if(Number == OFF):
            Label(Frames[Dic[Key][2]], image=NumberImages[10], border=0).grid(row=Dic[Key][0], column=Dic[Key][1], sticky=SE)
        else:
            Label(Frames[Dic[Key][2]], image=NumberImages[Number%10], border=0).grid(row=Dic[Key][0], column=Dic[Key][1], sticky=SE)
    elif (Number >   100):
        Label(Frames[Dic[Key][2]], image=NumberImages[int(Number%10)], border=0).grid(row=Dic[Key][0], column=Dic[Key][1], sticky=SE)
        Label(Frames[Dic[Key][2]], image=NumberImages[int(Number/100)], border=0).grid(row=Dic[Key][0], column=Dic[Key][1], sticky=SE, padx=59)
    else:
        if(Number == OFF):
            Label(Frames[Dic[Key][2]], image=NumberImages[10], border=0).grid(row=Dic[Key][0], column=Dic[Key][1], sticky=SE)
            Label(Frames[Dic[Key][2]], image=NumberImages[10], border=0).grid(row=Dic[Key][0], column=Dic[Key][1], sticky=SE, padx=59)
        else:
            Label(Frames[Dic[Key][2]], image=NumberImages[int(Number%10)], border=0).grid(row=Dic[Key][0], column=Dic[Key][1], sticky=SE)
            Label(Frames[Dic[Key][2]], image=NumberImages[int(Number/10)], border=0).grid(row=Dic[Key][0], column=Dic[Key][1], sticky=SE, padx=59)

def UpdateTop():
    ChangeNumber('Pitches', PitchCount)
    ChangeNumber('Ball', Misses)
    ChangeNumber('Strike', Strikes)
    ChangeNumber('Out', Outs)
    ChangeNumber('Hitter', Hitter)

def MoveOnBases(n):
    #Move
    global Bases
    j = n
    Bases = [True] + Bases
    while( j != 1):
        j -= 1
        Bases = [False] + Bases

    #Check if people got home
    for i in range(3, n+3):
        if(Bases[i]):
            global Runs
            Runs += 1
            global Inning
            RunsPerInning[Inning-1] += 1
            ChangeNumber('Runs', Runs)
            ChangeNumber('Inning%d' % Inning, RunsPerInning[Inning-1])

    Bases = Bases[0:3]
    updateBasePic()

def updateBasePic():
    #load new Picture
    Name = "Bases/"
    i = 0
    for b in Bases:
        i += 1
        if b :
            Name += "%d" %i

    if(Name == "Bases/"):
        Name += "Empty"
    Name += ".gif"

    global BasesPic
    BasesPic = PhotoImage(file=Name)
    BasesLabel.config(image = BasesPic)
    BasesFrame.update()

def walk():
    if(Bases[0]):
        if(Bases[1]):
            if(Bases[2]):
                MoveOnBases(1)
                return
            Bases[2] = True
        Bases[1] = True
    Bases[0] = True
    updateBasePic()

def strike():
    deactivateBtns()
    global Strikes
    global Misses
    global PitchCount
    global Outs

    HRProb = 0.01
    DProb  = 0.02
    SProb = 0.04
    bHit = True
    i = random.random()
    #print(i)
    if(i <= HRProb):
        #HR
        PlayAnimation(SZAnimations['HR'], True)
        if(not IsCaught(4)):
            MoveOnBases(4)
        else:
            Outs += 1
            CheckAndHandleOut
    elif (i <= HRProb + DProb):
        # double
        PlayAnimation(SZAnimations['Double'], True)
        if(not IsCaught(2)):
            MoveOnBases(2)
        else:
            Outs += 1
            CheckAndHandleOut
    elif (i <= SProb + HRProb + DProb):
        # single
        PlayAnimation(SZAnimations['Single'], True)
        if(not IsCaught(1)):
            MoveOnBases(1)
        else:
            Outs += 1
    else:
        # Strike
        PlayAnimation(SZAnimations['Strike'], True)
        Strikes += 1
        bHit = False

    PitchCount += 1

    if(bHit):
        Strikes = 0
        Misses = 0

        global Hitter
        Hitter = getNewHitter()

    CheckAndHandleOut()
    CheckAndHandleStrikeout()
    UpdateTop()
    if(GAMERUNNING):
        activateBtns()

def perfect():
    deactivateBtns()
    global Strikes
    global PitchCount

    PlayAnimation(SZAnimations['Strike'], True)
    Strikes += 1
    PitchCount += 1

    CheckAndHandleStrikeout()
    UpdateTop()
    if(GAMERUNNING):
        activateBtns()

def miss():

    deactivateBtns()
    global Misses
    global Strikes
    global PitchCount
    global Outs

    HRProb = 0.02
    DProb  = 0.06
    SProb = 0.10
    StrikeProb = 0.07


    bHit = True
    i = random.random()
    #print(i)
    if(i <= HRProb):
        #HR
        PlayAnimation(BAnimations['HR'], True)
        if(not IsCaught(4)):
            MoveOnBases(4)
        else:
            Outs += 1
    elif (i <= HRProb + DProb):
        # double
        PlayAnimation(BAnimations['Double'], True)
        if(not IsCaught(2)):
            MoveOnBases(2)
        else:
            Outs += 1
    elif (i <= SProb + HRProb + DProb):
        # single
        PlayAnimation(BAnimations['Single'], True)
        if(not IsCaught(1)):
            MoveOnBases(1)
        else:
            Outs += 1
    elif (i <= SProb + HRProb + DProb + StrikeProb):
        # Strike
        PlayAnimation(BAnimations['Strike'], True)
        Strikes += 1
        CheckAndHandleStrikeout()
        bHit = False
    else:
        # Ball
        PlayAnimation(BAnimations['Ball'], True)
        bHit = False
        Misses += 1

    CheckAndHandleOut()

    PitchCount += 1
    if(Misses == 4 or bHit):
        if(Misses == 4):
            walk()
        Strikes = 0
        Misses = 0
        global Hitter
        Hitter = getNewHitter()

    UpdateTop()
    if(GAMERUNNING):
        activateBtns()

def PlayAnimation(FileName, isSwingAnimation) :
    global FieldManPic
    global StandingFildManPic
    FieldManLabel.config(image = StandingFildManPic)
    FieldManFrame.update()

    counter = 0
    if(isSwingAnimation):
        FrameNumber = 24
        global AnimationPic

        while counter < FrameNumber :

            AnimationPic = PhotoImage(file=FileName, format="gif -index " + str(counter))
            AnimationLabel.config(image = AnimationPic)
            AnimationFrame.update()
            counter += 1
    else:
        FrameNumber = 24


        while counter < FrameNumber :

           FieldManPic = PhotoImage(file=FileName, format="gif -index " + str(counter))
           FieldManLabel.config(image = FieldManPic)
           FieldManFrame.update()
           counter += 1

def deactivateBtns():
    global Btns
    for B in Btns:
        B['state'] = 'disabled'

def activateBtns():
    global Btns
    for B in Btns:
        B['state'] = 'normal'

def CheckAndHandleStrikeout():
    global Strikes
    global Misses
    if(Strikes == 3):
        Strikes = 0
        Misses = 0
        global Outs
        Outs += 1
        CheckAndHandleOut()
        if(GAMERUNNING):
            global Hitter
            Hitter = getNewHitter()

def CheckAndHandleOut():
    global Outs
    if(Outs == 3):
        global Bases
        global Hitter
        global Strikes
        global Misses

        Bases = [False, False, False]
        updateBasePic()
        global Inning
        if(Inning == MaxInnings):
            #Game End
            global GAMERUNNING
            GAMERUNNING = False

            StrikeBtn['state']  = 'disabled'
            MissBtn['state']  = 'disabled'

            Hitter = OFF
            Misses = OFF
            Strikes = OFF
            Outs = OFF
            UpdateTop()
            return

        else:
            Inning += 1
            RunsPerInning.append(0)
            ChangeNumber('Inning%d' % Inning, RunsPerInning[Inning-1])

        Hitter = getNewHitter()
        Outs = 0

#main

print("How Many innings do you want to play?")
MaxInnings = int(input())
OFF = -1

window = Tk()

Inning = 1
Runs = 0
Outs = 0
Strikes = 0
Misses = 0
Hitter = getNewHitter()
PitchCount = 0
RunsPerInning = [0]

Bases = [False, False, False]

#
# Setup Window
#
window.title('Basedart')

#icon = PhotoImage(file='icon50.gif')
#window.tk.call('wm', 'iconphoto', window._w, icon)

window.configure(background='light grey')
window.grid_rowconfigure(0, pad=40)
Board = Frame(window, border=5, relief="solid")
Board.grid(row=0,column=0, sticky=N, pady=(40, 0))
Boardframe1 = Frame(Board)
Boardframe1.grid(row=0,column=0, sticky=W)
Boardframe2 = Frame(Board)
Boardframe2.grid(row=1,column=0, sticky=W)
Boardframe2_1 = Frame(Boardframe2)
Boardframe2_1.grid(row=0,column=0, sticky=W)
Boardframe2_2 = Frame(Boardframe2)
Boardframe2_2.grid(row=0,column=1, sticky=W)
Boardframe3 = Frame(Board)
Boardframe3.grid(row=2,column=0, sticky=W)

BtnFrame = Frame(Boardframe2);
BtnFrame.grid(row=0, column=0, sticky=W)
BtnFrame.configure(background='white')

Frames = [Boardframe1, Boardframe2_1, Boardframe2_2, Boardframe3]

BottomFrame = Frame(window)
BottomFrame.grid(row=3, column=0, sticky=W)
BottomFrame.configure(background='white')

AnimationFrame = Frame(BottomFrame)
AnimationFrame.grid(row=0, column=0, sticky=W)

BasesFrame = Frame(BottomFrame)
BasesFrame.grid(row=0, column=1, sticky=N)
BasesFrame.configure(background='white')

FieldManFrame = Frame(BottomFrame)
FieldManFrame.grid(row=0, column=2, sticky=W)



#Backgorund
BG00 = PhotoImage(file="Board/0_0.gif")
BG01 = PhotoImage(file="Board/0_1.gif")
BG02 = PhotoImage(file="Board/0_2.gif")
BG03 = PhotoImage(file="Board/0_3.gif")
BG04 = PhotoImage(file="Board/0_4.gif")
BG05 = PhotoImage(file="Board/0_5.gif")
BG10 = PhotoImage(file="Board/1_0.gif")
BG11 = PhotoImage(file="Board/1_1.gif")
BG12 = PhotoImage(file="Board/1_2.gif")
BG13 = PhotoImage(file="Board/1_3.gif")
BG14 = PhotoImage(file="Board/1_4.gif")
BG15 = PhotoImage(file="Board/1_5.gif")
BG16 = PhotoImage(file="Board/1_6.gif")
BG17 = PhotoImage(file="Board/1_7.gif")
BG18 = PhotoImage(file="Board/1_8.gif")
BG19 = PhotoImage(file="Board/1_9.gif")
BG110 = PhotoImage(file="Board/1_10.gif")
BG20 = PhotoImage(file="Board/2_0.gif")

#Numbers
Noff = PhotoImage(file="Numbers/off.gif")
N0 = PhotoImage(file="Numbers/0.gif")
N1 = PhotoImage(file="Numbers/1.gif")
N2 = PhotoImage(file="Numbers/2.gif")
N3 = PhotoImage(file="Numbers/3.gif")
N4 = PhotoImage(file="Numbers/4.gif")
N5 = PhotoImage(file="Numbers/5.gif")
N6 = PhotoImage(file="Numbers/6.gif")
N7 = PhotoImage(file="Numbers/7.gif")
N8 = PhotoImage(file="Numbers/8.gif")
N9 = PhotoImage(file="Numbers/9.gif")
NumberImages = [N0, N1, N2, N3, N4, N5, N6, N7, N8, N9, Noff]

#Animations

#
AnimationPic = PhotoImage(file="Animation/SZStrike.gif")
BasesPic = PhotoImage(file="Bases/Empty.gif")
StandingFildManPic = PhotoImage(file="Animation/Catch.gif")
FieldManPic = StandingFildManPic


SZAnimations = {'Strike' : "Animation/SZStrike.gif",
                'Single' : "Animation/SZSingle.gif",
                'Double' : "Animation/SZDouble.gif",
                'HR'     : "Animation/SZHomeRun.gif"}

BAnimations = { 'Strike' : "Animation/BStrike.gif",
                'Single' : "Animation/BSingle.gif",
                'Double' : "Animation/BDouble.gif",
                'HR'     : "Animation/BHomeRun.gif",
                'Ball'   : "Animation/BBall.gif"}

# Picture Labels
Label(Boardframe1, image=BG00, border=0).grid(row=0, column=0, sticky=S)
Label(Boardframe1, image=BG01, border=0).grid(row=0, column=1, sticky=W)
Label(Boardframe1, image=BG02, border=0).grid(row=0, column=2, sticky=W)
Label(Boardframe1, image=BG03, border=0).grid(row=0, column=3, sticky=W)
Label(Boardframe1, image=BG04, border=0).grid(row=0, column=4, sticky=W)
Label(Boardframe1, image=BG05, border=0).grid(row=0, column=5, sticky=W)

Label(Boardframe2_1, image=BG10, border=0).grid(row=0, column=0, columnspan=4, sticky=W)

Label(Boardframe2_2, image=BG11, border=0).grid(row=0, column=1, sticky=W)
Label(Boardframe2_2, image=BG12, border=0).grid(row=0, column=2, sticky=W)
Label(Boardframe2_2, image=BG13, border=0).grid(row=0, column=3, sticky=W)
Label(Boardframe2_2, image=BG14, border=0).grid(row=0, column=4, sticky=W)
Label(Boardframe2_2, image=BG15, border=0).grid(row=0, column=5, sticky=W)
Label(Boardframe2_2, image=BG16, border=0).grid(row=0, column=6, sticky=W)
Label(Boardframe2_2, image=BG17, border=0).grid(row=0, column=7, sticky=W)
Label(Boardframe2_2, image=BG18, border=0).grid(row=0, column=8, sticky=W)
Label(Boardframe2_2, image=BG19, border=0).grid(row=0, column=9, sticky=W)
Label(Boardframe2_2, image=BG110, border=0).grid(row=0, column=10, sticky=W)
Label(Boardframe3, image=BG20, border=0).grid(row=0, column=0, sticky=W)

AnimationLabel = Label(AnimationFrame, image=AnimationPic, border=0)
AnimationLabel.grid(row=0, column=0, sticky=W)

BasesLabel = Label(BasesFrame, image=BasesPic, border=0)
BasesLabel.configure(background='white')
BasesLabel.grid(row=0, column=0, sticky=W, pady=(40,0))

FieldManLabel = Label(FieldManFrame, image=FieldManPic, border=0)
FieldManLabel.grid(row=0, column=0, sticky=W)

#Buttons
LeftOffButton = PhotoImage(file="Board/l_off_btn.gif")
Label(BtnFrame, image=LeftOffButton, border=0).grid(row=0, column=0, sticky=W)
PerfectBtn = Button(BtnFrame, text="PERFECT", width=6, padx=20, pady=20, command=perfect)
PerfectBtn.grid(row=0, column=1, sticky=E)
StrikeBtn = Button(BtnFrame, text="STRIKE", width=6, padx=20, pady=20, command=strike)
StrikeBtn.grid(row=0, column=2, sticky=E)
MissBtn = Button(BtnFrame, text="BALL", width=6, padx=20, pady=20, command=miss)
MissBtn.grid(row=0, column=3, sticky=E)
Btns = [StrikeBtn, MissBtn, PerfectBtn]

UpdateTop()
ChangeNumber('Inning1', 0)
ChangeNumber('Runs', 0)
GAMERUNNING = True

window.mainloop()
print("Total gamescore after %d innings:\n You gave up %d runs in %d pitches." % (Inning, Runs, PitchCount))
input()

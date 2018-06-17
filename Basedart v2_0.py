import random
import math
from tkinter import *

def getNewHitter():
    x = random.random()*math.pi
    y = random.random()
    if(y<math.sin(x)):
        return 20 + (x/math.pi)*(100-20)
    return getNewHitter()

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

def strike():
    global Strikes    
    global Misses
    global PitchCount
    
    Strikes += 1    
    PitchCount += 1
    
    if(Strikes == 3):
        Strikes = 0
        Misses = 0
        
        global Hitter
        Hitter = getNewHitter()
        global Outs
        Outs += 1
        if(Outs == 3):
            global Inning
            if(Inning == MaxInnings):
                #Game End
                StrikeBtn['state']  = 'disabled'
                MissBtn['state']  = 'disabled'

                #These will produce off
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
            
            
            Outs = 0

    UpdateTop()  

def miss():
    global Misses
    global Strikes
    global PitchCount
    
    PitchCount += 1
    Misses += 1
    if(Misses == 4):
        Strikes = 0
        Misses = 0
        global Runs
        Runs += 1
        global Inning
        RunsPerInning[Inning-1] += 1
        ChangeNumber('Runs', Runs)
        ChangeNumber('Inning%d' % Inning, RunsPerInning[Inning-1])
        global Hitter
        Hitter = getNewHitter()
    UpdateTop()  

    
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

#
# Setup Window
#
window.title('Basedart')
frame1 = Frame(window)
frame1.grid(row=0,column=0, sticky=W)
frame2 = Frame(window)
frame2.grid(row=1,column=0, sticky=W)
frame2_1 = Frame(frame2)
frame2_1.grid(row=1,column=0, sticky=W)
frame2_2 = Frame(frame2)
frame2_2.grid(row=1,column=1, sticky=W)
frame3 = Frame(window)
frame3.grid(row=2,column=0, sticky=W)

Frames = [frame1, frame2_1, frame2_2, frame3]
PicLabels = []
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

Label(frame1, image=BG00, border=0).grid(row=0, column=0, sticky=S)
Label(frame1, image=BG01, border=0).grid(row=0, column=1, sticky=W)
Label(frame1, image=BG02, border=0).grid(row=0, column=2, sticky=W)
Label(frame1, image=BG03, border=0).grid(row=0, column=3, sticky=W)
Label(frame1, image=BG04, border=0).grid(row=0, column=4, sticky=W)
Label(frame1, image=BG05, border=0).grid(row=0, column=5, sticky=W)

Label(frame2_1, image=BG10, border=0).grid(row=0, column=0, columnspan=4, sticky=W)

Label(frame2_2, image=BG11, border=0).grid(row=0, column=1, sticky=W)
Label(frame2_2, image=BG12, border=0).grid(row=0, column=2, sticky=W)
Label(frame2_2, image=BG13, border=0).grid(row=0, column=3, sticky=W)
Label(frame2_2, image=BG14, border=0).grid(row=0, column=4, sticky=W)
Label(frame2_2, image=BG15, border=0).grid(row=0, column=5, sticky=W)
Label(frame2_2, image=BG16, border=0).grid(row=0, column=6, sticky=W)
Label(frame2_2, image=BG17, border=0).grid(row=0, column=7, sticky=W)
Label(frame2_2, image=BG18, border=0).grid(row=0, column=8, sticky=W)
Label(frame2_2, image=BG19, border=0).grid(row=0, column=9, sticky=W)
Label(frame2_2, image=BG110, border=0).grid(row=0, column=10, sticky=W)
Label(frame3, image=BG20, border=0).grid(row=0, column=0, sticky=W)

#Buttons
StrikeBtn = Button(frame2_1, text="STRIKE", width=6, padx=20, pady=20, command=strike)
StrikeBtn.grid(row=0, column=1, sticky=W)
MissBtn = Button(frame2_1, text="BALL", width=6, padx=20, pady=20, command=miss)
MissBtn.grid(row=0, column=2,   sticky=W)

UpdateTop()
ChangeNumber('Inning1', 0)
ChangeNumber('Runs', 0)

window.mainloop()


'''
while(Inning <= MaxInnings):
    FB = False;
    SB = False;
    TB = False;
    
    print("You are currently in the %d inning with %d outs, and gave up %d runs so far." % (Inning, Outs, Runs)) 
    print("A new hitter (%d) steps to the plate." % getNewHitter())
    while(Misses < 4 and Strikes <3):
        PitchCount += 1
        print("Pitch %d\nCount %d:%d" % (PitchCount, Misses, Strikes))
        Throw = input()
        if(Throw == 's'):
            Strikes += 1
        else:
            Misses += 1

    # update score
    if(Strikes == 3):
        print("STRIKEOUT!!!")
        Outs += 1
    else:
        print("HOMERUN!!!")
        Runs += 1

    if(Outs == 3):
        Inning += 1
'''
print("Total gamescore after %d innings:\n You gave up %d runs in %d pitches." % (Inning, Runs, PitchCount))
input()        

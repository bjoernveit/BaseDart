import random
from tkinter import *

def getNewHitter():
    n = 0
    for x in range(0, 10):
        n += random.randint(1,10)
    return(20 if n<20 else n)

def UpdateText(Label, NewText):
    Label.labelText = NewText


def strike():
    global Strikes    
    global Misses
    global PitchCount
    
    Strikes.set(Strikes.get() + 1)    
    PitchCount.set(PitchCount.get() + 1)
    
    if(Strikes.get() == 3):
        Strikes.set(0)
        Misses.set(0)
        
        global Hitter
        Hitter.set(getNewHitter())
        global Outs
        Outs.set(Outs.get() + 1)
        if(Outs.get() == 3):
            global Inning
            if(Inning.get() == MaxInnings):
                #Game End
                StrikeBtn['state']  = 'disabled'
                MissBtn['state']  = 'disabled'
            else:
                Inning.set(Inning.get() + 1)
            
            
            Outs.set(0)
    global Count
    Count.set('%d:%d' %(Misses.get(), Strikes.get()))

def miss():
    global Misses
    global Strikes
    global PitchCount
    
    PitchCount.set(PitchCount.get() + 1)
    Misses.set(Misses.get() + 1)
    if(Misses.get() == 4):
        Strikes.set(0)
        Misses.set(0)
        global Runs
        Runs.set(Runs.get()+ 1)
    global Count
    Count.set('%d:%d' %(Misses.get(), Strikes.get()))
#main

print("How Many innings do you want to play?")
MaxInnings = int(input())


window = Tk()

Inning = IntVar()
Runs = IntVar()
Count = StringVar()
Outs = IntVar()
Strikes = IntVar()
Misses = IntVar()
Hitter = IntVar()
PitchCount = IntVar()


#
# Setup Window
#
window.title('Basedart')

#Inning
Label(window, text='Inning: ', font="none 12 bold").grid(row=0, column=0, sticky=W)
InningLabel = Label(window, textvariable = Inning, font="none 12 bold")
InningLabel.grid(row=0,column=1, sticky=W)

#Runs
Label(window, text='Runs: ', font="none 12 bold").grid(row=1, column=0, sticky=W)
RunsLabel = Label(window, width=2, textvariable = Runs,font="none 12 bold")
RunsLabel.grid(row=1,column=1, sticky=W)

#Outs
Label(window, text='Outs: ', font="none 12 bold").grid(row=2, column=0, sticky=W)
OutsLabel = Label(window, width=2, textvariable = Outs, font="none 12 bold")
OutsLabel.grid(row=2,column=1, sticky=W)

#PitchCount
Label(window, text='PitchCount: ', font="none 12 bold").grid(row=3, column=0, sticky=W)
PitchCountLabel = Label(window, width=2, textvariable = PitchCount, font="none 12 bold")
PitchCountLabel.grid(row=3,column=1, sticky=W)

#Hitter
Label(window, text='Hitter: ', font="none 12 bold").grid(row=4, column=0, sticky=W)
HitterLabel = Label(window, width=2, textvariable = Hitter, font="none 12 bold")
HitterLabel.grid(row=4,column=1, sticky=W)

#Count
Label(window, text='Count: ', font="none 12 bold").grid(row=5, column=0, sticky=W)
CountLabel = Label(window, width=2, textvariable = Count, font="none 12 bold")
CountLabel.grid(row=5,column=1, sticky=W)

#Buttons
StrikeBtn = Button(window, text="Strike", width=6, command=strike)
StrikeBtn.grid(row=6, column=0, sticky=W)
MissBtn = Button(window, text="Miss", width=6, command=miss)
MissBtn.grid(row=6, column=1, sticky=W)

Inning.set(1)
Runs.set(0)
Count.set('0:0')
Outs.set(0)
Strikes.set(0)
Misses.set(0)
PitchCount.set(1)
Hitter.set(getNewHitter())


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
print("Total gamescore after %d innings:\n You gave up %d runs in %d pitches." % (Inning.get(), Runs.get(), PitchCount.get()))
input()        

# BaseDart
This project is a Dart checkout training game. You are a Baseball pitcher and try to give up as few runs as possible. 

# Rules
You are confronted with a hitter with a certain "hit power", you have to check out the power of the hitter in 3 trips (or any number of trips, depending on your skill).
If you do check out the "hit power" you have thrown a Strike, if you don't you get a Ball.

If you strike the hitter out you get an out, three outs end the inning, just as in real Baseball.
If you however throw 4 Balls, they get a run. In real Baseball this would only be a walk (hitter going to first base).

It is important to adjust the number of trips to the board for each "pitch", for your skill level as this game gets really frustrating if you just can't finisch out an Inning ever.
Right now the hitters are generated with values from 20-100, if you want to add 3 dart Checkouts to the equation, you would have to change it in the code.
Also note that the probability distribution of the numbers is generated using the sin() function form 0 to pi, that means 60(the middle) is the most likely and the further you get to the max/min values the more unlikely these are to be generated.
If you want to change this to suit your own practice needs, all you have to do is change up the getNewHitter() function at the top of the python file.

If you want to add 3 Dart checkouts you would also need to add an other digit to the Hitter display, you can just ask me though, as this part of the code is somewhat messi.

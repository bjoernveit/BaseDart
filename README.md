# BaseDart
This project is a Dart checkout training game. You are a Baseball pitcher and try to give up as few runs as possible. 

# Basic Rules (Version 2.0)
You are confronted with a hitter with a certain "hit power", you have to check out the power of the hitter in 3 trips (or any number of trips, depending on your skill).
If you do check out the "hit power" you have thrown a Strike, if you don't you get a Ball.

If you strike the hitter out you get an out, three outs end the inning, just as in real Baseball.
If you however throw 4 Balls, they get a run. In real Baseball this would only be a walk (hitter going to first base).

If you ever find yourself overthrowing, or only having one dart with an odd number left, I like to throw the remaning darts for the bullseye if I hit, I don't count this trip. This rule is mostly for always throwing 3 darts with purpose, but sometimes impacts the game. It's up to you if you want to play with or without it.

Check the Changelog, for newer Versions then 2.0

# Difficulty
It is important to adjust the number of trips to the board for each "pitch", for your skill level as this game gets really frustrating if you just can't finisch out an inning ever.
Right now the hitters are generated with values from 20-100, if you want to add 3 dart Checkouts to the equation, you would have to change it in the code.
Also note that the probability distribution of the numbers is generated using the sin() function form 0 to pi, that means 60(the middle) is the most likely and the further you get to the max/min values the more unlikely these are to be generated.
If you want to change this to suit your own practice needs, all you have to do is change up the getNewHitter() function at the top of the python file.

If you want to add 3 dart checkouts you would also need to add an other digit to the Hitter display, you can just ask me though, as this part of the code is somewhat messi.

# Version Changelog
## 1.0
This is just a bad looking V2.0, so essentially this should never be played. 

## 2.0 - Nice Looks
This is the first real version and is probably preffered by some people. Specically if you don't know anything about baseball. The Game is simple and consisten. If you strike somebody out he is out if, you give up to many balls they score.

## 3.0 - Bases and Hit-Probabilities
In this version bases and hit-probabilities added to the game. In other words it's a little more baseball. Before everytime you gave up 4 balls the offense would score a run, now they actually get a walk (go to first base). The hitter now also swings at the ball, regardless of you striking or balling. Yes, that means you can have the bases loaded, a full count, throwing a strike and still face a grandslam, but at the same time you might throw a ball and the hitter swings and misses. It is still very likely to get a strike/ball when you throw a strike/ball, but there is some variance to make it more interessting. When the ball is hit, the offense can get a single, double or homerun, so there are no triples. Baserunner all move the same amount on each hit.

## 3.1 Catch-Probabilities and perfect Strikes
I added the the possibility for the defense (us) to catch a hit ball, which leads to an out. There is also a 
"perfect"-Button, to reward you when you finished perfectly, as it was really frustrating playing perfect darts and getting scored on. If you hit the perfect button you will get a strike guaranteed. You should adjust the usage to you own skill level, for me I say it was perfect strike if I finish on the first trip to the board. 

I am aware that the game is currently to big, for a full hd resolution or less (as it has a height of 1100px), I will fix this at some point.

# Preview
![Preview of Game](https://raw.github.com/bjoernveit/BaseDart/master/preview.PNG)

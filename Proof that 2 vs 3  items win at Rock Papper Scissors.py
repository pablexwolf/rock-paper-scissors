import random
import time

#Numerical value of the items/objects, to make the score easier to track on a list.
rock = 0
paper = 1
scissors = 2

#Strategy would be your choice of items. Using just one, two or three, will tell you the probability of winning.
# Ideally, both will be random, and only stategy should be modified.

strategy = [0,1]
rival = [0, 1, 2]

#A list to keep track of the items/objects chosen during each match (rock, paper or scissors).
score = []

#Range will be how many matches will be occur. For a good sample, 100 matches are ideal, but the more, the better.
#Choices indicate what item (rock, paper or scissors) was chosen by each player.
#The append saves the choice on each match to a list called "score".

print("For a good sample, a total of 10,000  matches will be run.")
print()
time.sleep(3)
print("One Player will be using just two items randomly (Rock and Papper).")
time.sleep(2)
print("while the rival will be using the three possible items, also at random.")
print()
time.sleep(3)

for i in range (10000):
    choice1 = random.choice(strategy)
    choice2 = random.choice(rival)
    score.append((choice1, choice2))

#Table of values defining all possible win, tie and loose scenarios.
# E.g. (0, 2) is equivalent to stating "Rock beats Scissors" (rock, scissors), which is a winning scenario.
# (2, 0) is interpreted as scissors looses to rock, which consists a loosing scenario and counted towards how many times the strategy Lost.

winA = (0, 2)
winB = (1, 0)
winC = (2, 1)

tieA = (0, 0)
tieB = (1, 1)
tieC = (2, 2)

looseA = (2, 0)
looseB = (0, 1)
looseC = (2, 1)

#These variables store the count of times one of the three values of win was found, and the same is done for the tie and loose occurrrences.
Won = score.count(winA) + score.count(winB) + score.count(winC)
Tied = score.count(tieA) + score.count(tieB) + score.count(tieC)
Lost = score.count(looseA) + score.count(looseB) + score.count(looseC)

#Print how many times your strategy won, tied and lost against the rival.
print("Won", Won)
print("Tied", Tied)
print("Lost", Lost)
print()
time.sleep(2)

print("From the above results, you can conclude that the probability of winning goes up when you use 2 items only, when playing at least 3 matches of Rock Paper Scissors.")
print()
time.sleep(2)
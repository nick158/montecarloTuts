#!C:\Users\Nick\AppData\Local\Programs\Python\Python35
import random
import matplotlib
import matplotlib.pyplot as plt
#simple win / loss
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        #print (roll,"roll was 100, you lose.")
        return False
    elif roll <= 50:
        #print (roll, 'roll was 1-50, you lose')
        return False
    elif 100 > roll >=50:
        #print (roll, 'roll was 51-99, you win!')
        return True
#simple bettor that bets the same number every time
def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager

    # wager x
    wX = []
    #value Y
    vY = []
    #start at wager 1
    currentWager = 1
#if the current wager count is still less than # of times you
#want the dude to wager, then then keep on rolling that dice
    while currentWager <= wager_count:
        if rollDice():
            #if you win, add the wager to the value
            value += wager
            #track the wager count
            wX.append(currentWager)
            #track the overall value of the wager
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)
#increase by one for each time
        currentWager += 1
    #plot whatever you have for this bettor before running again in the external
    #loop
    plt.plot(wX,vY)

x = 0

while x<100:
    simple_bettor(10000,100,100000)
    x += 1
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()

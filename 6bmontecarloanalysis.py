import random
import matplotlib
import matplotlib.pyplot as plt
import time
#tutorial with tweak so it tracks the last best multiple so results only improve every time

lower_bust = 31.235
higher_profit = 63.208

# back to 1,000
sampleSize = 1000
startingFunds = 10000
wagerSize = 100
wagerCount = 100
#testing a new multiple range to speed up optimization
rand_low = 1.6
rand_high = 1.9
#create a multiple bettor. This guy tests a bunch
#of multiples and sees what works
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll >= 50:
        return True



def multiple_bettor(funds,initial_wager,wager_count):#,color):

    #add
    global multiple_busts
    global multiple_profits

    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():
                value += wager
                #wX.append(currentWager)
                #vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                #wX.append(currentWager)
            #    vY.append(value)
                if value <= 0:
                    multiple_busts += 1
                    break
        elif previousWager == 'loss':
            if rollDice():

                #### must change the multiple ####
                wager = previousWagerAmount * random_multiple
                if (value - wager) <= 0:
                    wager = value

                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * random_multiple
                if (value - wager) <= 0:
                    wager = value
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

                if value <= 0:
                    #change
                    multiple_busts += 1
                    break

        currentWager += 1

    #plt.plot(wX,vY)
    #####################
    if value > funds:
        #change
        multiple_profits+=1




def doubler_bettor(funds,initial_wager,wager_count,color):
    global doubler_busts
    global doubler_profits
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rollDice():
                value += wager
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value < 0:
                    currentWager += 10000000000000000
                    doubler_busts += 1
        elif previousWager == 'loss':
            if rollDice():
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value

                value += wager
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                value -= wager
                previousWager = 'loss'
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)

                if value <= 0:
                    currentWager += 10000000000000000
                    doubler_busts += 1

        currentWager += 1
    #plt.plot(wX,vY,color)
    #####################
    if value > funds:
        doubler_profits+=1

def simple_bettor(funds,initial_wager,wager_count,color):
    global simple_busts
    global simple_profits

    value = funds
    wager = initial_wager
    wX = []
    vY = []
    currentWager = 1
    while currentWager <= wager_count:
        if rollDice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

            if value <= 0:
                currentWager += 10000000000000000
                simple_busts +=1
        currentWager += 1
    plt.plot(wX,vY,color)
    if value > funds:
        simple_profits+=1
x = 0

#Doubler Bettor Bust Chances: 84.1457... so anything less than this... aaaand
#Doubler Bettor Profit Chances: 15.6355 ... aaaand better than this.
#10000 times, test
while x < 4000:

    ######## move this stuff in here for the math done in function.
    multiple_busts = 0.0
    multiple_profits = 0.0
    # now we're wanting to do 100 attempts to get a good sample #
    multipleSampSize = 100
    currentSample = 1
#create a new random multiple this run
    random_multiple = random.uniform(rand_low,rand_high)
    #random_multiple = 2.00
    #print((random_multiple
    # go through as many samples as you want
    while currentSample <= multipleSampSize:
        multiple_bettor(startingFunds,wagerSize,wagerCount)
        #add one to sample
        currentSample += 1
#percentage rate of failure is smaller than set amount and profits are highe
    if ((multiple_profits/multipleSampSize)*100.00 > higher_profit):
        print(('#################################################'))
        print(('found a winner, the multiple was:',random_multiple))
        print(('Lower Bust Rate Than:',lower_bust))
        print(('Higher profit rate than:',higher_profit))
        print(('Bust Rate:',(multiple_busts/multipleSampSize)*100.00))
        print(('Profit Rate:',(multiple_profits/multipleSampSize)*100.00))
        print(('#################################################'))
        recordMultiple = random_multiple
        lower_bust = multiple_busts/multipleSampSize * 100.00
        higher_profit = multiple_profits / multipleSampSize * 100.00
        time.sleep(5)
        #plt.show()
    else:
        pass


##        print(('####################################'))
##        print(('To beat:'))
##        print(('Lower Bust Rate Than:',lower_bust))
##        print(('Higher profit rate than:',higher_profit))
##        print(('Bust Rate:',(multiple_busts/multipleSampSize)*100.00))
##        print(('Profit Rate:',(multiple_profits/multipleSampSize)*100.00))
##        print(('####################################'))
##
##        #clears the figure
##        plt.clf()


    x+=1

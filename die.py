import random

# dies
die1 = 0
die2 = 0
die3 = 0
die4 = 0
die5 = 0

#die backside
die1Back = 0
die2Back = 0
die3Back = 0
die4Back = 0
die5Back = 0

# begin text for programm
def beginText():
    print("Hello and welcom to the die game.")
    print("Type how many dies u want to use with a max of 5.\n")
    dieAmount = int(input())
    print("\n")
    throwDie(dieAmount)

# function to throw the die(s)
def throwDie(amount):

    #throw first die
    if amount >= 1:
        die1 = randomDie()
        die1Back = checkBack(die1)
        print("your throw: ", die1)
        #print("\n")
        print("the back of the die: ", die1Back)
        print("\n")
    #throw second die
    if amount >= 2:
        die2 = randomDie()
        die2Back = checkBack(die2)
        print("your throw: ", die2)
        #print("\n")
        print("the back of the die: ", die2Back)
        print("\n")
    #throw third die
    if amount >= 3:
        die3 = randomDie()
        die3Back = checkBack(die3)
        print("your throw: ", die3)
        #print("\n")
        print("the back of the die: ", die3Back)
        print("\n")
    #throw fourth die
    if amount >= 4:
        die4 = randomDie()
        die4Back = checkBack(die4)
        print("your throw: ", die4)
        #print("\n")
        print("the back of the die: ", die4Back)
        print("\n")
    #throw fifth die
    if amount == 5:
        die5 = randomDie()
        die5Back = checkBack(die5)
        print("your throw: ", die5)
        #print("\n")
        print("the back of the die: ", die5Back)
        print("\n")
    throwAgain()

#generate the random number for the die
def randomDie():
    randomNumber = random.random()
    dieNumber = 0
    if randomNumber <= 0.1666:
        dieNumber = 1
    elif randomNumber <= 0.3332:
        dieNumber = 2
    elif randomNumber <= 0.4998:
        dieNumber = 3
    elif randomNumber <= 0.6664:
        dieNumber = 4
    elif randomNumber <= 0.833:
        dieNumber = 5
    else:
        dieNumber = 6
    return dieNumber

#connect the back to the number that is thrown
def checkBack(die):
    back = 0
    if die == 1:
        back = 6
    if die == 2:
        back = 5
    if die == 3:
        back = 4
    if die == 4:
        back = 3
    if die == 5:
        back = 2
    if die == 6:
        back = 1
    return back

#ask if player wants to throw again
def throwAgain():
    print("Do you want to throw again (y/n). \n")
    answer = input()
    if answer == "y":
        beginText()
    elif answer == "n":
        exit()
    else:
        print("Please enter a valid answer.\n")
        throwAgain()


#begin programm
beginText()

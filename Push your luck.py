#Made by Colin Campbell
#This script is made for a game on Cool Math Games
#In the game a wheel 1-13 is spun and you get how ever many points you land on
#After the initial spin you have to guess higher or lower
#If you are correct you get what number it lands on
#If you are incorrect you lose all of your points
#At any point you are able to cash out
#As higher values give you more points the script gives expected value
#Expected value is just expected amount of points if higher is rolled
#FUTURE PLANS: Implent recomendations on when to cash out.

value = 0
userInput = "Go"
choicesLeft = [1,2,3,4,5,6,7,8,9,10,11,12,13]





while True:
    userInput = int(input("What value did the whell land on?: "))
    if userInput == 0:
        print("reset")
        choicesLeft = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        userInput = int(input("What value did the whell land on?: "))

    #removing the value it landed on 
    choicesLeft.remove(userInput)
    #finds number of numbers in list
    numNumbers = len(choicesLeft)

    #makes two new lists of the new values
    lower = []
    higher = []

    #finds the prob of each value
    probability = 1 / numNumbers
    #assigns each list the correct values
    for i in range(numNumbers):
        #Goes through each number, currentNumber is the one its looking at right now
        currentNumber = choicesLeft[i]
        if currentNumber < userInput:
            lower.append(currentNumber)
        if currentNumber > userInput:
            higher.append(currentNumber)


    #calculate the probability of each
    lengthLower = len(lower)
    lengthHigher = len(higher)

    probLower = lengthLower / numNumbers
    probHigher = lengthHigher / numNumbers


    #finding expected value for lower and higher
    #lower
    lowerTotalValue = 0
    higherTotalValue = 0
    for i in range(lengthLower):
        #setting current value in lower list
        currentNumber = lower[i]
        #summing up every value (prob * value)
        lowerTotalValue += currentNumber * probability
    for i in range(lengthHigher):
        currentNumber = higher[i]
        higherTotalValue += currentNumber * probability
    
        




    #printing each list
    print("Lower: {}".format(lower))
    print("Higher: {}".format(higher))
    print("Total list: {}".format(choicesLeft))
    print("Probability of lower: {}".format(probLower))
    print("Probability of Higher: {}".format(probHigher))
    print("The expected value for lower: {}".format(lowerTotalValue))
    print("The expected value for higher: {}".format(higherTotalValue))
    

    




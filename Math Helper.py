import math
import random
##############################
# Full name: Maxim Melkonian #
# Student number:  300019652 #
# Course: IT1 1120           #
# Assignment Number: 2       #
################################################################################
#Function
def performTest(flag:int,n:int)->int:
    """ (int,int) -> int
    Preconditions:
            flag must be either 0 or 1
            n cannot be a negative number
    Returns the number of questions answered correctly
 """
    correctAnswers=0
    if flag==0:
        for i in range(n):
            intOne = random.randrange(10)
            intTwo = random.randrange(10)
            """print(str(intOne) + " - " + str(intTwo))"""
            userInput = int(input("What is your answer? "))
            if userInput == (intOne-intTwo):
                correctAnswers+=1
            return correctAnswers
    elif flag==1:
        for i in range(n):
            intOne = random.randrange(10)
            intTwo = random.randrange(10)
            print(str(intOne) + "^" + str(intTwo))
            userInput = int(input("What is your answer? "))
            if userInput == pow(intOne, intTwo):
                correctAnswers+=1
        return correctAnswers

userName = input("What is your name?: ")
revisedUserName = userName.strip()
flag = int(input("What would you like to practice? \n 0: subtraction \n 1: exponentiation \n"))
practise = int(input("How many practise questions would you like? "))
if practise<=0:
    print("You're all ready for the test! Good luck!")
else:
    h = performTest(flag,practise)
    if ((h/practise)*100)>=90:
        print("Congratulations " + revisedUserName + "! You'll probably get an A tomorrow. Now go eat your dinner and go to sleep. Goodbye " + revisedUserName + "!")
    elif 70<=((h/practise)*100)<90:
        print("You did well " + revisedUserName + ", but I know you can do better. Goodbye " + revisedUserName + "!")
    elif 70>((h/practise)*100):
        print("I think you need more practice " + revisedUserName + ". Goodbye "+revisedUserName + "!")


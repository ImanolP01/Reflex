#### Reflex Game
import os

### stores the attempts in dictionary
attempts = {}

### gets inputs and stores in attempts dictionary
repeat = True
while(repeat):
    name = input("What is your name? ")
    graduation = input("What year did you graduate? ")
    time = input("#: ")


    attempts[name] = graduation
    attempts[name] = time


    print(attempts)

    try_again = input("Press anything but 0 to try again. ")
    if try_again == "0":
        repeat = False
    else:
        ###clear screen 
        os.system('cls')
        repat = True
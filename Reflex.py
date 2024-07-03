#### Reflex Game
import os
import time
import random
import keyboard
import string
from datetime import datetime



timer=random.randint(2,5)

txtfile = open("inputs.txt", "r")
data = str(txtfile.readlines())
txtfile.close()


### credit to charlie for helping us retrieve player data back
attempts = []
for c in data:
    if c == "{":
        index = data.index(",")
        index -= 2
        name = ""
        while data[index] != "\'":
            name = data[index] + name
            index -= 1

        data = data[data.index(",") + 1:]
        grad_year = ""
        index = data.index(",")
        index -= 2
        while data[index] != "\'":
            grad_year = data[index] + grad_year
            index -= 1

        data = data[data.index(",") + 1:]
        index = data.index(",")
        index -= 2
        date = ""
        while data[index] != "\'":
            date = data[index] + date
            index -= 1

        data = data[data.index(",") + 1:]
        time1 = ""
        index = data.index("}")
        index -= 1
        while data[index] != " ":
            time1 = data[index] + time1
            index -= 1

        try:
            data = data[data.index(",") + 1:]
        except:
            ...
        attempts.append({'Name':name, 'Graduation':grad_year, 'Date':date, 'Time': float(time1)})
        


attempts = sorted(attempts, key=lambda x: x['Time'])


counter = 1
repeat = True
while(repeat):
    current_time=str(datetime.now())
    print(current_time)

    name = input("What is your name? ")
    graduation = input("What year did you graduate? ")
    #time1 = int(input("#: "))
    time1 = 0

    print("okay get ready to play, click the character displayed as soon as it appears")
    time.sleep(2)
    print("Hmmm I wonder when it'll show up")
    time.sleep(timer)
    print("Now!!!")
    x=random.choice(string.ascii_letters)
    z=x.lower()
    print(f"The letter you need to press is {z}")
    key_no_press=True
    start_time=time.time()
    while(key_no_press):
        if (keyboard.is_pressed (z)):
            print("You pressed the right one lets go!")
            end_time=time.time()
            time1=end_time-start_time
            print(f"Your total time it took to press the key was {time1:.2f} seconds")
            key_no_press=False
            break

    user = {"Name": name, "Graduation": graduation, "Date": current_time, "Time":float(f"{time1:.2f}")}

    attempts.append(user)
    

    attempts = sorted(attempts, key=lambda x: x['Time'])

    
    

    if len(attempts) > 10:
        attempts = attempts[0:10]
    
 
    


    
    #### txt file stuff
    txtfile = open("inputs.txt", "w")
    txtfile.write(str(attempts))
    txtfile.close()
    
    print("Score board: ")
    print(attempts)
    filler = input("Press enter: ")
    try_again = input("Press anything but 0 to try again. ")
    if try_again == "0":
        repeat = False
    else:
        ###clear screen 
        os.system('cls')
        repat = True
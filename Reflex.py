#### Reflex Game
import os
import time
import random
import keyboard
import string


timer=random.randint(2,5)

txtfile = open("inputs.txt", "r")
data = str(txtfile.readlines())
txtfile.close()


attempts = data


print(attempts)

counter = 1
repeat = True
while(repeat):


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

    user = { "Name": name, "Graduation": graduation, "Time":float(f"{time1:.2f}")}

    attempts.append(user)

  
    print("Counter: ", counter)
    

    if counter > 9:
        var = attempts[9]['Time'] 
        if var > time1:
            attempts.pop(9)
    
    
    ### sorts dictionaries in list based on Time 
    
    counter += 1

    
    #### txt file stuff
    txtfile = open("inputs.txt", "w")
    txtfile.write(str(attempts))
    txtfile.close()
   
    attempts = sorted(attempts, key=lambda x: x['Time'])
    print(attempts)
      
    try_again = input("Press anything but 0 to try again. ")
    if try_again == "0":
        repeat = False
    else:
        ###clear screen 
        os.system('cls')
        repat = True
#### Reflex Game
import os

attempts = [
     {
        "Name": "bob",
        "Graduation": "1988",
        "Time": 3
    }
]

previousUser = "bob"
counter = 1
repeat = True
while(repeat):

    name = input("What is your name? ")
    graduation = input("What year did you graduate? ")
    time = int(input("#: "))

    user = { "Name": name, "Graduation": graduation, "Time": time }

    attempts.append(user)

  
    print("Counter: ", counter)

    
    if counter > 9:
        var = attempts[9]['Time'] 
        if var > time:
            attempts.pop(9)
    
    
    ### sorts dictionaries in list based on Time 
    attempts = sorted(attempts, key=lambda x: x['Time'])
    print(attempts)
    counter += 1
      
    try_again = input("Press anything but 0 to try again. ")
    if try_again == "0":
        repeat = False
    else:
        ###clear screen 
        os.system('cls')
        repat = True
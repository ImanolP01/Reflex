#### Reflex Game
import os

attempts = {
    "bob" : {
        "Graduation": "1988",
        "Time": 3
    }
}

previousUser = "bob"
counter = 0
repeat = True
while(repeat):

    name = input("What is your name? ")
    graduation = input("What year did you graduate? ")
    time = int(input("#: "))

    user = { name : { "Graduation": graduation, "Time": time }}

    attempts.update(user)

    previousTime = attempts[previousUser]["Time"]
    if counter > 10:
        if time < previousTime:
            del attempts[previousUser]
            previousUser = name
            previousTime = time
        elif time > previousTime:
            del attempts[name]

    counter += 1
    print(counter)

    for x, user in attempts.items():
        print(x)
        for time in user.items():
            print(time)

    print(attempts)

    try_again = input("Press anything but 0 to try again. ")
    if try_again == "0":
        repeat = False
    else:
        ###clear screen 
        os.system('cls')
        repat = True
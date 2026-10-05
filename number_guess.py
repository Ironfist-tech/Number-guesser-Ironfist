# number guess
import random
import time

num = random.randint(1,50)
answer = int
in_put = str

print("Game starting.", end="")
time.sleep(0.5)

print("\rGame starting..", end="")
time.sleep(0.5)

print("\rGame starting...", end="")
time.sleep(0.5)

print("\rGame starting.   ")
time.sleep(0.5)

print("GAME STARTED!!")


while True:

    in_put = input("Choose(hard/med/ez):")

    if in_put == "ez":
        num = random.randint(1,10)
    elif in_put == "med":
        num = random.randint(1,50)
    elif in_put == "hard":
        num = random.randint(1,100)
    else:
        print("(type hard or med or ez only)")

    for x in range(1,6):
        try:
            answer = int(input("Guess The number!: "))
        except ValueError:
            print("You dummy XD type a number!")

        if answer > num:
            print("Lower!")

        if answer < num:
            print("higher!")

        if answer == num:
            print("Good Job!! You got the number right")
            in_put = str(input("Whould you like to do that again?(y/n):"))
            break

        if x == 5:
            print("It looks like you ran out of attemts!")
            in_put = str(input("Whould you like to do that again?(y/n):"))
            break


    if in_put == "y":
        continue
    elif in_put == "n":
        break
            

        
            

        

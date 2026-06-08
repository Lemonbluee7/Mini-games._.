import random
num=random.randint(0,100)

print("guess the number GAME!!")

while True:
    try:
        guess= int(input("What's your guess??"))
        if guess > num:
            print("too big")
        elif guess < num:
             print("too small")
        else:
                print("you got it!!")
                break
    except ValueError:
         print("Please enter a valid number >:(")
    
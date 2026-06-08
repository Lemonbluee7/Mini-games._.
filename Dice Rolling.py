import random

while True:
    choise = input("Do you wanna roll the dice? [Y/N]")
    if choise== 'Y':
        num1= random.randint(1,6)
        num2= random.randint(1,6)
        print (f'({num1},{num2})')     
    elif choise== 'N':
        print('Thanks for playing!')
        break
    else:
     print("Not recognised character")

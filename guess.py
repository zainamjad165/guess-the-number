import random

def guess(x):
    random_number=random.randint(1,x)
    print(random_number)
    guess=0
    while guess != random_number:
        guess=int(input(f"guess the number between 1 to {x}:  "))
        if guess > random_number:
            print ("the guessed number is too high")
        elif guess < random_number:
            print ("the guessed number is too low")
    print ("congrats you have guessed the number corect!")

guess(10)                

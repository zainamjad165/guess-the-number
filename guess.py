import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f"Guess a number between 1 to {x}:  "))
        if guess > random_number:
            print ("This number is too high")
        elif guess < random_number:
            print ("This number is too low")
    print ("Congrats! Your guess is correct.")

guess(10)                

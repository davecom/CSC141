from random import randint

answer = randint(1, 100)
guess = -1

while guess != answer:
    guess = input("What number do you think it is?")
    guess = int(guess)
    if guess < answer:
        print("Too low!")
    elif guess > answer:
        print("Too high!")
print("You won!")

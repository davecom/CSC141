# Break Version

age = -1
while True:
    age = input("What is the person's age?")
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        print("You're free")
    elif age <= 12:
        print("You're $10")
    else:
        print("You're $15")

# While condition version

age = -1
while age != -5:
    age = input("What is the person's age?")
    age = int(age)
    if age < 3:
        print("You're free")
    elif age <= 12:
        print("You're $10")
    else:
        print("You're $15")

# activate version

age = -1
active = True
while active:
    age = input("What is the person's age?")
    if age == "quit":
        active = False
    else:
        age = int(age)
        if age < 3:
            print("You're free")
        elif age <= 12:
            print("You're $10")
        else:
            print("You're $15")
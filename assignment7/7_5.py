# A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

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
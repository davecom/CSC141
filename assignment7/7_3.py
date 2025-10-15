# Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("What number do you want?")
number = int(number)

if number % 10 == 0:
    print("It's a multiple of 10")
else:
    print("It's not a multiple of 10")

# 16 % 5 == 1
# 18 % 5 == 3
# 15 % 5 == 0
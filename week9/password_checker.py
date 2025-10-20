
def long_enough(password):
    return len(password) >= 15
    # if len(password) >= 15:
    #     return True
    # else:
    #     return False

def has_special(password):
    for c in password:
        if c in "$^%&*()@#!":
            return True
    return False

def has_number(password):
    for c in password:
        if c.isdigit():
            return True
    return False

def has_capital(password):
    for c in password:
        if c.isupper():
            return True
    return False

def has_lower(password):
    for c in password:
        if c.islower():
            return True
    return False

# at least 15 characters
# should have a special character: $^%&*()@#!
# should have a number
# should have a capital letter
# should have a lower case letter
def password_check(password):
    return long_enough(password) and has_special(password) and has_number(password) and has_capital(password) and has_lower(password)

def main():
    print("Please enter a password with 15 characters, a special character, a number, and both cases:")
    password = input()
    if password_check(password):
        print("Good password")
    else:
        print("Invalid password")

main()
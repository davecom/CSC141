import random
words = ["apple", "python", "tree", "computer", "dog", "grapes"]
word = "tree".upper()
#word = random.choice(words).upper()

scrambled = ["_" for letter in word]
print("".join(scrambled))

while "".join(scrambled) != word:
    print("Guess a letter.")
    guess = input()
    guess = guess.upper()
    if guess in word:
        letter_index = word.index(guess)
        scrambled[letter_index] = guess
        rest = word[(letter_index + 1):]
        print(rest)
        if guess in rest:
            print("found it")
            second_letter_index = rest.index(guess)
            print(second_letter_index)
            scrambled[letter_index + second_letter_index + 1] = guess
    else:
        print("Not in word.")
    print("".join(scrambled))
    
print("Game Over")
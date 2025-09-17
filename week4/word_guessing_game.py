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
        index = 0
        for letter in word:
            if letter == guess:
                scrambled[index] = letter
            index += 1 
    else:
        print("Not in word.")
    print("".join(scrambled))
    
print("Game Over")
import random

# variables: answer, numbers to add, score

score = 0
keep_playing = True

while keep_playing:
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    print(f"What is {number1} + {number2}?")
    user_answer = input()
    user_answer = int(user_answer)
    right_answer = number1 + number2
    if user_answer == right_answer:
        print("You got it right!")
        score += 1
    else:
        print(f"Wrong! The right answer is {right_answer}")
        score -= 1
    print(f"Your score is {score}")
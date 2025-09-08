import random
answers = ["yes", "no", "maybe", "unlikely", "perhaps"]
print("What do you want to know?")
question = input()
answer = random.choice(answers)
print(answer)
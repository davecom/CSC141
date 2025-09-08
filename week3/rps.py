import random

keep_playing = True

computer_wins = 0
human_wins = 0

while keep_playing:
    answers = ["rock", "paper", "scissors"]
    computer_answer = random.choice(answers)
    print("Do you want to play rock, paper, or scissors? Or quit?")
    human_answer = input()
    human_answer = human_answer.lower()

    if human_answer == "quit":
        break

    if human_answer not in answers:
        print("That's not a valid answer.")
        exit()

    print(f"Computer played {computer_answer}")

    if computer_answer == human_answer:
        print("Nobody wins!")
    elif computer_answer == "rock" and human_answer == "scissors":
        computer_wins += 1
        print("Computer wins!")
    elif computer_answer == "paper" and human_answer == "rock":
        computer_wins += 1
        print("Computer wins!")
    elif computer_answer == "scissors" and human_answer == "paper":
        computer_wins += 1
        print("Computer wins!")
    else:
        human_wins += 1
        print("Human wins!")
    
    print(f"Human Score {human_wins} Computer Score {computer_wins}")
print("Thanks for playing!")
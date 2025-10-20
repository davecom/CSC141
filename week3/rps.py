import random

def human_play():
    print("Do you want to play rock, paper, or scissors? Or quit?")
    human_answer = input()
    human_answer = human_answer.lower()
    return human_answer

# 0 if tie, 1 if computer wins, -1 if human wins
def compare_plays(human_answer, computer_answer):
    if computer_answer == human_answer:
        return 0
    elif computer_answer == "rock" and human_answer == "scissors":
        return 1
    elif computer_answer == "paper" and human_answer == "rock":
        return 1
    elif computer_answer == "scissors" and human_answer == "paper":
        return 1
    else:
        return -1

def main():
    keep_playing = True

    computer_wins = 0
    human_wins = 0

    while keep_playing:
        answers = ["rock", "paper", "scissors"]
        computer_answer = random.choice(answers)
        human_answer = human_play()    

        if human_answer == "quit":
            break

        if human_answer not in answers:
            print("That's not a valid answer.")
            exit()

        print(f"Computer played {computer_answer}")

        result = compare_plays(human_answer, computer_answer)
        if result == 1:
            computer_wins += 1
        elif result == -1:
            human_wins += 1
       
        
        print(f"Human Score {human_wins} Computer Score {computer_wins}")
    print("Thanks for playing!")

# top level
main()
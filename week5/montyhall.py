from random import randint

def door_select():
    prize_door = randint(0, 2)
    guess_door = randint(0, 2)
    print(f"prize door: {prize_door}")
    print(f"original guess door: {guess_door}")
    return (prize_door, guess_door)

def find_takeaway(prize_door, guess_door):
    takeaway_door = randint(0, 2)
    while takeaway_door == prize_door or takeaway_door == guess_door:
        takeaway_door = randint(0, 2)
    print(f"takeaway door: {takeaway_door}")
    return takeaway_door

def switch_door(doors, takeaway_door, guess_door):
    del doors[takeaway_door]
    index = 0
    for door in doors:
        if door == guess_door:
            del doors[index]
            break
        index += 1

def main():
    win_count = 0
    trials = 1000
    for trial in range(trials):
        # setup
        doors = [0, 1, 2]

        # play the game
        prize_door, guess_door = door_select()
        takeaway_door = find_takeaway(prize_door, guess_door)
        switch_door(doors, takeaway_door, guess_door)
        guess_door = doors[0]

        # show the result
        print(f"final guess door: {guess_door}")

        # check if they found the prize
        if guess_door == prize_door:
            print("You found the prize.")
            win_count += 1
        else:
            print("You did not find the prize")
    print(f"Winning percentage: {win_count / trials}")

main()
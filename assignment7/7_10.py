vacation_spots = {}
response = ""
while response != "quit":
    print("Where do you want to go? Or type quit to end.")
    response = input()
    if response in vacation_spots:
        vacation_spots[response] += 1
    else:
        vacation_spots[response] = 1

print("Here are the poll results:")
for spot in vacation_spots:
    print(f"{vacation_spots[spot]} people selected {spot}")
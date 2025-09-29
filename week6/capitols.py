from random import choice

capitols = {"United States": "Washington",
            "Canada": "Ottawa",
            "Japan": "Tokyo",
            "France": "Paris"}

country = choice(list(capitols.keys()))

print(f"What is the capitol of {country}?")
answer = input()
if answer == capitols[country]:
    print("You got it!")
else:
    print(f"No, the answer was {capitols[country]}")
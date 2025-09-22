print("Are you providing celsius (C) or fahrenheit (F)?")
scale = input()
scale = scale.upper()
print("How many degrees?")
degrees = input()
degrees = int(degrees)
# °F = (°C × 9/5) + 32
# °C = (°F − 32) x 5/9
if scale == "C":
    fahrenheit = (degrees * (9 / 5)) + 32
    print(fahrenheit)
elif scale == "F":
    celsius = (degrees - 32) * (5 / 9)
    print(celsius)
else:
    print("That's not a valid scale.")

# temperature = 10
# humidity = 40
# windspeed = 10

# storm = (humidity > 70 and windspeed > 50) or (temperature < 32 and humidity > 60 and windspeed > 50)
# storm = True
# print(storm)

# if storm:
#     print("There's a serious storm")
# else:
#     print("It's mild right now")

# animals = ["cat", "cow", "dog"]
# if animals:
#     print("there are animals")

# animals.pop()
# animals.pop()
# animals.pop()

# if animals:
#     print("there are animals")
# else:
#     print("there are no animals")




# if temperature == 85:
#     print("It's really hot")
# elif temperature > 70:
#     print("It's warm today")
# elif temperature > 50:
#     print("It's a little chilly")
# else:
#     print("It's cold today")

# if temperature > 80:
#     print("It's a good day to go sailing")

# 4-1
pizzas = ["pepperoni", "pineapple", "sicilian"]
for pizza in pizzas:
    print(f"{pizza} is a type of pizza")
print("I like pizza ocassionally.")

# 4-2
animals = ["dog", "cow", "chicken"]
for animal in animals:
    print(f"{animal} is a type of animal")
print("All of these animals live on a farm.")

# 4-3


#4-4
#for i in range(1, 100000):
#    print(i)

print(min(range(1, 100000 + 1)))

# 4-7
threes = list(range(3, 30, 3))
for three in threes:
    print(three)

#4-8
cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)
    print(i ** 3)
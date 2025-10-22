def greet(name):
    print(f"Hi, {name}")

def greet2(name="Joe", times=1):
    for time in range(times):
        print(f"Hi, {name}")

greet2()

# people = ["Joe", "Mary", "Sal"]
# for person in people:
#     print(f"Hi, {name}")
    # greet(person)

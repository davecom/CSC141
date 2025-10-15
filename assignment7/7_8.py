sandwich_orders = []
while True:
    print("Name of a sandwich or quit")
    name = input()
    if name == "quit":
        break
    sandwich_orders.append(name)

finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"Made {sandwich}")
    finished_sandwiches.append(sandwich)
print(f"We made {finished_sandwiches}")
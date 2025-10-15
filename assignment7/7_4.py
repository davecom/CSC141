toppings = []
new_topping = ""
while new_topping != "quit":
    new_topping = input("What topping do you want to add?")
    toppings.append(new_topping)
print(f"Your toppings: {toppings}")
def total(costs):
    t = 0
    for cost in costs:
        t += cost
    return t

def calculate_tip(total, tip_percentage):
    tip_amount = total * tip_percentage
    return tip_amount

def calculate_tax(total):
    tax_amount = total * 0.06
    return tax_amount

def bill(check_items, tip_percentage):
    costs = []
    for item in check_items:
        cost = check_items[item]
        print(f"{item} \t {cost}")
        costs.append(cost)
    item_total = total(costs)
    print(f"Total Cost: {item_total}")
    tip_amount = calculate_tip(item_total, tip_percentage)
    print(f"Tip: {tip_amount}")
    tax_amount = calculate_tax(item_total)
    print(f"Tax: {tax_amount}")
    owed = item_total + tip_amount + tax_amount
    print(f"Amount Due: {owed}")

def main():
    check_items = {"Filet Mignon" : 56.00, "Trout" : 35.65, "Coffee" : 3.00, "Cake" : 5.00}
    bill(check_items, 0.20)

main()
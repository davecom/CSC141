names = ["Brian", "Sarah", "Mary", "Jillian"]
salaries = [25, 20, 40, 50]
ages = [45, 20, 50, 30]

# for i in range(len(names)):
#     print(f"Name: {names[i]} Salary: {salaries[i]} Age: {ages[i]}")

# print(names[0])

employees = {
    "Brian" : {"salary": 25, "age": 45},
    "Sarah" : {"salary": 20, "age": 20},
    "Mary" : {"salary": 40, "age": 50},
    "Jillian" : {"salary": 50, "age": 30}
}

employees["Julie"]

# print(employees["Sarah"])
# print(employees["Sarah"]["salary"])

for employee in employees:
    data = employees[employee]
    print(employee)
    print(data["salary"])
    print(data["age"])

populations = {
    "United States" : 340000000,
    "Canada" : 40000000,
    "Japan" : 120000000,
}

populations_list = [340000000, 400000000, 1200000000]
# print(populations["United States"])
# print(populations_list[0])

populations["United Kingdom"] = 70000000
# print(populations)
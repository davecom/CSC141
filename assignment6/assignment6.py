# 6-1
print("6-1")
person = {"first_name" : "Sarah",
          "last_name" : "Smith",
          "age" : 27,
          "location" : "New York"}
for property in person:
    print(f"{property} : {person[property]}")

# 6-2
print("6-2")
favorite_numbers = {"John" : 24, "Shaq" : 4, "Ida" : 2, "Michael" : 7}
for person in favorite_numbers:
    print(f"{person}'s favorite number is {favorite_numbers[person]}")

#6-3 & 6-4
print("6-3 and 6-4")
glossary = {"integer" : "whole number in programming", 
            "string" : "type for holding text", 
            "boolean" : "type that can only be True or False typically used for conditionals",
            "list" : "data structure for holding a collection of ordered items",
            "loop" : "way of repeating the same block of code multiple times"}
glossary["float"] = "a number with a decimal point"
for term in glossary:
    print(f"{term}\n{glossary[term]}")

#6-5
print("6-5")
rivers = {"Mississippi" : "USA", "Amazon" : "Brazil", "Thames" : "UK", "Seine" : "France", "Tigris" : "Iraq"}
for river in rivers:
    print(f"The {river} river runs through {rivers[river]}")

#6-6
print("6-6")
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
should_take = ["john", "sarah", "abby"]
for name in should_take:
    if name in favorite_languages:
        print(f"Thanks for taking the poll, {name}")
    else:
        print(f"You should take the poll, {name}")

#6-7
print("6-7")
person1 = {"first_name" : "Sarah",
          "last_name" : "Smith",
          "age" : 27,
          "location" : "New York"}
person2 = {"first_name" : "Tara",
          "last_name" : "Johnson",
          "age" : 29,
          "location" : "Boston"}
person3 = {"first_name" : "Matt",
          "last_name" : "Brooks",
          "age" : 25,
          "location" : "Philadelphia"}
people = [person1, person2, person3]
for individual in people:
    print(individual)

# 6-8
print("6-8")
pet1 = {"name" : "Garfield", "type" : "dog", "owner" : "Jon"}
pet2 = {"name" : "Socks", "type" : "cat", "owner" : "Bill"}
pet3 = {"name" : "Hallie", "type" : "dog", "owner" : "Rebecca"}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(pet)

# 6-9
print("6-9")
favorite_places = {"John" : "Carolina", "Abby" : "Paris", "Terrence" : "Milan"}
for name in favorite_places:
    print(f"{name}'s favorite place is {favorite_places[name]}")

# 6-10
print("6-10")
favorite_numbers2 = {"John" : [24, 7], "Shaq" : [4, 30, 21], "Ida" : [2], "Michael" : [7, 50]}
for person in favorite_numbers2:
    print(f"{person}'s favorite numbers are {favorite_numbers2[person]}")

#6-11 & 6-12
print("6-11 and 6-12")
cities = {"NYC" : {"population" : 8000000, "state" : "New York", "country" : "USA", "fact" : "largest city in USA"},
          "Boston" : {"population" : 1000000, "state" : "Massachusetts", "country" : "USA", "fact" : "home of the Celtics"},
          "Baltimore" : {"population" : 1000000, "state" : "Maryland", "country" : "USA", "fact" : "home of Edgar Allen Poe"}}
for city in cities:
    print(f"{city}, {cities[city]['state']}, {cities[city]['country']} has a population of {cities[city]['population']}. One fact about it is that it's {cities[city]['fact']}")
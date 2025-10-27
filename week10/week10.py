class LivingThing:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def breathe(self):
        print(f"{self.name} is breathing")

class Person(LivingThing):
    def __init__(self, name, age, phone):
        self.phone = phone
        super().__init__(name, age)

class Pet(LivingThing):
    def __init__(self, type, name, age):
        self.type = type
        self.veterinarian = None
        super().__init__(name, age)
    
    def age_in_dog_years(self):
        if self.type == "dog":
            return self.age * 7
        else:
            print("Not a dog")
            return None
    
    def set_veterinarian(self, v):
        self.veterinarian = v

p1 = Pet("dog", "Spot", 3)
p2 = Pet("cat", "Garfield", 5)
p3 = Pet("bird", "Sarah", 7)
p1.name = "Joe"
p1.breathe()
print(f"There is a {p1.type} named {p1.name}")
print(p1.age_in_dog_years())
print(p2.age_in_dog_years())
v1 = Person("Dr. Smith", 50, "555-5555")
v1.breathe()
p1.set_veterinarian(v1)
print(f"It's an emergency, call the vet for {p1.name} at {p1.veterinarian.phone}")
# 9-1 & 9-4

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open")

    def set_number_served(self, n):
        self.number_served = n
    
    def increment_number_served(self, n):
        self.number_served += n

restaurant = Restaurant("Austins", "Steakhouse")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.open_restaurant()
restaurant.describe_restaurant()

# 9-2
r1 = Restaurant("Chipotle", "Fast Food")
r2 = Restaurant("Peking Sun", "Chinese")
r3 = Restaurant("Sakura", "Sushi")
r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()
r1.set_number_served(5)
r1.increment_number_served(3)
print(f"{r1.restaurant_name} has served {r1.number_served}")

# 9-3 & 9-5
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} has email {self.email}")
    
    def greet_user(self):
        print(f"Welcome, {self.first_name}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

u1 = User("John", "Smith", "sdf@sdf.com")
u2 = User("Sarah", "Abbott", "abs@abs.com")
u1.describe_user()
u1.greet_user()
u2.describe_user()
u2.greet_user()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
print(f"{u1.first_name} has logged in {u1.login_attempts} times")
u1.reset_login_attempts()
print(f"{u1.first_name} has logged in {u1.login_attempts} times")

# 9-6

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type)
    
    def display_flavors(self):
        print(f"{self.restaurant_name}'s flavors are {self.flavors}")

ics = IceCreamStand("Mollys", "Ice Cream", ["vanilla", "chocolate", "strawberry"])
ics.display_flavors()

# 9-7 & 9-8
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, email, privileges):
        self.privileges = privileges
        super().__init__(first_name, last_name, email)

p = Privileges(["can add post", "can ban user"])
a = Admin("John", "Smith", "sdf@sdf.com", p)
a.privileges.show_privileges()

# 9-9

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")



my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()

# 9-13
from random import randint
class Die:
    def __init__(self, sides):
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))

d10 = Die(10)
d20 = Die(20)
for x in range(10):
    d10.roll_die()
    d20.roll_die()

# 9-14
lottery_parts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D"]
from random import choice
winning_combo = [choice(lottery_parts), choice(lottery_parts), choice(lottery_parts), choice(lottery_parts)]
print(f"{winning_combo} wins a prize")

# 9-15
trials = 0
while True:
    trials += 1
    test_combo = [choice(lottery_parts), choice(lottery_parts), choice(lottery_parts), choice(lottery_parts)]
    if test_combo == winning_combo:
        print(f"Took {trials} trials to win")
        break

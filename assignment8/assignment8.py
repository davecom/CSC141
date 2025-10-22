# 8-1
def display_message():
    print("We are learning about functions...")

display_message()

# 8-2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Good to Great")

# 8-3 & 8-4
def make_shirt(message="I Love Python", size="Large"):
    print(f"You made a size {size} shirt with {message} printed on it.")

make_shirt("Good Morning", "Medium")
make_shirt(message="Good Morning", size="Medium")
make_shirt()
make_shirt(size="Large")
make_shirt(message="Go Team")

# 8-5
def describe_city(city, country="USA"):
    print(f"{city} is in {country}")

describe_city("New York")
describe_city("Los Angeles")
describe_city("Tokyo", "Japan")

# 8-6
def city_country(city, country="USA"):
    return f"{city} is in {country}"

print(city_country("New York"))
print(city_country("Los Angeles"))
print(city_country("Tokyo", "Japan"))

# 8-7
def make_album(artist, title, num_tracks=None):
    album = {"artist" : artist, "title" : title}
    if num_tracks != None:
        album["num_tracks"] = num_tracks
    return album

album1 = make_album("Michael Jackson", "Thriller")
album2 = make_album("Offspring", "Americana")
album3 = make_album("Beatles", "Abby Road", 12)
print(album1)
print(album2)
print(album3)

# 8-8
# while True:
#     title = input("What is the album's title (or quit)?")
#     if title == "quit":
#         break
#     artist = input("Who is the album artist?")
#     print(make_album(title, artist))

# 8-9
def show_messages(messages):
    for message in messages:
        print(message)

l = ["Hi", "Hey", "Bye"]
show_messages(l)

# 8-10 & 8-11
def send_messages(messages, sent_messages):
    for message in messages:
        print(message)
        sent_messages.append(message)
sent = []
send_messages(l, sent)
print(l)
print(sent)

# 8-12
def build_sandwich(*ingredients):
    print("Ordered a sandwich with:")
    for ingredient in ingredients:
        print(ingredient)
build_sandwich("cheese", "turkey", "lettuce")
build_sandwich("peanut butter", "jelly")
build_sandwich("egg")

# 8-13

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

print(build_profile("Bill", "Gates", age=71, net_worth="really high", location="Seattle"))

# 8-14

def make_car(make, model, **characteristics):
    characteristics["make"] = make
    characteristics["model"] = model
    return characteristics

print(make_car("Ford", "Mustang", color="red", cylinders=6, location="New York"))
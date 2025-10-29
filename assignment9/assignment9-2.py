#9-10

from assignment9 import Restaurant

r4 = Restaurant("McDonalds", "Fast Food")
r4.describe_restaurant()

from assignment9 import User, Privileges, Admin
p2 = Privileges(["run script", "cancel time"])
a2 = Admin("Bee", "Arthur", "b@a.com", p2)
a2.privileges.show_privileges()


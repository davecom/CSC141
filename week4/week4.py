# Using list comprehensions; can you write a program
# that will generate the even numbers from 2 to 20
# list comprehension looks like [item for item in list]
# for example [2 ** n for n in range(0,11)] generates the powers of 2 up to 10
evens = [n for n in range(2, 21)][0::2]
print(evens)
evens = [n * 2 for n in range(1,11)]
print(evens)
evens = [n for n in range(2, 21)[0::2]]
print(evens)
evens = [n for n in range(2, 21)[0:19:2]]
print(evens)
# can you rewrite the evens list comprehension using the mod (%) operator?
evens = [n if n % 2 == 0 else 0 for n in range(2,21)]
print(evens)
evens = [n for n in range(2,21) if n % 2 == 0]
print(evens)
evens_doubled = [n * 2 for n in range(2,21) if n % 2 == 0]
print(evens_doubled)
# (1) Make a list in Python.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# (2) Adding items to a list.
#NOTE: This is useful when you have an empty list and want to add to it.

motorcycles.append('ducati')
print(motorcycles)

# (3) Removing an item from a list.

motorcycles.remove('ducati')
print(motorcycles)

# (4) Adding an item to a specific point within the list.
motorcycles.insert(0, 'ducati')
motorcycles.insert(2, 'triumph')
print(motorcycles)

# (5) Removing specific item from a list; "Triumph" in this case.
del motorcycles[2]
print(motorcycles)

# (6) To pop a value.
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
motorcycles.append('suzuki')
motorcycles.append('triumph')

# (7) Working with popped items. Triumph used because of append.
last_owned = motorcycles.pop()
print("My last owned motorcyle was a " + last_owned.title() + ".\n")

# (8) Removing values by name.
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

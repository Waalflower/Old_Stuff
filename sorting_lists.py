#Alphabatize a list. 9/3/2016
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Reverse alphabatize a list.
cars.sort(reverse=True)
print(cars)

#Temporarily sort/reverse sort a list.
print(sorted(cars))
print(cars)
#NOTE: cars.reverse() and cars.sort(reverse=True) are NOT the same.
#Reverse just reversed the order, not reverse alphabatize.

#Finding how many items are in a list.
print(len(cars))

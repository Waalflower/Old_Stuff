#Writting a list myself without step by step. 9/4/2016
pizzas = ['mushroom', 'spinach', 'pepperoni', 'cheese', 'sardine', 'pineapple']
print("The first three toppings are:")
print(pizzas[:3])

print("\nTwo items in the middle of the list are:")
print(pizzas[2:4])

print("\nThe last three items on the list are:")
print(pizzas[3:])

my_pizza = ['mushroom', 'spinach', 'cheese']
friend_pizza = my_pizza[:]
my_pizza.append('onion')
friend_pizza.append('pepperoni')

print("\nMy favorite pizzas are:")
print(my_pizza)
print("My freind's favorite pizzas are:")
print(friend_pizza) 

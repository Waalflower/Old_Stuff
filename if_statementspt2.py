#Part 2 of if statements. 9/6/2016
available_toppings = ['mushrooms', 'olives', 'green peppers', 
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, " + requested_topping + " is not available.")
print("\nYour pizza is ready!")

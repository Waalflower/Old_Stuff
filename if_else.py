#Testing if and else statements. 9/5/2016
age = 17

if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")
	
#Using elif for amusement park admission rates.
age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

#Condensing all of the above into simpler code. NOTE: Multiple ELIFs
#are possible. ALSO, else is NOT required.
age = 19

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5

print("Your admission cost is $" + str(price) + ".") #See how neat tis?

"""If you want to see if multiple conditions are met, use multiple IF
statements"""

requested_topping = ['cheese', 'pepperoni']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms")
if 'pepperoni' in requested_topping:
    print("\nAdding pepperoni")
if 'cheese' in requested_topping:
    print("Adding cheese")
    
print("\nYour pizza is ready for pickup!")

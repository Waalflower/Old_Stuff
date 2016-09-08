#Using the 'if' statements. 9/5/2016
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else: 
		print(car.title())

#The != means "does not equal". If this turns out true, it runs da code.
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")

#If statements work with numbers too.
answer = 7
if answer != 42:
	print('That is not correct. Please try again.')
	
#How to check multiple values at once. Use "and"
age_0 = 22
age_1 = 18
print(age_0 <= 21 and age_1 >= 21) #False
print(age_0 >=21 or age_1 >= 21) #True

#Checking if an item is on a list
requested_topping = ['mushroom', 'onions', 'pineapple']
print('mushroom' in requested_topping) #Results in true.
print('pepperoni' in requested_topping) #Results in false.

#Checking whether a value is not in a list.
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")
	
#Boolean Expressions
game_active = True
can_edit = False

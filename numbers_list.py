#To make a numerical list with ranges. 9/2/2016
#NOTE: Putting range (1,6) will result in numbers 1-5. Remember this!
for value in range(1,6):
	print(value)
	
#To create a list of ranges quickly.
numbers = list(range(1,6))
print(numbers)

#An example of how to get only even numbers.
even_numbers = list(range(2,11,2))
print(even_numbers)

#Finding square numbers in a sequence.
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
	
print (squares)

#Finding min, max, and sum of a list.
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#Simpler way to find squares in a range.
squares = [value**2 for value in range(1,11)]
print(squares)

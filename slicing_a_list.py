#Slicing a list. 9/4/2016
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#This will give you Charles, Martina, and Michael.

print(players[:4])
"""With no specified starting point, Python starts from the beginning. So in the above example, it will print everyone except Eli. Similarly, having a start point with no specified end point will continue until it reaches the end of a list"""
print(players[2:])

#If you want to loop a sliced list.
print("Here are the first three players of my team:")
for player in players[:3]:
	print(player.title())

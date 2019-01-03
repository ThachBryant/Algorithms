#given two numbers find their product using recursion

x = 5
y = 30	# this cuts down on total recursive call

def recursive_method(x,y):
	# this cuts down on total recursive call, prevents recursion error
	if x < y: 
		return recursive_method(y, x)
	if y == 0:
		return 0
	return x + recursive_method(x, y-1)


print (x * y)
print(recursive_method(5,30))

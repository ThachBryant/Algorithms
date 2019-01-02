#given a string, find the first uppercase character
#solve using a iterative solution, and use another way using recrusion.

input_str_1 = 'lucidProgramming'
input_str_2 = 'lucidproGramming'
input_str_3 = 'lucidprogramming'

def find_uppercase_iterative(input_str):
	for i in range(len(input_str)):
		if input_str[i].isupper():
			return input_str[i]
	else:
		return 'No uppercase letter found'


print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))
print '============'

def find_uppercase_recursion(input_str,idx=0):
	if input_str[idx].isupper():
		return input_str[idx]
	if idx == len(input_str) - 1:
		return "No uppercase character found"
	return find_uppercase_recursion(input_str,idx+1)

print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))



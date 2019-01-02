# Given a string, calculate the length of the string

input_str = "LetsProgram"

print(len(input_str))

def iterative_string_len(input_str):
	count = 0
	for i in range(len(input_str)):
		count +=1
	return count


def recursive_string(input_str):
	if input_str == '':
		return 0
	return 1 + recursive_string(input_str[1:])


print(iterative_string_len(input_str))

print(recursive_string(input_str))
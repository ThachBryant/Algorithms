# The sequence starts with the number 1:
# 1 
# we then say how many of each integer exists in the squence. for example
# there is one 1, which gives the next term 11
# given an n value, print the entire nth sequence


def next_number(s):
	result = []
	i = 0
	while i < len(s):
		count = 1
		while i + 1 < len(s) and s[i] == s[i+1]:
			i+= 1
			count += 1
		result.append(str(count) + s[i])
		i += 1
	return ''.join(result)

s="1"
n = 4
for i in range(n-1):
	s = next_number(s)
	print(s)

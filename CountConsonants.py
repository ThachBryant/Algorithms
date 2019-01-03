#given a string, count the number of consonants
# These are letters that are not a vowel

input_str_1 = 'abc de'
input_str_2 = 'LeTsPrOgRaM'
vowels = 'aeiou'

def iterative_solution(input_str):
	count = 0
	for i in range(len(input_str)):
		if input_str[i].lower() not in vowels and input_str[i].isalpha():
			count += 1
	return count

def recursive_solution(input_str):
	if input_str == '':
		return 0
	if input_str[0].lower() not in vowels and input_str[0].isalpha():
		return 1 +recursive_solution(input_str[1:])
	else:
		return recursive_solution(input_str[1:])
print(iterative_solution(input_str_1))
print(iterative_solution(input_str_2))
print '+++++++++++++++++'
print(recursive_solution(input_str_1))
print(recursive_solution(input_str_2))
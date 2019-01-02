data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 5

# Slowest, o(linear)
def linear_search(data, target):
	for num in range(len(data)):
		if data[num] == target:
			return True
	return False

#Iterative Binary Search
#Faster, O(log)
def binary_search_iterative(data, target):
	low = 0
	high = len(data) - 1
	while low <= high:
		mid =(low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False
# Fastest, 
def recursive_binary_search(data, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return recursive_binary_search(data, target, low, mid-1)
		else:
			return recursive_binary_search(data, target, mid+1, high)


print(linear_search(data, target))
print(binary_search_iterative(data,target))
print(recursive_binary_search(data, target, 0, len(data)-1))


			


# we want to find a optimal way to assign task to workers, assuming each worker
#must take two tasks and each take a fixed amount of time
#want the time it takes to complete all tasks to be minimized. 

A = [6, 3, 2, 7,5,5]
A = sorted(A)

for i in range(len(A)//2):
	print(A[i], A[~i])

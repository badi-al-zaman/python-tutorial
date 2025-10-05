def mysum(*numbers): # * Mean Passing many arguments
	count = 0
	for num in numbers:
		count += num
	return count

print(mysum(1,2,3,4,5)) # 15
list = [1, 5, 8 , 10 , 15]

def add_list(x):
	total = 0
	for i in range(len(x)):
		total = x[i] + 25
	return total
		
	
print "I just made these sexy numbers to make" + " " + str(add_list(list))

def pascal(n) :
	if n == 0:
		return 
	else :
		if n == 1:
			return n
		else :
			return pascal(n-1)


for i in range(4):
	print pascal(i)

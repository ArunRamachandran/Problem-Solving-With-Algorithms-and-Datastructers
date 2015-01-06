def search(lst, n): 
	if lst == []:
		print "Empty !"
		return False
	else :
		x = lst.pop()
		if n == x:
			print "n : %d , lst.pop() : %d" % (n, x)
			return True
		else :	
			print "n : %d , lst.pop() : %d" % (n, x)
			return search(lst, n)

case = search([1,2,3,4], 3)
print case


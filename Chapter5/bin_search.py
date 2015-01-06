""" bin. search """

def bin_search(lst, item) :
	first = 0
	last  = len(lst) - 1
	found = False
	
	while first <= last and not found:
		midpoint = (first + last) // 2
		#print "MidElement : %d" % (lst[midpoint])
		if item == lst[midpoint]:
			found = True
		else :
			if item < lst[midpoint]:
				last = midpoint - 1
			else :
				first = midpoint + 1

	return found

print bin_search([9, 10, 20, 30, 40, 50, 55, 79], 55)
		

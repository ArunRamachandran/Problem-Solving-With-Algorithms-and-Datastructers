def list_sum(lst) :
	if len(lst) == 1:
		return lst[0]
	else :
		return lst[0] + list_sum(lst[1 : ])

print list_sum([1,2,3,4,5])
